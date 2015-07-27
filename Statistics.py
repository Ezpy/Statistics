# -*- coding: utf-8 -*-
# Statistics.py

import numpy as np
import pylab

def CoefficientD(a, b):
    #  coefficient of determination
    Saa = 0
    Sbb = 0
    Sab = 0
    
    a_avg = np.average(a)
    b_avg = np.average(b)
    
    if len(a) == len(b):
        for i in range(len(a)):
            Saa += np.power(a[i]-a_avg,2)
            Sbb += np.power(b[i]-b_avg,2)
            Sab += ( (a[i]-a_avg)*(b[i]-b_avg) )
        return np.power( Sab / np.sqrt( Saa * Sbb ), 2)
    else:
        raise Exception('Error: both list length must be equal')

def CoefficientG(a, b):
    #  coefficient graph
    Saa = 0
    Sab = 0
    
    a_avg = np.average(a)
    b_avg = np.average(b)
    
    if len(a) == len(b):
        for i in range(len(a)):
            Saa += np.power(a[i]-a_avg,2)
            Sab += ( (a[i]-a_avg)*(b[i]-b_avg) )
        slope = Sab / Saa
        yintercept = b_avg - a_avg * slope
        
        return (slope, yintercept)
    else:
        raise Exception('Error: both list length must be equal')

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = [2,4,1,7,6,11]
    
    
    print '------------------------------------'
    print 'Testing ..'
    print 'A:',a
    print 'B:',b
    
    
    print '------------------------------------'
    print 'Coefficient of Determination is %.2f' % CoefficientD(a,b)
    # easy solution with numpy library
    print 'Numpy library result is also %.2f' % np.power(np.corrcoef(a,b)[0][1],2)
    print '------------------------------------'
    test = CoefficientG(a,b)
    print ' * Graph equation'
    print 'y = (%.2f) * x + (%.2f)' % (test[0],test[1])
    print '------------------------------------'

    testa = []
    testb = []
    _min = min(a)
    
    while _min-0.1 <= max(a):
        testa.append(_min)
        testb.append(_min*test[0]+test[1])
        _min += 0.1
        
    for i in range(len(a)):
        pylab.scatter(a[i],b[i],color='blue')
    pylab.plot(testa,testb,color='red')
    
    