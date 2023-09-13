from scipy.optimize import linprog

# 定义目标函数的系数向量
c = [1, -2, 2]

# 定义不等式约束条件的系数矩阵和右侧常数向量
A_ub = [[-1, 1, 0], [3, 2, 1]]
b_ub = [1, 12]

# 定义变量的取值范围，默认为非负数
x_bounds = [(0, None), (0, None), (0, None)]

# 求解线性规划问题
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds)
print(res)