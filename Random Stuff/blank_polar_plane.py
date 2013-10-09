from pylab import *

polar()
rgrids([1,2,3,4,5,6])
thetagrids( range(0,360,45), ('0','$\pi/4$', '$\pi/2$', '$3\pi/4$','$\pi$',
'$5\pi/4$', '$3\pi/2$', '$7\pi/4$') )
show()