from pylab import *

def f(x):
    return x**2

def g(x):
    return sin(x-1)
    

x = linspace(-2,1,num=1000)
plot(x,f(x), 'b-')

x = linspace(1,3,num=1000)
plot(x,g(x), 'b-')

plot(1,0,'bo')
plot(1,1,'wo')
ylim(-1.5, 1.5)
xlim(0,3)

show()