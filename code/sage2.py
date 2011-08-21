sage: var('x')
x
sage: sin(10).n(digits=10)
-0.5440211109
sage: (sin(10)*x).n(digits=10)
...
TypeError: ...
sage: integrate(sin(x), x, 0, 2*pi)
0
sage: sin(x) == 1
sin(x) == 1
sage: solve(_, x)
[x == 1/2*pi]

