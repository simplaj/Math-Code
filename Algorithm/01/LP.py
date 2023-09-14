from gurobi_init import e
from gurobipy import GRB
import gurobipy as gp

model = gp.Model(env=e, name='LP')
x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x')
y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='y')
z = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='z')

model.setObjective(x - 2 * y + 2 * z)

model.addConstr(-x + y <= 1)
model.addConstr(3 * x + 2 * y + z <= 12)

model.optimize()

print(x.X, y.X, z.X)
