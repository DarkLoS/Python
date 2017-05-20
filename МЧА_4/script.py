from functions import *
from textwrap import *
np.set_printoptions(precision=7)      #опции для вывода
np.set_printoptions(linewidth=500)
np.set_printoptions(suppress=True)
#np.set_printoptions(threshold=np.inf)


v = [1+0.1/3, 1.5+0.1/2, 2-0.1/3]          #точки
x = Symbol('x')
myf=lambdify(x, 1.7*e**(-x)+1-1.7*cos(x))
params = [0]*11
values = [0]*11
start = 1.0
h = 0.1
for i in range (11):
    params[i]=start
    values[i]=myf(start)
    start+=h
print("Точки:")
print(params)
print("Значения в точках:")
print(values)
print('---------------------------------------------------------------------------------------------------------------')
print('А это Лагранж\n\n')
f = 1
for e in params:
    f*=(x-e)
lPl=0
for i in range(len(params)):
    q, r = div(f, x-params[i], x)
    g = lambdify(x, q)
    lPl+=q*values[i]/g(params[i])
print('Сам полином:\n')
print(fill(str(simplify(lPl)), 120)+'\n')
l = lambdify(x, lPl)
for i in range(len(v)):
    print("Корень номер {0}, приближение многочленом Лагранжа  {1} и его реальное значение {2}".format(i,l(v[i]),myf(v[i])))

print('---------------------------------------------------------------------------------------------------------------')
print('А это Ньютон\n\n')
interpolant = rr(params,values)
f = 1
g = 0
for i in range(len(params)):
	g+=interpolant[i]*f
	f*=(x-params[i])
print('Сам полином:\n')
print(fill(str(simplify(g)), 120)+'\n')
l = lambdify(x, g)
for i in range(len(v)):
    print("Корень номер {0}, приближение многочленом Ньютона {1} и его реальное значение {2}".format(i,l(v[i]),myf(v[i])))

print('---------------------------------------------------------------------------------------------------------------')
print('А это Ньютон с равностоящими узлами\n\n')
f = 1
g = 0
for i in range(len(params)):
	g+=delta(i,values)*f
	f*=(x-params[i])/(i+1)/h
l = lambdify(x, g)
print('Сам полином:\n')
print(fill(str(simplify(g)), 120)+'\n')
for i in range(len(v)):
    print("Корень номер {0}, приближение многочленом Ньютона {1} и его реальное значение {2}".format(i,l(v[i]),myf(v[i])))

print('---------------------------------------------------------------------------------------------------------------')
print('А это Эрмит\n\n')
k = 2                                              #это кол-во производных
fg=[0]*(len(params)*(k+1))
fr=[0]*(len(values)*(k+1))
for i in range(len(fg)) :
	fg[i]=params[i//(k+1)]
	fr[i]=values[i//(k+1)]
a = []
for r in range(k):
	a.append([])
	for c in range(len(params)):
		phi = lambdify((x), diff(eval('1.7*exp(-x)+1-1.7*cos(x)'), x, r+1), 'numpy')
		a[r].append((phi(params[c])))
print('Производные в точках\n')
print(fill(str(a), 120)+'\n')
interpolant = rr_ermit(fg,fr,a,(k+1))
f = 1
g = 0
for i in range(len(fg)):
	g+=interpolant[i]*f
	f*=(x-fg[i])
print('Сам полином:\n')
print(fill(str(simplify(g)), 120)+'\n')
l = lambdify(x, g)
for i in range(len(v)):
    print("Корень номер {0}, приближение многочленом Эрмита {1} и его реальное значение {2}".format(i,l(v[i]),myf(v[i])))