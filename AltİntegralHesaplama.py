xi = [0,1,2,3,4,5]
yi = [2.1,7.7,13.6,27.2,40.9,61.1]
n = len(xi)

deltax=xi[1]-xi[0]
altintegral= 0

for i in range(n-1):
    altintegral += deltax * yi[i]
print(altintegral)