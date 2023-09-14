import gurobipy as gp
from gurobipy import GRB

from gurobi_init import e


if __name__ == '__main__':
    model = gp.Model(env=e, name='QP')
    
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x')
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x')
    z = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x')
    
    model.setObjective(x * x + y * z)
    
    quad_expr = gp.QuadExpr()
    
    quad_expr.addTerms(1, x, y)
    quad_expr.addTerms(1, y, z)

    model.addQConstr(quad_expr <= z + 5)
    model.addConstr(x + z <= 6)
    
    model.optimize()
    
