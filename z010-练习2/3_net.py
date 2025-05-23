"""中国有句俗语叫“三天打鱼两天晒网”。某人从1990年1月1日起开始“三天打鱼两天晒网”，问这个人在以后的以后的某一天中是打鱼还是晒网。（以2020年8月1日为例）"""
"""答案写的也很好，看看"""
# 写成一个用户输入然后查询的吧
time = input("请输入当前时间年份，格式如2020/08/01"+":")
# print(time)
year = int(time[0:4])  # 切片中从0开始数，A[0：3]，列表中索引为0，1，2的元素（即0到3-1个）------重点其实是列表的索引是从0开始的
# print(year)
mouth = int(time[5:7])
day = int(time[8:10])  # 在这里用int做变化和在计算时用int做变化效果应该是一样的
print(year, mouth, day)
i = 0
j = 0
for y in range(1990, year+1):
    if y % 4 == 0:  # 取余数符号------查了下说闰年是普通年能被4整除但是不能被100整除，世纪年必须要能被400整除才是。如1900就不是闰年。但是因为到不了一个世纪年，所以我这个好像也没问题。
        i = i+1
    else:
        j = j+1
dy = 365*j+366*i
dm = 0
for m in range(1, mouth+1):
    if m != 2 and m != 8 and m % 2 == 0:
        dm = dm+30
    elif m != 2 and m != 8 and m % 2 != 0:
        dm = dm + 31
    elif m == 8:
        dm = dm + 31
    elif m == 2 and year % 4 != 0:
        dm = dm + 28
    elif m == 2 and year % 4 == 0:
        dm = dm + 29
dd = day-1
days = dy+dm+dd
judgment = days % 5
if judgment <= 3:
    print('在打鱼')
elif judgment > 3:
    print('在晒网')


"""结果是对的，但是感觉可以狠狠的优化"""
