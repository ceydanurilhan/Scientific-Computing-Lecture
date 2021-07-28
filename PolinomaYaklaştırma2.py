xi = [1,2,3,4,5,6,7]
yi = [0.5,2.5,2,4,3.5,6,5.5]
n = len(xi)

xi2,xi3,xiyi,xi4,xi2yi=0,0,0,0,0
for i in range(n):
    xiyi +=xi[i]*yi[i]
    xi2yi += xi[i]**2*yi[i]
    xi2 += xi[i]**2
    xi3 += xi[i] ** 3
    xi4 += xi[i] ** 4

print(n,sum(xi),xi2,sum(yi),xi3,xiyi,xi4,xi2yi)