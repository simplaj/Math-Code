from cvxopt import matrix, solvers

# 定义二次规划的系数矩阵和向量
P = matrix([[1.0, 0.4], [0.4, 1.0]])
q = matrix([-1.0, -2.0])

# 定义约束条件的系数矩阵和右侧常数向量
G = matrix([[-1.0, 0.0], [0.0, -1.0]])
h = matrix([0.0, 0.0])

# 求解二次规划问题
sol = solvers.qp(P, q, G, h)
print(sol['x'])