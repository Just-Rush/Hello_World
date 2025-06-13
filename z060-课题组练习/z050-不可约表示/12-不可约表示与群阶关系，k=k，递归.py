import time


def find_solutions(n, k, current_solution=[], start=1):
    if k == 0:
        # 1.如果k为0，检查当前解是否满足等式; 2.此处不是为了防止输入的k为0，是因为后续有k-1
        if sum(x ** 2 for x in current_solution) == n:
            return [current_solution]  # 这个地方return是将值传到21行
        else:
            return []

    solutions = []  # 这里只是为了定一个变量，跟占位一样的
    max_val = int((n - sum(x ** 2 for x in current_solution)) ** 0.5)

    # 尝试从start到max_val的所有可能值
    for l in range(start, max_val + 1):
        # 检查剩余部分是否足够大以继续搜索
        remaining = n - (sum(x ** 2 for x in current_solution) + l ** 2)
        if remaining >= 0:
            # 递归调用，减少k的值，并将当前l添加到当前解中
            new_solutions = find_solutions(n, k - 1, current_solution + [l], l)  # 1.start替换为l，防止出现重复项，同时减少计算量；2.同时在这个地方进行递归了，就又回到了开头,
            # 暂时就不继续往下读了，但是当一个递归完成后，还是要继续向下的 3. 这个地方对c_s加了[l]
            solutions.extend(new_solutions)
        # else:
        #     return
        # 加上这两句后似乎可以些微提高一点点速度

    return solutions  # 最终这个sol是一个列表，并且返回函数值，但是注意在这一个函数里多次调用了它自己，所以返回函数后值后并不是结束整个函数的运行了，也许还在嵌套里。


# 输入n和k值
n = int(input("请输入一个大于0的整数值n: "))
k = int(input("请输入一个大于0的整数k（l的数量）: "))
st = time.time()
if n <= 0 or k <= 0:
    print("输入错误: n和k必须是大于0的整数")
else:
    solutions = find_solutions(n, k)

    if not solutions:  # if not判断后面的变量solutions是否为none，为none则继续。py中[]为none值
        print(f"对于n={n}和k={k}, 没有找到满足条件的(l1, l2, ..., lk)组合。")
    else:
        print(f"对于n={n}和k={k}, 找到了以下解：")
        for solution in solutions:
            print(solution)

end = time.time()
print(end - st)


'''引入了一个新的参数 start，它表示当前层递归尝试的起始值。初始调用时，start 设置为1。
在每次递归调用中，我们将 start 更新为当前选择的 l 值，这样在下一层递归中只会考虑大于或等于当前 l 的值。
这样做可以保证解是非降序的，从而避免了重复的组合。
这个方法有效地减少了不必要的计算，并且确保了输出的唯一性。例如，如果 k=3 并且 n=27，那么 (1, 1, 5) 和 (1, 5, 1) 将被视为相同的解，因为它们只涉及位置对调。通过这种方式，我们只会得到 (1, 1, 5) 作为有效解。'''