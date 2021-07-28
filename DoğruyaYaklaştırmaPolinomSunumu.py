xi = [0,1,2,3,4,5]
yi = [2.1,7.7,13.6,27.2,40.9,61.1]
n = len(xi)

xiyi,xi2,standartsapma,ortalamahata = 0,0,0,0
for i in range(n):
    xiyi += xi[i]*yi[i]
    xi2 += xi[i]**2
    standartsapma += (yi[i]-sum(yi)/n)**2

a1 = (n*xiyi-sum(xi)*sum(yi))/(n*xi2-sum(xi)**2)
a0 = sum(yi)/n-a1*sum(xi)/n

standartsapma = (standartsapma/(n-1))**(1/2)

for i in range(n):
    y = a0+a1*xi[i]
    ortalamahata += yi[i]-y
ortalamahata = abs((ortalamahata/(n-2))**(1/2))

print(a0,a1)