from sympy import *
a = 5
b = 4
g = 0
t = 5
m = 5
n = 5

x, y = symbols('x y')

# Expand the expression (2 * x + a)^(m + 3)
expr1 = (2 * x + a )**(m + 3)
print('Task 1')
print(expand(expr1))

# Factor the rational expression
expr2 = (a * x**2 + b * x + g) / ((x - m) * (2 * x - t - 1) * (x + 3))
print('\nTask 2')
print(factor(expr2))

# Substitute values into the expression and calculate its value
expr3 = expr2.subs([(x, sin(y)), (a, exp(x))])  # Substitute sin(y) for x and exp(x) for a
expr3 = expr3.subs([(x, 1), (y, pi)])  # Now substitute x = 1 and y = pi
print('\nTask 3')
print(expr3)

# Expand the polynomial expression
expr4 = (x-(n+2))*(x-a)*(x-(m+3))*(x-(g+1))
print('\nTask 4')
print(expand(expr4))

# Differentiate the expression 4^(cos(x+5))
expr5 = 4**cos(x+5)
print('\nTask 5')
print(diff(expr5))

# Integrate the expression (5**sqrt(x))/sqrt(x)
expr6 = (5**sqrt(x))/sqrt(x)
print('\nTask 6')
print(integrate(expr6, x))

# Compute the definite integral of a rational expression
expr7 = (a*x+b*x+x*sin(x)**2)/(x+g*cos(x)+3)
print('\nTask 7')
print(integrate(expr7, (x, m+1, n+6)))

# Compute the limit of the expression (5**x - 1)/sin(3*x) as x approaches 0
expr8 = (5**x - 1)/sin(3*x)
print('\nTask 8')
print(limit(expr8, x, 0))
