'''l1**2+l2**2+l3**2+lk**2=n,l、n均为正整数'''
'''k=3时'''


def find_solutions(n):
    # 确保n是正整数
    if n <= 0:
        return "输入错误: n必须是大于0的整数"

    solutions = []
    max_val = int(n ** 0.5)  # 因为l1, l2, l3都是正整数，它们的最大值不会超过sqrt(n)

    for l1 in range(1, max_val + 1):
        for l2 in range(l1, max_val + 1):  # 从l1开始避免重复组合
            l3_squared = n - (l1 ** 2 + l2 ** 2)

            # 检查l3_squared是否非负
            if l3_squared >= 0:
                l3 = int(l3_squared ** 0.5)

                # 检查l3是否是正整数且其平方等于剩余的部分
                if l3 > 0 and l3 >= l2 and l3 ** 2 == l3_squared:
                    solutions.append((l1, l2, l3))

    return solutions


# 输入n值
n = int(input("请输入一个大于0的整数值n: "))
solutions = find_solutions(n)

if isinstance(solutions, str):
    print(solutions)
else:
    if not solutions:
        print(f"对于n={n}, 没有找到满足条件的(l1, l2, l3)组合。")
    else:
        print(f"对于n={n}, 找到了以下解：")
        for solution in solutions:
            print(solution)

