from pylab import *

def f(x):
    return (x+2)*(x-3)*(x-5)

x = linspace(-3,7,num=1000)
plot(x,f(x), 'k-')

xlim(-3,7)
grid('on')

show()