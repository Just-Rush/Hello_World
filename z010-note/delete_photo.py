from pathlib import Path
import shutil
import re
aim_path = r"D:\临时文件夹\梦"

def delete_photo(path):
    for file in Path(path).rglob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            # 匹配 ![](任意内容) 的图片语法
            changed_file = re.sub(r'!\[\]\([^)]+\)', '图片', content)
        with open(file, "w", encoding="utf-8") as f:
            f.write(changed_file)


if __name__ == "__main__":
    delete_photo(aim_path)

