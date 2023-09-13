from scipy.optimize import minimize

# 定义目标函数
def objective(x):
    return x[1] ** 2 + x[1] * x[2]

# 定义约束条件
def constraint(x):
    return [x[0] + x[1] - 3, x[0] - x[2]]

# 定义初始点
x0 = [1, 2, 3]

# 求解非线性规划问题
res = minimize(objective, x0, constraints={'type': 'eq', 'fun': constraint})
print(res)