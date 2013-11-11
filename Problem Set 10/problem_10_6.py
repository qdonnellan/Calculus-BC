from pylab import *

def f(x):
    return (x+4)*(x)*(x-4)

x = linspace(-3,7,num=1000)
plot(x,f(x), 'k-')
plot(2.3, f(2.3), 'ko')
plot(0,f(0), 'ko')
annotate('a', xy=(0.1, 1))
annotate('b', xy=(2.3, f(2.8)))

xlim(-3,4)
ylim(-50,50)
grid('on')

show()