from pathlib import Path
import shutil
import re
aim_path = r"D:\临时文件夹\梦"

def delete_photo(path):
    for file in Path(path).rglob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            # 匹配 ![](任意内容) 的图片语法
            changed_content = re.sub(r'!\[\]\([^)]+\)', '图片', content)
        with open(file, "w", encoding="utf-8") as f:
            f.write(changed_content)

def transfer_time(path):
    for file in Path(path).rglob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        lines = content.splitlines()
        # 只检查第一行和第二行，找到其中出现的 6 位数字后转换为 20xx年xx月xx日
        for index in range(min(2, len(lines))):
            match = re.search(r'(?<!\d)(\d{6})(?!\d)', lines[index])
            if match:
                digits = match.group(1)
                replaced = f"20{digits[:2]}年{digits[2:4]}月{digits[4:6]}日"
                lines[index] = lines[index].replace(digits, replaced, 1)
                break
        changed_content = "\n".join(lines)
        if content.endswith("\n"):
            changed_content += "\n"
        with open(file, "w", encoding="utf-8") as f:
            f.write(changed_content)

if __name__ == "__main__":
    delete_photo(aim_path)
    transfer_time(aim_path)

