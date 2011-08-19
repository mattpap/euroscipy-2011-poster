>>> from swiginac import symbol, sin
>>> x = symbol('x')
>>> sin(2*x).diff(x)
2*cos(2*x)
