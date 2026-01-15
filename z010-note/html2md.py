from pathlib import Path
import shutil

aim_path = r'D:\local_file\bwl'
# target_path = r"D:\local_file\bwl"
def replace_suffix(path):
    dest_path = Path(path)
    # target_path = Path(target_path)
    # target_path.mkdir(parents=True, exist_ok=True)
    if not dest_path.exists():
        print("路径不存在")
        return
    
    html_files = list(dest_path.rglob("*.html"))
    for html_file in html_files:
        # md_file = target_path / html_file.with_suffix('.md').name
        md_file = html_file.parent / f"{html_file.stem}(1).md"
        shutil.copy2(html_file, md_file)
        print(f"已将 {html_file} 重命名")

if __name__ == "__main__":
    replace_suffix(aim_path)