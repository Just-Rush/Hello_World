"""对一组数进行简单排序（冒泡排序）"""
"""利用冒泡排序，从小到大排"""
list1 = [4, 1, 78, 25, 52, 13, 90, 67, 87, 90, 123]
# for i in list1:
#    xx = i + 1
#    print(xx)
""" 要搞清楚for循环，遍历列表的意义，是对列表中每一个元素进行使用，但是并不对元素的值做处理------代码中间用""""""好像会报一些错误"""
#     for j in list1:
#         if i > j:
#             k = j
#             i = k
#             j = i
# print(list1)

for i1 in range(len(list1)):  # 应为类型 'collections.Iterable'，但实际为 'int'------之前没有range------
    # 再之前是对list1遍历，就会出问题，因为i1会引用成4，1，78等，后面要用list[]就会超出列表的范围
    # 最后这里因为只有一个列表且数量已知，所以用range(11)也可以，但这种方法显然更通用
    for j1 in range(i1+1, len(list1)):  # 这里因为要避免与i1的值重复，所以起始项不同
        # if i1 > j1:------i1始终小于j1...又是没有区分开列表的值与列表的索引，还不够熟悉。现在的i1、j1都变成了list1的索引
        if list1[i1] > list1[j1]:
            k = list1[i1]
            list1[i1] = list1[j1]
            # list1[j1] = list1[i1]------这样的话等于list1[j1]值没有变化...要利用中间变量
            list1[j1] = k
print(list1)
