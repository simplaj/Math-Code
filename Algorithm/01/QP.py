import gurobipy as gp
from gurobipy import GRB

from gurobi_init import e


if __name__ == '__main__':
    model = gp.Model(env=e, name='QP')
    
    x = model.addVar(lb=0, vtype=GRB.BINARY, name='x')
    y = model.addVar(lb=0, vtype=GRB.BINARY, name='y')
    z = model.addVar(lb=0, vtype=GRB.BINARY, name='z')
    
    model.setObjective(x * x + y * z, GRB.MAXIMIZE)
    
    quad_expr = gp.QuadExpr()
    
    quad_expr.addTerms(1, x, x)
    quad_expr.addTerms(1, x, y)
    quad_expr.addTerms(1, y, z)

    model.addQConstr(quad_expr <= z + 5)
    model.addConstr(3 * x + 2 * z <= 4)
    
    model.optimize()
    print('x = ', x.x)
    print('y = ', y.x)
    print('z = ', z.x) 
    
