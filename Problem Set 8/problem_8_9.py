from pylab import *

def f(x):
    return 2*x-3

x = linspace(0,5,num=1000)
plot(x,f(x))
xlabel('$x$')
ylabel('$y$')
grid('on')
show()
