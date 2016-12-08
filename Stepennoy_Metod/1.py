from numpy import *
inp = open('in.txt', 'r')
A = []
n = 5
eps = 10 ** (-15)
for line in inp:
    temp = [float(x) for x in line.split()]
    A.append(temp)
a = array(A)
print('A:\n {}'.format(a))
At = a.transpose()
a = dot(At, a)
print('A(new-A*AT):\n {}'.format(a))
yk = ones(5)
y = dot(a, yk)
l = y[0] / yk[0]
k = 1
while (True):
    yk = dot(a, y)
    lk = yk[0] / y[0]
    yk /= max(yk)
    if abs(lk - l) <= eps:
        break
    y = yk
    l = lk
    k += 1
print('lambdа: {}'.format(lk))
print('eps: {}'.format(eps))