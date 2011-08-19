>>> from sympy import var, sin
>>> var('x')
x
>>> sin(2*x).diff(x)
2*cos(2*x)
