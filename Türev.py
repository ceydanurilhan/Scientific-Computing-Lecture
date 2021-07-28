import math
def f(x):
    return (math.log(x))

h=0.1
n=10
turev=(f(n+h)-f(n))/h
ikinciturev = (f(n+2*h)-2*f(n+h)+f(n))/h**2

print(turev,ikinciturev)