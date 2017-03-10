from numpy import *
from math import *
x0=3.7
e=1e-4
n=0
while (True):
    n+=1
    x=(8/5)*(log(x0)+1)
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))
print("Вектор невязки:{0}".format(x0-(8/5)*(log(x0)+1)))