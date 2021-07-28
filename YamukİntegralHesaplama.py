xi = [-1.732,0,1.732]
yi = [-4.732,-3,-1,268]
n = len(xi)

deltax=xi[1]-xi[0]
altintegral,ustintegral,yamuk= 0,0,0

for i in range(n-1):
    altintegral += deltax * yi[i]
    ustintegral += deltax * yi[i+1]
    yamuk += deltax*(yi[i]+yi[i+1])/2
print(altintegral,ustintegral,yamuk)