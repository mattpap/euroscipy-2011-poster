>>> var('x')
x
>>> sin(10).evalf(n=10)
-0.5440211109
>>> (sin(10)*x).evalf(n=10)
-0.5440211109*x
>>> integrate(sin(x), (x, 0, 2*pi))
0
>>> sin(x) == 1
False
>>> Eq(sin(x), 1)
sin(x) = 1
>>> solve(_, x)
[pi/2]
