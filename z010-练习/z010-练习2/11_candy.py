"""10个小孩围成一圈分糖果，老师顺次分给每个人的糖块数为12，2，8，22，16，4，10，6，14，20。
然后按下列规则调整，所有小孩同时把自己的糖果分一半给右边的小孩，糖块数变为奇数的人，再向老师补要一块，问经过多少次调整后，大家的糖块一样多，且每人多少块？"""
list1 = [12, 2, 8, 22, 16, 4, 10, 6, 14, 20]
list2 = [12, 2, 8, 22, 16, 4, 10, 6, 14, 20]
a = 0
while True:
    for e in range(len(list1)):
        list2[e] = list1[e]/2 + list1[e-1]/2
        if list2[e] % 2 != 0:
            list2[e] += 1
        # a += 1  # 在这个地方计数不对，这里是计算将每次分配都算作1次

    for ee in range(len(list1)):
        list1[ee] = list2[ee]
    print(list2)
    a += 1
    if list2[1] == list2[2] == list2[3] == list2[4] == list2[5] == list2[6] == list2[7] == list2[8] == list2[9] \
            == list2[0]:  # 这个地方感觉很蠢，但是想到的用循环又不太对
        break
    # for i in range(len(list2)):
    #     for j in range(i,len(list2)):
    #         if list2[i] == list2[j]:
    #             break
"""答案用的方法很不错，值得借鉴"""
# equal = 0
# for i in range(len(list1)):
#     if list1[0] == list2[i]:
#         equal = equal + 1
#
# if equal == len(list1):
#     print('经过', count, '次传送', '大家手中糖果数一样，为', list1[0], '颗')
#     # print(count,list[0])
#     break

print(a)
