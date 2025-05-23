"""一个口袋中放有12个球，已知其中3个是红的，3个是白的，6个是黑的，现从中任取8个，问共有多少种可能的颜色搭配？"""
# list0 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]
# list1 = []
# for i1 in range(len(list0)):
#     for i2 in range(len(list0)):
#         for i3 in range(len(list0)):
#             for i4 in range(len(list0)):
#                 for i5 in range(len(list0)):
#                     for i6 in range(len(list0)):
#                         for i7 in range(len(list0)):
#                             for i8 in range(len(list0)):
#                                 a = list0[i1] + list0[i2] + list0[i3] +list0[i4] + list0[i5] + list0[i6] + list0[i7] + \
#                                     list0[i8]
#                                 list1.append(a)
#                                 print(list1)
# for j in range(len(list1)):
#     for k in range(j,len(list1)):
#         if list1[j] == list[k]:
#             list1.pop(k)
# print(list1)
# print(len(list1))
"""我觉得这是可行的，但是要算12**8次，上亿次了，算了很久还没算完..."""
i = 0
for r in range(4):
    for w in range(4):
        for b in range(7):
            if r + w + b == 8:
                print(r, w, b)
                i += 1
print(i)
"""唉，我好菜
唉，明明是简单的数学问题"""
