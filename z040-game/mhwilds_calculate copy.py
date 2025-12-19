from pathlib import Path
import unicodedata

def dic() -> dict:
    weapon_dict = {"攻击":'1', "会心":'2'}
    reverse_weapon_dict = {v:k for k,v in weapon_dict.items()}

    series_dict = {}
    with open(Path(__file__).parent / 'ct_series.txt', "r", encoding='utf-8') as f:
        for line in f:
            number, series_name = line.strip().split()
            series_dict[series_name] = number
    reverse_series_dict = {v:k for k,v in series_dict.items()}

    group_dict = {}
    with open(Path(__file__).parent / 'ct_group.txt', "r", encoding='utf-8') as f:
        for line in f:
            number, group_name = line.strip().split()
            group_dict[group_name] = number
    reverse_group_dict = {v:k for k,v in group_dict.items()}

    return weapon_dict, reverse_weapon_dict, series_dict, reverse_series_dict, group_dict, reverse_group_dict

def get_visual_width(s: str) -> int:
    """计算字符串在终端中的视觉宽度，汉字等全角字符计为2，英文等半角字符计为1。"""
    width = 0
    for char in s:
        if unicodedata.east_asian_width(char) in ('F', 'W', 'A'):
            width += 2
        else:
            width += 1
    return width

def format_dict_for_display(d: dict, columns: int = 3) -> str:
    """将字典的键值对格式化为多列对齐的字符串，以便清晰地显示。"""
    if not d:
        return ""

    # 1. 创建 "键:值" 格式的字符串列表
    items_as_str = [f"{key}:{value}" for key, value in d.items()]
    # items = list(d.items()),

    # 2. 计算所有项中的最大视觉宽度
    max_visual_width = max(get_visual_width(item) for item in items_as_str) if items_as_str else 0
    
    # 3. 确定列宽（最大宽度 + 间距）
    col_width = max_visual_width + 4

    lines = []
    # 4. 按列数分组处理
    for i in range(0, len(items_as_str), columns):
        row_items = items_as_str[i:i + columns]
        line_str = ""
        # 5. 对当前行的每一项，计算并填充所需空格以实现对齐
        for item in row_items:
            visual_width = get_visual_width(item)
            padding = " " * (col_width - visual_width)
            line_str += item + padding
        lines.append(line_str)

    return "\n" + "\n".join(lines)


def from_skill_to_code() -> str :
    weapon_dict, reverse_weapon_dict, series_dict, reverse_series_dict, group_dict, reverse_group_dict = dic()

    weapon_list = [f"{key}:{value}" for key, value in weapon_dict.items()]
    weapon_options = "/".join(weapon_list)
    series_options = format_dict_for_display(series_dict)
    group_options = format_dict_for_display(group_dict)

    weapon_type = input(f"请输入武器零件类型 ({weapon_options}):")
    if weapon_type.isdigit():
        weapon_type = str(reverse_weapon_dict.get(weapon_type))
    series_name = input(f"请输入系列名称，可选系列包括：{series_options}\n> ")
    if series_name.isdigit():
        series_name = str(reverse_series_dict.get(series_name))
    group_name = input(f"请输入组合技能名称，可选组合包括：{group_options}\n> ")
    if group_name.isdigit():
        group_name = str(reverse_group_dict.get(group_name))

    weapon_code = int(weapon_dict.get(weapon_type))
    series_code = int(series_dict.get(series_name))
    group_code = int(group_dict.get(group_name))

    # 可以有更简短的写法。其实好像差不多，可读性还不如上面的
    # weapon_code = (int(weapon_dict.get(weapon_type)) if not weapon_dict.get(weapon_type).isdigit() else str(reverse_weapon_dict.get(weapon_type)))

    if weapon_code and series_code and group_code:
        skill_code = str(series_code * 15 + group_code +2)
        # if len(skill_code) == 2:
        #     address1 = '0'
        #     address2 = skill_code[0]
        #     address3 = skill_code[1]
        #     ce_used_code = f"{address1}{weapon_code}0{address2}{weapon_code}0{address3}{weapon_code}"
        # elif len(skill_code) == 3:
        #     address1 = skill_code[0]
        #     address2 = skill_code[1]
        #     address3 = skill_code[2]
        #     ce_used_code = f"{address1}{weapon_code}0{address2}{weapon_code}0{address3}{weapon_code}"

        # zfill(3)方法用于在字符串的左侧填充0，直到达到指定的总长度。
        # ljust(3, '0')方法也可以实现，这个默认是填充空格。rjust是往右填充
        skill_code = skill_code.zfill(3)
        ce_used_code = (f"{str(skill_code)[0]}{weapon_code}0{str(skill_code)[1]}{weapon_code}0"
                        f"{str(skill_code)[2]}{weapon_code}")
        return ce_used_code
    else:
        return "输入有误，请检查输入的武器类型、系列名称和分组名称。"



if __name__ == "__main__":
    print(from_skill_to_code())

