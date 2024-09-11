from sympy import symbols, Eq, solve
x = symbols('x')
equation = Eq(x + 5, 10)
solution = solve(equation, x)
print(solution)
