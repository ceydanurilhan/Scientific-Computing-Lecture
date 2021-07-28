'''
from math import factorial
e=1

for n in range(1,30):
    e+=1/factorial(n)
    print(n,e)
'''
from math import factorial
from decimal import *
getcontext().prec=42
e=1

for n in range(1,70):
    e+=Decimal(1/factorial(n))
print(n,e)
