
#Ex4

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def approx_sin(x, n):
    res = 0
    for i in range(0,n):
        res += ((-1)**(i))*(x**(2*i + 1))/factorial(2*i + 1)
    return res

def approx_cos(x, n):
    res = 0
    for i in range(0,n):
        res += ((-1)**(i))*(x**(2*i))/factorial(2*i)
    return res

def approx_sinh(x, n):
    res = 0
    for i in range(0,n):
        res += (x**(2*i + 1))/factorial(2*i + 1)
    return res

def approx_cosh(x, n):
    res = 0
    for i in range(0,n):
        res += (x**(2*i))/factorial(2*i)
    return res
