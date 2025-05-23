def find_solutions(n, k, current_solution=[], start=1):
    if k == 0:
        # 如果k为0，检查当前解是否满足等式
        if sum(x ** 2 for x in current_solution) == n:
            return [current_solution]
        else:
            return []

    solutions = []
    max_val = int((n - sum(x ** 2 for x in current_solution)) ** 0.5)

    # 尝试从start到max_val的所有可能值
    for l in range(start, max_val + 1):
        # 检查剩余部分是否足够大以继续搜索
        remaining = n - (sum(x ** 2 for x in current_solution) + l ** 2)
        if remaining >= 0:
            # 递归调用，减少k的值，并将当前l添加到当前解中
            new_solutions = find_solutions(n, k - 1, current_solution + [l], l)
            solutions.extend(new_solutions)

    return solutions


# 输入n和k值
n = int(input("请输入一个大于0的整数值n: "))
k = int(input("请输入一个大于0的整数k（l的数量）: "))

if n <= 0 or k <= 0:
    print("输入错误: n和k必须是大于0的整数")
else:
    solutions = find_solutions(n, k)

    if not solutions:
        print(f"对于n={n}和k={k}, 没有找到满足条件的解。")
    else:
        print(f"对于n={n}和k={k}, 找到了以下解：")
        for solution in solutions:
            print(solution)
