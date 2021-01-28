from pulp import LpProblem, LpMaximize, LpVariable, value

m = LpProblem(sense=LpMaximize)
x = LpVariable('x', lowBound=0)
y = LpVariable('y', lowBound=0)

m += 100 * x + 100 *y
m += x + 2 * y <=16
m += 3 * x + y <=18
m.solve()

print(value(x), value(y))
