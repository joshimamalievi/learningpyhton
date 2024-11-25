#lambda is a small anonymous function.

x = lambda a : a + 10

print(x(4))

y = lambda a, b, c: (a+b+c)//3

print(y(1, 2, 3))

#you can also use lambda in a function 

def multiplier(n):
    return lambda a: a*n
double = multiplier(2)
tripler = multiplier(3)
print(double(12), tripler(12))
