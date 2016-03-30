import math
import numpy as np
import matplotlib.pyplot as plt
import math
from collections import Counter
import scipy as sp
from matplotlib.pylab import hist, show

def congruencialMixto(a,b,m,x0,limite):
    i=0
    Xn=0.0
    Un=0.0
    generador=[]
    while i<limite:
        Xn = ((a*x0)+b)%m
        Un = Xn/float(m)
        generador.append(Un)
        x0=Xn
        i+=1
    return generador

def testKolmogorov(limite):
    # Teoretical CDF for Uniform distribution F(x)
    u = [1.0] * limite
    #print(u)

    # Gerate random numbers with Uniform distribution f(x)
    #np.random.seed(123456789)
    x=congruencialMixto(5,10,997,15,limite)
    # Plot empirical distribution f(x)
    count, bins, ignored = plt.hist(x, 25, normed=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()
    x1 = np.arange(1/(limite+0.0),1+1/(limite+0.0),1/(limite+0.0))
    y1 = np.cumsum(np.sort(u)/np.max(np.cumsum(u)))

    x2 = np.sort(x)
    y2 = np.cumsum(np.sort(x)/np.max(np.cumsum(x)))

    De=np.absolute(y2-y1)
    #print(D)
    print("De = ",np.max(De))
    if np.max(De)< (1.36/(limite**0.5)+0.0):
        print 'Hipotesis valida '
    else:
        print 'Hipotesis rechazada'

def testChicuadrado(limite,k):    
    vec=congruencialMixto(16645,13467,317,999,limite)
    ParE=0.0
    ParS=1.0/k
    aumento=1.0/k
    dat=[]
    sum=[]
    for i in range(len(vec)):
        for j in range(k):
            if vec[i]>ParE and vec[i]<=ParS:
                dat.append(ParE)
            ParE=ParS
            ParS+=aumento
        ParE=0.0
        ParS=aumento
    k=0.0
    while k<=1:
        sum.append(dat.count(k))
        print dat.count(k)
        k+=aumento
    ei=(limite+0.0)/(k+0.0)
    print len(sum)
    val=0.0
    for j in range(len(sum)):
        val+=((sum[j]-ei)**2)/ei
    print val