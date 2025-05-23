shop_list_618=["CPU","显卡","主板","固态硬盘"]
shop_list_618.append("内存")
shop_list_618.append("散热")
shop_list_618.remove("固态硬盘")
shop_list_618.append("电源")
shop_list_618.append("显示器")
shop_list_618.append("机箱")
#如何往清单中一次添加多个元素。
print(len(shop_list_618))
print(shop_list_618[4])
print(shop_list_618)

dictionary={"CPU":"13600kf","显卡":"4070S技嘉魔鹰还是啥",
            "内存":"64或32G","固态硬盘":"不急",
            "电源":"海韵？","显示器":"LG","散热":"不知",}
dictionary["机箱"]="不知"
# print(dictionary[3])，怎么查看字典中第几个元素
print(dictionary)
print(len(dictionary))
find=str(input("请输入您想查询的配件："))
print("您查询的配件型号为"+dictionary[find])
"""dictionary.keys(),返回所有键
dictionary.values()，返回所有值
dictionay.items()，返回所有键值对"""