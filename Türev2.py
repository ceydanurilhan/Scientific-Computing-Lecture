#ileri sonlu farklar
def f(x):
    return (x**3-2*x**2+x)

h=0.0001
n=1
turev=(f(n+h)-f(n))/h
ikinciturev = (f(n+2*h)-2*f(n+h)+f(n))/h**2

print(turev,ikinciturev)

#geri  sonlu farklar
def f(x):
    return (x**3-2*x**2+x)

h=0.01
n=1
turev=(f(n)-f(n-h))/h
ikinciturev = (f(n)-2*f(n-h)+f(n-2*h))/h**2

print(turev,ikinciturev)

#merkezi farklar
def f(x):
    return (x**3-2*x**2+x)

h=0.01
n=1
turev=(f(n+h)-f(n-h))/2*h
ikinciturev = (f(n+h)-2*f(n)+f(n-h))/h**2

print(turev,ikinciturev)