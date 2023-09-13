from pyomo.environ import *

# 创建一个具体的模型对象
model = ConcreteModel()

# 定义整数规划变量
model.x = Var(within=Integers)

# 定义目标函数和约束条件
model.obj = Objective(expr=model.x + 10, sense=minimize)
model.con = Constraint(expr=model.x >= 5)

# 构建优化器并求解整数规划问题
solver = SolverFactory('gurobi')
solver.solve(model)

# 输出结果
print(value(model.x))