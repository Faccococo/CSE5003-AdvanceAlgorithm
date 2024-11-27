from scipy.optimize import linprog

# 定义目标函数的系数（注意 linprog 需要最小化，因此取负号来实现最大化）
c = [1, -2]

# 定义不等式约束条件矩阵和向量
A = [[3, 2],  # x1 + x2 <= 4
     [-1, 1]]  # x2 <= 3
b = [7, 2]

# 定义变量的范围
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# 调用 linprog 解决问题
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# 输出结果
if result.success:
    print("优化成功！")
    print(f"最大值: {-result.fun}")
    print(f"x1: {result.x[0]}")
    print(f"x2: {result.x[1]}")
else:
    print("优化失败！")
