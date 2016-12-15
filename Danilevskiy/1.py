from numpy import *
from numpy.linalg import *
from sympy.solvers import solve
from sympy import Symbol
inp = open('in.txt', 'r')
A = []
n = 5
for line in inp:
    temp = [float(x) for x in line.split()]
    A.append(temp)
a = array(A)
At = a.transpose()  # находим Аt
a = dot(At, a)  # перемножаем А на Аt, теперь А - симметрическая
f = a
print('A:\n {}'.format(a))
s = identity(n)
for i in range(n - 1):
    m = identity(n)
    m[n - 2 - i][:] = f[n - 1 - i][:]
    f = dot(m, f)
    f = dot(f, inv(m))
    s = dot(s, inv(m))
print('F:\n {}'.format(f))
p = f[0][:]
print('p:\n {}'.format(p))
x = Symbol('x')
Lambda = solve(x ** 5 - p[0] * x ** 4 - p[1] * x ** 3- p[2] * x ** 2- p[3] * x - p[4],x)
print('lambda:\n {}'.format(Lambda))
l = Lambda[0]
print(' l{0}:  {1}'.format(0,l))
y = [l ** i for i in range(n - 1, -1, -1)]
print('     x{0}: {1}'.format(0,dot(s, y)))
print("Остальные собственные вектора будут комплексными")
