# lambda: argument: expression

x = lambda a: a+10

print(x(5))

# multiple argument

x = lambda a,b: a*b

print(x(5,4))

# lambda inside function

def myfun(n):
    return lambda a: a*n 

product = myfun(3)

print(product(3))