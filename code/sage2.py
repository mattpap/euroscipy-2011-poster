sage: var('x')
x
sage: sin(10).n(digits=10)
-0.5440211109
sage: integrate(sin(x), x, 0, 2*pi)
0
sage: sin(x) == 1
sin(x) == 1
sage: solve(sin(x) == 1, x)
[x == 1/2*pi]
sage: K.<t> = GF(2)['t']
sage: factor(t**2 + 1)
(t + 1)^2
