>>> var('x')
x
>>> sin(10).evalf(n=10)
-0.5440211109
>>> integrate(sin(x), (x, 0, 2*pi))
0
>>> sin(x) == 1
False
>>> solve(Eq(sin(x), 1), x)
[pi/2]
>>> t = Symbol('t')
>>> factor(t**2 + 1, modulus=2)
(t + 1)**2
