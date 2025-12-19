from pathlib import Path

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

def format_dict_for_display(d: dict, columns: int = 5) -> str:
    items = list(d.items())
    if not items:
        return ""

    max_len = max(len(item) for item in items)
    col_width = max_len + 4  

    lines = []
    for i in range(0, len(items), columns):

        row_items = items[i:i+columns]

        lines.append("".join(f"{item[0]:<{col_width}}" for item in row_items))
    

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
        
        # .zfill() 方法用于在字符串的左侧填充指定的字符（默认为空格），直到达到指定的总长度。
        skill_code = str(skill_code).zfill(3)
        ce_used_code = f"{skill_code[0]}{weapon_code}0{skill_code[1]}{weapon_code}0{skill_code[2]}{weapon_code}"
        return ce_used_code
    else:
        return "输入有误，请检查输入的武器类型、系列名称和分组名称。"



if __name__ == "__main__":
    print(from_skill_to_code())

