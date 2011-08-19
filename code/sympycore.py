>>> from sympycore import var, sin
>>> var('x')
Calculus('x')
>>> sin(2*x).diff(x)
Calculus('2*Cos(2*x)')
