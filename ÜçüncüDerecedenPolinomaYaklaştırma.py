xi = [0,1,2,3,4,5]
yi = [2.1,7.7,13.6,27.2,40.9,61.1]
n = len(xi)

xi2, xi3, xiyi, xi4, xi2yi, xi5, xi3yi, xi6 = 0,0,0,0,0,0,0,0
for i in range(n):
    xi2 += xi[i]**2
    xi3 += xi[i]**3
    xi4 += xi[i]**4
    xi5 += xi[i]**5
    xi6 += xi[i]**6
    xiyi += xi[i]*yi[i]
    xi2yi += xi[i]**2*yi[i]
    xi3yi += xi[i]**3*yi[i]

print("n:",n, "xi:",sum(xi), "xi2:",xi2, "xi3",xi3, "yi:",sum(yi), "xi4:",xi4, "xiyi:",xiyi, "xi5:",xi5, "xi2yi:",xi2yi, "xi6:",xi6,"xi3yi:",xi3yi)