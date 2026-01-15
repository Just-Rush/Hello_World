from pathlib import Path
import shutil
import re
aim_path = r""

def delete_photo(path):
    for file in Path(path).rglob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            changed_file = re.sub(r'\[\]\([a-zA-Z0-9]+\)', '图片', content)

