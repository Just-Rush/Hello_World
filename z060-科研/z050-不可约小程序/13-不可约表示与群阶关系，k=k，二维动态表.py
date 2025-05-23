import time


def find_solutions_dp(n, k):

    # 初始化DP表
    dp = [[[] for _ in range(n + 1)] for _ in range(k + 1)]

    # 对于k=1的情况，初始化基础解
    for i in range(1, int(n ** 0.5) + 1):
        if i * i <= n:
            dp[1][i * i].append([i])

    # 填充DP表
    for i in range(2, k + 1):  # 使用的平方数的数量
        for j in range(1, n + 1):  # 当前的和
            for l in range(1, int(j ** 0.5) + 1):  # 可能的l值
                l_squared = l * l
                if l_squared > j:
                    break
                if dp[i - 1][j - l_squared]:
                    for prev_solution in dp[i - 1][j - l_squared]:
                        if not prev_solution or l >= prev_solution[-1]:  # 确保非降序
                            dp[i][j].append(prev_solution + [l])

    return dp[k][n]



# 输入n和k值
n = int(input("请输入一个大于0的整数值n: "))
k = int(input("请输入一个大于0的整数k（l的数量）: "))


st = time.time()
if n <= 0 or k <= 0:
    print("输入错误: n和k必须是大于0的整数")
else:
    solutions = find_solutions_dp(n, k)

    if not solutions:
        print(f"对于n={n}和k={k}, 没有找到满足条件的(l1, l2, ..., lk)组合。")
    else:
        print(f"对于n={n}和k={k}, 找到了以下解：")
        for solution in solutions:
            print(solution)
end = time.time()
print(end - st)



'''使用动态规划（Dynamic Programming, DP），它可以避免重复计算，并且在某些情况下比递归更快。

我们可以构建一个二维DP表 dp[i][j]，其中 i 表示使用的平方数的数量，j 表示当前的和。dp[i][j] 将存储所有可能的组合，这些组合是由 i 个平方数组成并且它们的和为 j。
在这个动态规划版本中：

dp[i][j] 存储了由 i 个平方数组成并且它们的和为 j 的所有非降序排列的解。
我们首先处理 k=1 的情况，即单个平方数等于 j 的情况。
然后我们逐步增加 k 的值，通过将新的平方数 l 添加到之前的解中来更新 dp 表。
为了确保非降序，我们在添加新的 l 时检查它是否不小于当前解中的最后一个元素。
这种方法利用了之前计算的结果，避免了大量的重复计算，因此在较大的 n 和 k 值下会更加高效。但是，需要注意的是，当 n 和 k 非常大时，即使是动态规划也可能需要大量的内存和时间。在这种情况下，可能还需要进一步的优化或采用其他策略。'''