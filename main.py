import math

def sinFunction(x): # This gets the values of the functions
    return math.sin(x)
def Multipli(x):
    return 1/3 * x ** 3
def sinFunctionTwo(x):
    return math.sin(x) + 1

def integral(f, a, b, n): # Integration function
    dx = (b - a)/n
    total = f(a) + f(b)
    middle = 0
    current = dx

    for x in range(1, n):
        middle += f(a + current)
        current += dx
    total += middle
    return round(total * (dx), 3)

n = 1
ans = 0
while (abs(ans - 1.994) > .001):
    n = n * 2
    ans = integral(sinFunction, 0, math.pi, n)
    print('n = %d ans = %.3f' % (n, ans))

print(f"f(x) = sin(x), from 0 to pi : {integral(sinFunction, 0, math.pi, 16)}") # integral function 1

n = 1
ans = 0
while (abs(ans - 21.253) > .01):
    n = n * 2
    ans = integral(Multipli, 1, 4, n)
    print('n = %d ans= %.3f' % (n, ans))

print(f"f(x) = 1/3 * x**3, from 1 to 4 : {integral(Multipli, 1, 4, 4096)}") # integral function 2

n = 1
ans = 0
while (abs(ans - 6.283) > .0001):
    n = n * 2
    ans = integral(sinFunctionTwo, 0, 2 * math.pi, n)
    print('n = %d ans = %.3f' % (n, ans))

print(f"f(x) = sin(x) + 1, from 0 to 2pi : {integral(sinFunctionTwo, 0, 2 * math.pi, 32768)}") # integral function 3