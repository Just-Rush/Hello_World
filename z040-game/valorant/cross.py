import pygame
import sys
import ctypes
import time
import threading

class TopmostCrosshair:
    def __init__(self):
        pygame.init()
        
        # 获取屏幕信息
        self.screen_info = pygame.display.Info()
        self.screen_width = self.screen_info.current_w
        self.screen_height = self.screen_info.current_h
        
        # ========== 用户参数 ==========
        self.CROSSHAIR_COLOR = (255, 0, 0, 255)  # 红色
        self.TRANSPARENT_COLOR = (0, 0, 0)
        self.LINE_THICKNESS = 1
        self.CENTER_DOT_SIZE = 2
        # ============================
        
        # 创建窗口
        flags = pygame.NOFRAME | pygame.HWSURFACE | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags)
        pygame.display.set_caption("十字准星")
        
        # 设置窗口属性
        self.set_window_properties_enhanced()
        
        # 运行标志
        self.running = True
        self.clock = pygame.time.Clock()
        self.click_through = True
        
        # 启动强制置顶线程
        self.start_topmost_thread()
        
        # 运行主循环
        self.main_loop()
    
    def set_window_properties_enhanced(self):
        """增强的窗口属性设置"""
        if sys.platform == "win32":
            try:
                hwnd = pygame.display.get_wm_info()["window"]
                hwnd = pygame.display.get_wm_info()["window"]

                # 获取并保留已有扩展样式，然后在其上添加我们需要的标志
                GWL_EXSTYLE = -20
                WS_EX_LAYERED = 0x00080000
                WS_EX_TRANSPARENT = 0x00000020
                WS_EX_TOOLWINDOW = 0x00000080
                WS_EX_TOPMOST = 0x00000008
                WS_EX_COMPOSITED = 0x00040000
                WS_EX_NOACTIVATE = 0x08000000

                ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                ex_style |= WS_EX_LAYERED | WS_EX_TOOLWINDOW | WS_EX_TOPMOST | WS_EX_COMPOSITED | WS_EX_NOACTIVATE
                # 可选：保持或移除 WS_EX_TRANSPARENT（如果需要点击穿透则保留）
                ex_style |= WS_EX_TRANSPARENT

                ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex_style)

                # 只让背景色透明，避免全屏半透明窗口压暗游戏画面。
                LWA_COLORKEY = 0x01
                transparent_colorref = (
                    self.TRANSPARENT_COLOR[0]
                    | (self.TRANSPARENT_COLOR[1] << 8)
                    | (self.TRANSPARENT_COLOR[2] << 16)
                )
                ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, transparent_colorref, 0, LWA_COLORKEY)

                # 立即设置为顶层但不激活窗口（不夺取焦点）
                HWND_TOPMOST = -1
                SWP_NOMOVE = 0x0002
                SWP_NOSIZE = 0x0001
                SWP_NOACTIVATE = 0x0010
                SWP_FRAMECHANGED = 0x0020
                ctypes.windll.user32.SetWindowPos(
                    hwnd,
                    HWND_TOPMOST,
                    0, 0, 0, 0,
                    SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE | SWP_FRAMECHANGED
                )

                # 使用 ShowWindow 不激活地显示窗口
                SW_SHOWNA = 8
                ctypes.windll.user32.ShowWindow(hwnd, SW_SHOWNA)

                print("窗口属性设置完成（保留原始样式，使用分层透明 & 顶置）")
            except Exception as e:
                print(f"Windows API设置失败: {e}")

    def set_click_through(self, enable: bool):
        """开启或关闭点击穿透（WS_EX_TRANSPARENT）"""
        if sys.platform != "win32":
            return
        try:
            hwnd = pygame.display.get_wm_info()["window"]
            GWL_EXSTYLE = -20
            WS_EX_TRANSPARENT = 0x00000020
            ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            if enable:
                ex_style |= WS_EX_TRANSPARENT
            else:
                ex_style &= ~WS_EX_TRANSPARENT
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex_style)
            # 让更改立即生效
            SWP_NOMOVE = 0x0002
            SWP_NOSIZE = 0x0001
            SWP_NOACTIVATE = 0x0010
            SWP_FRAMECHANGED = 0x0020
            HWND_TOPMOST = -1
            ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE | SWP_FRAMECHANGED)
            self.click_through = enable
            print(f"点击穿透已设置为: {enable}")
        except Exception as e:
            print(f"设置点击穿透失败: {e}")
    
    def force_topmost(self):
        """强制窗口置顶"""
        if sys.platform == "win32":
            try:
                hwnd = pygame.display.get_wm_info()["window"]
                
                # 方法1: 使用SetWindowPos
                HWND_TOPMOST = -1
                SWP_NOMOVE = 0x0002
                SWP_NOSIZE = 0x0001
                SWP_NOACTIVATE = 0x0010
                SWP_SHOWWINDOW = 0x0040
                ctypes.windll.user32.SetWindowPos(
                    hwnd,
                    HWND_TOPMOST,
                    0, 0, 0, 0,
                    SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE | SWP_SHOWWINDOW
                )

                # 尝试将窗口带到最上层但不激活（不会抢焦点）
                try:
                    ctypes.windll.user32.BringWindowToTop(hwnd)
                except:
                    pass
                
                return True
            except:
                return False
        return False
    
    def start_topmost_thread(self):
        """启动强制置顶的守护线程"""
        def topmost_worker():
            while self.running:
                self.force_topmost()
                time.sleep(0.1)  # 每0.1秒强制置顶一次
        
        thread = threading.Thread(target=topmost_worker, daemon=True)
        thread.start()
    
    def draw_crosshair(self):
        """绘制十字准星"""
        self.screen.fill(self.TRANSPARENT_COLOR)
        
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        
        # 垂直线
        pygame.draw.line(
            self.screen, 
            self.CROSSHAIR_COLOR, 
            (center_x, 0), 
            (center_x, self.screen_height), 
            self.LINE_THICKNESS
        )
        
        # 水平线
        pygame.draw.line(
            self.screen, 
            self.CROSSHAIR_COLOR, 
            (0, center_y), 
            (self.screen_width, center_y), 
            self.LINE_THICKNESS
        )
        
        # 中心点
        pygame.draw.circle(
            self.screen, 
            self.CROSSHAIR_COLOR, 
            (center_x, center_y), 
            self.CENTER_DOT_SIZE
        )
    
    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    self.running = False
    
    def main_loop(self):
        """主循环"""
        while self.running:
            self.handle_events()
            self.draw_crosshair()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit(0)

if __name__ == "__main__":
    app = TopmostCrosshair()
