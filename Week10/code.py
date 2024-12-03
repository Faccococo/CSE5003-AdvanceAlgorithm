from scipy.optimize import linprog

# 定义目标函数的系数
c = [-1, -2, -3]  # 注意：这里取负号，因为 linprog 默认是求最小化问题

# 定义约束条件矩阵和右端向量
A = [
    [1, 2, 3],
    [2, 1, 1],
    [1, 1, 2],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]
]

b = [6, 4, 5, 0, 0, 0]

# 求解线性规划问题
result = linprog(c, A_ub=A, b_ub=b, method="highs")

# 输出结果
if result.success:
    print("Optimal value:", -result.fun)  # 恢复为最大化问题的结果
    print("Optimal solution:", result.x)
else:
    print("No solution found")