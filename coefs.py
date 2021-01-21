import sympy as sp
from sympy import degree as dg
import numpy as np
import IntCuad
import math as mt
import fls
import time as tm
import prnt
import os
#import smpx
#ex=6;ey=6
#sxiyj: i<=4;j<=2
for i in range(3):
    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
    globals()['y%i'%(i+1)]=sp.symbols('y%i'%(i+1))
#for i in range(ex+1):
#    for j in range(ey+1):
#        if(i==0):
#            if(j==1):
#                globals()['sy']=sp.symbols('sy')#y1+y2+y3
#            elif(j>1):
#                globals()['sy%i'%j]=sp.symbols('sy%i'%j)#y1**j+y2**j+y3**j
#        elif(i==1):
#            if(j==0):
#                globals()['sx']=sp.symbols('sx')#x1+x2+x3
#            elif(j==1):
#                globals()['sxy']=sp.symbols('sxy')#x1*y1+x2*y2+x3*y3
#            else:
#                globals()['sxy%i'%j]=sp.symbols('sxy%i'%j)#x1*y1**j+x2*y2**j+x3*y3**j   
#        else:
#            if(j==0):
#                globals()['sx%i'%i]=sp.symbols('sx%i'%i)#x1**i+x2**i+x3**i
#            elif(j==1):
#                globals()['sx%iy'%i]=sp.symbols('sx%iy'%i)#x1**i*y1+x2**i*y2+x3**i*y3
#            else:
#                globals()['sx%iy%i'%(i,j)]=sp.symbols('sx%iy%i'%(i,j))#x1**i*y1**j+x2**i*y2**j+x3**i*y3**j

def smdf(ex,ey):
    for i in range(ex+1):
        for j in range(ey+1):
            if(i==0):
                if(j==1):
                    globals()['sy']=sp.symbols('sy')#y1+y2+y3
                elif(j>1):
                    globals()['sy%i'%j]=sp.symbols('sy%i'%j)#y1**j+y2**j+y3**j
            elif(i==1):
                if(j==0):
                    globals()['sx']=sp.symbols('sx')#x1+x2+x3
                elif(j==1):
                    globals()['sxy']=sp.symbols('sxy')#x1*y1+x2*y2+x3*y3
                else:
                    globals()['sxy%i'%j]=sp.symbols('sxy%i'%j)#x1*y1**j+x2*y2**j+x3*y3**j   
            else:
                if(j==0):
                    globals()['sx%i'%i]=sp.symbols('sx%i'%i)#x1**i+x2**i+x3**i
                elif(j==1):
                    globals()['sx%iy'%i]=sp.symbols('sx%iy'%i)#x1**i*y1+x2**i*y2+x3**i*y3
                else:
                    globals()['sx%iy%i'%(i,j)]=sp.symbols('sx%iy%i'%(i,j))#x1**i*y1**j+x2**i*y2**j+x3**i*y3**j
    return ex

def dfvr(ex,ey):
    for i in range(ex+1):
        for j in range(ey+1):
            if(i==0):
                if(j==1):
                    globals()['sy']=y1+y2+y3
                elif(j>1):
                    globals()['sy%i'%j]=y1**j+y2**j+y3**j
            elif(i==1):
                if(j==0):
                    globals()['sx']=x1+x2+x3
                elif(j==1):
                    globals()['sxy']=x1*y1+x2*y2+x3*y3
                else:
                    globals()['sxy%i'%j]=x1*y1**j+x2*y2**j+x3*y3**j   
            else:
                if(j==0):
                    globals()['sx%i'%i]=x1**i+x2**i+x3**i
                elif(j==1):
                    globals()['sx%iy'%i]=x1**i*y1+x2**i*y2+x3**i*y3
                else:
                    globals()['sx%iy%i'%(i,j)]=x1**i*y1**j+x2**i*y2**j+x3**i*y3**j

#def frm():
    #smdf(i,j)
    #fml=(15*x1**4*y1**2 + 5*x1**4*y1*y2 + 5*x1**4*y1*y3 + x1**4*y2**2 + x1**4*y2*y3 + x1**4*y3**2 + 10*x1**3*x2*y1**2 + 8*x1**3*x2*y1*y2 + 4*x1**3*x2*y1*y3 + 3*x1**3*x2*y2**2 + 2*x1**3*x2*y2*y3 + x1**3*x2*y3**2 + 10*x1**3*x3*y1**2 + 4*x1**3*x3*y1*y2 + 8*x1**3*x3*y1*y3 + x1**3*x3*y2**2 + 2*x1**3*x3*y2*y3 + 3*x1**3*x3*y3**2 + 6*x1**2*x2**2*y1**2 + 9*x1**2*x2**2*y1*y2 + 3*x1**2*x2**2*y1*y3 + 6*x1**2*x2**2*y2**2 + 3*x1**2*x2**2*y2*y3 + x1**2*x2**2*y3**2 + 6*x1**2*x2*x3*y1**2 + 6*x1**2*x2*x3*y1*y2 + 6*x1**2*x2*x3*y1*y3 + 3*x1**2*x2*x3*y2**2 + 4*x1**2*x2*x3*y2*y3 + 3*x1**2*x2*x3*y3**2 + 6*x1**2*x3**2*y1**2 + 3*x1**2*x3**2*y1*y2 + 9*x1**2*x3**2*y1*y3 + x1**2*x3**2*y2**2 + 3*x1**2*x3**2*y2*y3 + 6*x1**2*x3**2*y3**2 + 3*x1*x2**3*y1**2 + 8*x1*x2**3*y1*y2 + 2*x1*x2**3*y1*y3 + 10*x1*x2**3*y2**2 + 4*x1*x2**3*y2*y3 + x1*x2**3*y3**2 + 3*x1*x2**2*x3*y1**2 + 6*x1*x2**2*x3*y1*y2 + 4*x1*x2**2*x3*y1*y3 + 6*x1*x2**2*x3*y2**2 + 6*x1*x2**2*x3*y2*y3 + 3*x1*x2**2*x3*y3**2 + 3*x1*x2*x3**2*y1**2 + 4*x1*x2*x3**2*y1*y2 + 6*x1*x2*x3**2*y1*y3 + 3*x1*x2*x3**2*y2**2 + 6*x1*x2*x3**2*y2*y3 + 6*x1*x2*x3**2*y3**2 + 3*x1*x3**3*y1**2 + 2*x1*x3**3*y1*y2 + 8*x1*x3**3*y1*y3 + x1*x3**3*y2**2 + 4*x1*x3**3*y2*y3 + 10*x1*x3**3*y3**2 + x2**4*y1**2 + 5*x2**4*y1*y2 + x2**4*y1*y3 + 15*x2**4*y2**2 + 5*x2**4*y2*y3 + x2**4*y3**2 + x2**3*x3*y1**2 + 4*x2**3*x3*y1*y2 + 2*x2**3*x3*y1*y3 + 10*x2**3*x3*y2**2 + 8*x2**3*x3*y2*y3 + 3*x2**3*x3*y3**2 + x2**2*x3**2*y1**2 + 3*x2**2*x3**2*y1*y2 + 3*x2**2*x3**2*y1*y3 + 6*x2**2*x3**2*y2**2 + 9*x2**2*x3**2*y2*y3 + 6*x2**2*x3**2*y3**2 + x2*x3**3*y1**2 + 2*x2*x3**3*y1*y2 + 4*x2*x3**3*y1*y3 + 3*x2*x3**3*y2**2 + 8*x2*x3**3*y2*y3 + 10*x2*x3**3*y3**2 + x3**4*y1**2 + x3**4*y1*y2 + 5*x3**4*y1*y3 + x3**4*y2**2 + 5*x3**4*y2*y3 + 15*x3**4*y3**2)/420
    #fml2=x1**8 + 8*x1**7*x2 + 8*x1**7*x3 + 28*x1**6*x2**2 + 56*x1**6*x2*x3 + 28*x1**6*x3**2 + 56*x1**5*x2**3 + 168*x1**5*x2**2*x3 + 168*x1**5*x2*x3**2 + 56*x1**5*x3**3 + 70*x1**4*x2**4 + 280*x1**4*x2**3*x3 + 420*x1**4*x2**2*x3**2 + 280*x1**4*x2*x3**3 + 70*x1**4*x3**4 + 56*x1**3*x2**5 + 280*x1**3*x2**4*x3 + 560*x1**3*x2**3*x3**2 + 560*x1**3*x2**2*x3**3 + 280*x1**3*x2*x3**4 + 56*x1**3*x3**5 + 28*x1**2*x2**6 + 168*x1**2*x2**5*x3 + 420*x1**2*x2**4*x3**2 + 560*x1**2*x2**3*x3**3 + 420*x1**2*x2**2*x3**4 + 168*x1**2*x2*x3**5 + 28*x1**2*x3**6 + 8*x1*x2**7 + 56*x1*x2**6*x3 + 168*x1*x2**5*x3**2 + 280*x1*x2**4*x3**3 + 280*x1*x2**3*x3**4 + 168*x1*x2**2*x3**5 + 56*x1*x2*x3**6 + 8*x1*x3**7 + x2**8 + 8*x2**7*x3 + 28*x2**6*x3**2 + 56*x2**5*x3**3 + 70*x2**4*x3**4 + 56*x2**3*x3**5 + 28*x2**2*x3**6 + 8*x2*x3**7 + x3**8
#fml2=6*x1**2*y1**2 + 3*x1**2*y1*y2 + 3*x1**2*y1*y3 + x1**2*y2**2 + x1**2*y2*y3 + x1**2*y3**2 + 3*x1*x2*y1**2 + 4*x1*x2*y1*y2 + 2*x1*x2*y1*y3 + 3*x1*x2*y2**2 + 2*x1*x2*y2*y3 + x1*x2*y3**2 + 3*x1*x3*y1**2 + 2*x1*x3*y1*y2 + 4*x1*x3*y1*y3 + x1*x3*y2**2 + 2*x1*x3*y2*y3 + 3*x1*x3*y3**2 + x2**2*y1**2 + 3*x2**2*y1*y2 + x2**2*y1*y3 + 6*x2**2*y2**2 + 3*x2**2*y2*y3 + x2**2*y3**2 + x2*x3*y1**2 + 2*x2*x3*y1*y2 + 2*x2*x3*y1*y3 + 3*x2*x3*y2**2 + 4*x2*x3*y2*y3 + 3*x2*x3*y3**2 + x3**2*y1**2 + x3**2*y1*y2 + 3*x3**2*y1*y3 + x3**2*y2**2 + 3*x3**2*y2*y3 + 6*x3**2*y3**2
    #fml2=x1**3*y1**3 + 3*x1**3*y1**2*y2 + 3*x1**3*y1**2*y3 + 3*x1**3*y1*y2**2 + 6*x1**3*y1*y2*y3 + 3*x1**3*y1*y3**2 + x1**3*y2**3 + 3*x1**3*y2**2*y3 + 3*x1**3*y2*y3**2 + x1**3*y3**3 + 3*x1**2*x2*y1**3 + 9*x1**2*x2*y1**2*y2 + 9*x1**2*x2*y1**2*y3 + 9*x1**2*x2*y1*y2**2 + 18*x1**2*x2*y1*y2*y3 + 9*x1**2*x2*y1*y3**2 + 3*x1**2*x2*y2**3 + 9*x1**2*x2*y2**2*y3 + 9*x1**2*x2*y2*y3**2 + 3*x1**2*x2*y3**3 + 3*x1**2*x3*y1**3 + 9*x1**2*x3*y1**2*y2 + 9*x1**2*x3*y1**2*y3 + 9*x1**2*x3*y1*y2**2 + 18*x1**2*x3*y1*y2*y3 + 9*x1**2*x3*y1*y3**2 + 3*x1**2*x3*y2**3 + 9*x1**2*x3*y2**2*y3 + 9*x1**2*x3*y2*y3**2 + 3*x1**2*x3*y3**3 + 3*x1*x2**2*y1**3 + 9*x1*x2**2*y1**2*y2 + 9*x1*x2**2*y1**2*y3 + 9*x1*x2**2*y1*y2**2 + 18*x1*x2**2*y1*y2*y3 + 9*x1*x2**2*y1*y3**2 + 3*x1*x2**2*y2**3 + 9*x1*x2**2*y2**2*y3 + 9*x1*x2**2*y2*y3**2 + 3*x1*x2**2*y3**3 + 6*x1*x2*x3*y1**3 + 18*x1*x2*x3*y1**2*y2 + 18*x1*x2*x3*y1**2*y3 + 18*x1*x2*x3*y1*y2**2 + 36*x1*x2*x3*y1*y2*y3 + 18*x1*x2*x3*y1*y3**2 + 6*x1*x2*x3*y2**3 + 18*x1*x2*x3*y2**2*y3 + 18*x1*x2*x3*y2*y3**2 + 6*x1*x2*x3*y3**3 + 3*x1*x3**2*y1**3 + 9*x1*x3**2*y1**2*y2 + 9*x1*x3**2*y1**2*y3 + 9*x1*x3**2*y1*y2**2 + 18*x1*x3**2*y1*y2*y3 + 9*x1*x3**2*y1*y3**2 + 3*x1*x3**2*y2**3 + 9*x1*x3**2*y2**2*y3 + 9*x1*x3**2*y2*y3**2 + 3*x1*x3**2*y3**3 + x2**3*y1**3 + 3*x2**3*y1**2*y2 + 3*x2**3*y1**2*y3 + 3*x2**3*y1*y2**2 + 6*x2**3*y1*y2*y3 + 3*x2**3*y1*y3**2 + x2**3*y2**3 + 3*x2**3*y2**2*y3 + 3*x2**3*y2*y3**2 + x2**3*y3**3 + 3*x2**2*x3*y1**3 + 9*x2**2*x3*y1**2*y2 + 9*x2**2*x3*y1**2*y3 + 9*x2**2*x3*y1*y2**2 + 18*x2**2*x3*y1*y2*y3 + 9*x2**2*x3*y1*y3**2 + 3*x2**2*x3*y2**3 + 9*x2**2*x3*y2**2*y3 + 9*x2**2*x3*y2*y3**2 + 3*x2**2*x3*y3**3 + 3*x2*x3**2*y1**3 + 9*x2*x3**2*y1**2*y2 + 9*x2*x3**2*y1**2*y3 + 9*x2*x3**2*y1*y2**2 + 18*x2*x3**2*y1*y2*y3 + 9*x2*x3**2*y1*y3**2 + 3*x2*x3**2*y2**3 + 9*x2*x3**2*y2**2*y3 + 9*x2*x3**2*y2*y3**2 + 3*x2*x3**2*y3**3 + x3**3*y1**3 + 3*x3**3*y1**2*y2 + 3*x3**3*y1**2*y3 + 3*x3**3*y1*y2**2 + 6*x3**3*y1*y2*y3 + 3*x3**3*y1*y3**2 + x3**3*y2**3 + 3*x3**3*y2**2*y3 + 3*x3**3*y2*y3**2 + x3**3*y3**3
    #fml2=x1**4*y1**4 + 4*x1**4*y1**3*y2 + 4*x1**4*y1**3*y3 + 6*x1**4*y1**2*y2**2 + 12*x1**4*y1**2*y2*y3 + 6*x1**4*y1**2*y3**2 + 4*x1**4*y1*y2**3 + 12*x1**4*y1*y2**2*y3 + 12*x1**4*y1*y2*y3**2 + 4*x1**4*y1*y3**3 + x1**4*y2**4 + 4*x1**4*y2**3*y3 + 6*x1**4*y2**2*y3**2 + 4*x1**4*y2*y3**3 + x1**4*y3**4 + 4*x1**3*x2*y1**4 + 16*x1**3*x2*y1**3*y2 + 16*x1**3*x2*y1**3*y3 + 24*x1**3*x2*y1**2*y2**2 + 48*x1**3*x2*y1**2*y2*y3 + 24*x1**3*x2*y1**2*y3**2 + 16*x1**3*x2*y1*y2**3 + 48*x1**3*x2*y1*y2**2*y3 + 48*x1**3*x2*y1*y2*y3**2 + 16*x1**3*x2*y1*y3**3 + 4*x1**3*x2*y2**4 + 16*x1**3*x2*y2**3*y3 + 24*x1**3*x2*y2**2*y3**2 + 16*x1**3*x2*y2*y3**3 + 4*x1**3*x2*y3**4 + 4*x1**3*x3*y1**4 + 16*x1**3*x3*y1**3*y2 + 16*x1**3*x3*y1**3*y3 + 24*x1**3*x3*y1**2*y2**2 + 48*x1**3*x3*y1**2*y2*y3 + 24*x1**3*x3*y1**2*y3**2 + 16*x1**3*x3*y1*y2**3 + 48*x1**3*x3*y1*y2**2*y3 + 48*x1**3*x3*y1*y2*y3**2 + 16*x1**3*x3*y1*y3**3 + 4*x1**3*x3*y2**4 + 16*x1**3*x3*y2**3*y3 + 24*x1**3*x3*y2**2*y3**2 + 16*x1**3*x3*y2*y3**3 + 4*x1**3*x3*y3**4 + 6*x1**2*x2**2*y1**4 + 24*x1**2*x2**2*y1**3*y2 + 24*x1**2*x2**2*y1**3*y3 + 36*x1**2*x2**2*y1**2*y2**2 + 72*x1**2*x2**2*y1**2*y2*y3 + 36*x1**2*x2**2*y1**2*y3**2 + 24*x1**2*x2**2*y1*y2**3 + 72*x1**2*x2**2*y1*y2**2*y3 + 72*x1**2*x2**2*y1*y2*y3**2 + 24*x1**2*x2**2*y1*y3**3 + 6*x1**2*x2**2*y2**4 + 24*x1**2*x2**2*y2**3*y3 + 36*x1**2*x2**2*y2**2*y3**2 + 24*x1**2*x2**2*y2*y3**3 + 6*x1**2*x2**2*y3**4 + 12*x1**2*x2*x3*y1**4 + 48*x1**2*x2*x3*y1**3*y2 + 48*x1**2*x2*x3*y1**3*y3 + 72*x1**2*x2*x3*y1**2*y2**2 + 144*x1**2*x2*x3*y1**2*y2*y3 + 72*x1**2*x2*x3*y1**2*y3**2 + 48*x1**2*x2*x3*y1*y2**3 + 144*x1**2*x2*x3*y1*y2**2*y3 + 144*x1**2*x2*x3*y1*y2*y3**2 + 48*x1**2*x2*x3*y1*y3**3 + 12*x1**2*x2*x3*y2**4 + 48*x1**2*x2*x3*y2**3*y3 + 72*x1**2*x2*x3*y2**2*y3**2 + 48*x1**2*x2*x3*y2*y3**3 + 12*x1**2*x2*x3*y3**4 + 6*x1**2*x3**2*y1**4 + 24*x1**2*x3**2*y1**3*y2 + 24*x1**2*x3**2*y1**3*y3 + 36*x1**2*x3**2*y1**2*y2**2 + 72*x1**2*x3**2*y1**2*y2*y3 + 36*x1**2*x3**2*y1**2*y3**2 + 24*x1**2*x3**2*y1*y2**3 + 72*x1**2*x3**2*y1*y2**2*y3 + 72*x1**2*x3**2*y1*y2*y3**2 + 24*x1**2*x3**2*y1*y3**3 + 6*x1**2*x3**2*y2**4 + 24*x1**2*x3**2*y2**3*y3 + 36*x1**2*x3**2*y2**2*y3**2 + 24*x1**2*x3**2*y2*y3**3 + 6*x1**2*x3**2*y3**4 + 4*x1*x2**3*y1**4 + 16*x1*x2**3*y1**3*y2 + 16*x1*x2**3*y1**3*y3 + 24*x1*x2**3*y1**2*y2**2 + 48*x1*x2**3*y1**2*y2*y3 + 24*x1*x2**3*y1**2*y3**2 + 16*x1*x2**3*y1*y2**3 + 48*x1*x2**3*y1*y2**2*y3 + 48*x1*x2**3*y1*y2*y3**2 + 16*x1*x2**3*y1*y3**3 + 4*x1*x2**3*y2**4 + 16*x1*x2**3*y2**3*y3 + 24*x1*x2**3*y2**2*y3**2 + 16*x1*x2**3*y2*y3**3 + 4*x1*x2**3*y3**4 + 12*x1*x2**2*x3*y1**4 + 48*x1*x2**2*x3*y1**3*y2 + 48*x1*x2**2*x3*y1**3*y3 + 72*x1*x2**2*x3*y1**2*y2**2 + 144*x1*x2**2*x3*y1**2*y2*y3 + 72*x1*x2**2*x3*y1**2*y3**2 + 48*x1*x2**2*x3*y1*y2**3 + 144*x1*x2**2*x3*y1*y2**2*y3 + 144*x1*x2**2*x3*y1*y2*y3**2 + 48*x1*x2**2*x3*y1*y3**3 + 12*x1*x2**2*x3*y2**4 + 48*x1*x2**2*x3*y2**3*y3 + 72*x1*x2**2*x3*y2**2*y3**2 + 48*x1*x2**2*x3*y2*y3**3 + 12*x1*x2**2*x3*y3**4 + 12*x1*x2*x3**2*y1**4 + 48*x1*x2*x3**2*y1**3*y2 + 48*x1*x2*x3**2*y1**3*y3 + 72*x1*x2*x3**2*y1**2*y2**2 + 144*x1*x2*x3**2*y1**2*y2*y3 + 72*x1*x2*x3**2*y1**2*y3**2 + 48*x1*x2*x3**2*y1*y2**3 + 144*x1*x2*x3**2*y1*y2**2*y3 + 144*x1*x2*x3**2*y1*y2*y3**2 + 48*x1*x2*x3**2*y1*y3**3 + 12*x1*x2*x3**2*y2**4 + 48*x1*x2*x3**2*y2**3*y3 + 72*x1*x2*x3**2*y2**2*y3**2 + 48*x1*x2*x3**2*y2*y3**3 + 12*x1*x2*x3**2*y3**4 + 4*x1*x3**3*y1**4 + 16*x1*x3**3*y1**3*y2 + 16*x1*x3**3*y1**3*y3 + 24*x1*x3**3*y1**2*y2**2 + 48*x1*x3**3*y1**2*y2*y3 + 24*x1*x3**3*y1**2*y3**2 + 16*x1*x3**3*y1*y2**3 + 48*x1*x3**3*y1*y2**2*y3 + 48*x1*x3**3*y1*y2*y3**2 + 16*x1*x3**3*y1*y3**3 + 4*x1*x3**3*y2**4 + 16*x1*x3**3*y2**3*y3 + 24*x1*x3**3*y2**2*y3**2 + 16*x1*x3**3*y2*y3**3 + 4*x1*x3**3*y3**4 + x2**4*y1**4 + 4*x2**4*y1**3*y2 + 4*x2**4*y1**3*y3 + 6*x2**4*y1**2*y2**2 + 12*x2**4*y1**2*y2*y3 + 6*x2**4*y1**2*y3**2 + 4*x2**4*y1*y2**3 + 12*x2**4*y1*y2**2*y3 + 12*x2**4*y1*y2*y3**2 + 4*x2**4*y1*y3**3 + x2**4*y2**4 + 4*x2**4*y2**3*y3 + 6*x2**4*y2**2*y3**2 + 4*x2**4*y2*y3**3 + x2**4*y3**4 + 4*x2**3*x3*y1**4 + 16*x2**3*x3*y1**3*y2 + 16*x2**3*x3*y1**3*y3 + 24*x2**3*x3*y1**2*y2**2 + 48*x2**3*x3*y1**2*y2*y3 + 24*x2**3*x3*y1**2*y3**2 + 16*x2**3*x3*y1*y2**3 + 48*x2**3*x3*y1*y2**2*y3 + 48*x2**3*x3*y1*y2*y3**2 + 16*x2**3*x3*y1*y3**3 + 4*x2**3*x3*y2**4 + 16*x2**3*x3*y2**3*y3 + 24*x2**3*x3*y2**2*y3**2 + 16*x2**3*x3*y2*y3**3 + 4*x2**3*x3*y3**4 + 6*x2**2*x3**2*y1**4 + 24*x2**2*x3**2*y1**3*y2 + 24*x2**2*x3**2*y1**3*y3 + 36*x2**2*x3**2*y1**2*y2**2 + 72*x2**2*x3**2*y1**2*y2*y3 + 36*x2**2*x3**2*y1**2*y3**2 + 24*x2**2*x3**2*y1*y2**3 + 72*x2**2*x3**2*y1*y2**2*y3 + 72*x2**2*x3**2*y1*y2*y3**2 + 24*x2**2*x3**2*y1*y3**3 + 6*x2**2*x3**2*y2**4 + 24*x2**2*x3**2*y2**3*y3 + 36*x2**2*x3**2*y2**2*y3**2 + 24*x2**2*x3**2*y2*y3**3 + 6*x2**2*x3**2*y3**4 + 4*x2*x3**3*y1**4 + 16*x2*x3**3*y1**3*y2 + 16*x2*x3**3*y1**3*y3 + 24*x2*x3**3*y1**2*y2**2 + 48*x2*x3**3*y1**2*y2*y3 + 24*x2*x3**3*y1**2*y3**2 + 16*x2*x3**3*y1*y2**3 + 48*x2*x3**3*y1*y2**2*y3 + 48*x2*x3**3*y1*y2*y3**2 + 16*x2*x3**3*y1*y3**3 + 4*x2*x3**3*y2**4 + 16*x2*x3**3*y2**3*y3 + 24*x2*x3**3*y2**2*y3**2 + 16*x2*x3**3*y2*y3**3 + 4*x2*x3**3*y3**4 + x3**4*y1**4 + 4*x3**4*y1**3*y2 + 4*x3**4*y1**3*y3 + 6*x3**4*y1**2*y2**2 + 12*x3**4*y1**2*y2*y3 + 6*x3**4*y1**2*y3**2 + 4*x3**4*y1*y2**3 + 12*x3**4*y1*y2**2*y3 + 12*x3**4*y1*y2*y3**2 + 4*x3**4*y1*y3**3 + x3**4*y2**4 + 4*x3**4*y2**3*y3 + 6*x3**4*y2**2*y3**2 + 4*x3**4*y2*y3**3 + x3**4*y3**4
    #cf=fml.subs({x1:1,x2:0,x3:0,y1:0,y2:0,y3:1})
    #fml*=cf
    #formula=15*x1**4*y1**2 + 5*x1**4*y1*y2 + 5*x1**4*y1*y3 + x1**4*y2**2 + x1**4*y2*y3 + x1**4*y3**2 + 10*x1**3*x2*y1**2 + 8*x1**3*x2*y1*y2 + 4*x1**3*x2*y1*y3 + 3*x1**3*x2*y2**2 + 2*x1**3*x2*y2*y3 + x1**3*x2*y3**2 + 10*x1**3*x3*y1**2 + 4*x1**3*x3*y1*y2 + 8*x1**3*x3*y1*y3 + x1**3*x3*y2**2 + 2*x1**3*x3*y2*y3 + 3*x1**3*x3*y3**2 + 6*x1**2*x2**2*y1**2 + 9*x1**2*x2**2*y1*y2 + 3*x1**2*x2**2*y1*y3 + 6*x1**2*x2**2*y2**2 + 3*x1**2*x2**2*y2*y3 + x1**2*x2**2*y3**2 + 6*x1**2*x2*x3*y1**2 + 6*x1**2*x2*x3*y1*y2 + 6*x1**2*x2*x3*y1*y3 + 3*x1**2*x2*x3*y2**2 + 4*x1**2*x2*x3*y2*y3 + 3*x1**2*x2*x3*y3**2 + 6*x1**2*x3**2*y1**2 + 3*x1**2*x3**2*y1*y2 + 9*x1**2*x3**2*y1*y3 + x1**2*x3**2*y2**2 + 3*x1**2*x3**2*y2*y3 + 6*x1**2*x3**2*y3**2 + 3*x1*x2**3*y1**2 + 8*x1*x2**3*y1*y2 + 2*x1*x2**3*y1*y3 + 10*x1*x2**3*y2**2 + 4*x1*x2**3*y2*y3 + x1*x2**3*y3**2 + 3*x1*x2**2*x3*y1**2 + 6*x1*x2**2*x3*y1*y2 + 4*x1*x2**2*x3*y1*y3 + 6*x1*x2**2*x3*y2**2 + 6*x1*x2**2*x3*y2*y3 + 3*x1*x2**2*x3*y3**2 + 3*x1*x2*x3**2*y1**2 + 4*x1*x2*x3**2*y1*y2 + 6*x1*x2*x3**2*y1*y3 + 3*x1*x2*x3**2*y2**2 + 6*x1*x2*x3**2*y2*y3 + 6*x1*x2*x3**2*y3**2 + 3*x1*x3**3*y1**2 + 2*x1*x3**3*y1*y2 + 8*x1*x3**3*y1*y3 + x1*x3**3*y2**2 + 4*x1*x3**3*y2*y3 + 10*x1*x3**3*y3**2 + x2**4*y1**2 + 5*x2**4*y1*y2 + x2**4*y1*y3 + 15*x2**4*y2**2 + 5*x2**4*y2*y3 + x2**4*y3**2 + x2**3*x3*y1**2 + 4*x2**3*x3*y1*y2 + 2*x2**3*x3*y1*y3 + 10*x2**3*x3*y2**2 + 8*x2**3*x3*y2*y3 + 3*x2**3*x3*y3**2 + x2**2*x3**2*y1**2 + 3*x2**2*x3**2*y1*y2 + 3*x2**2*x3**2*y1*y3 + 6*x2**2*x3**2*y2**2 + 9*x2**2*x3**2*y2*y3 + 6*x2**2*x3**2*y3**2 + x2*x3**3*y1**2 + 2*x2*x3**3*y1*y2 + 4*x2*x3**3*y1*y3 + 3*x2*x3**3*y2**2 + 8*x2*x3**3*y2*y3 + 10*x2*x3**3*y3**2 + x3**4*y1**2 + x3**4*y1*y2 + 5*x3**4*y1*y3 + x3**4*y2**2 + 5*x3**4*y2*y3 + 15*x3**4*y3**2
    #fml2=sp.expand(sx**ex*sy**ey)
    #x8=x1**8 + x1**7*x2 + x1**7*x3 + x1**6*x2**2 + x1**6*x2*x3 + x1**6*x3**2 + x1**5*x2**3 + x1**5*x2**2*x3 + x1**5*x2*x3**2 + x1**5*x3**3 + x1**4*x2**4 + x1**4*x2**3*x3 + x1**4*x2**2*x3**2 + x1**4*x2*x3**3 + x1**4*x3**4 + x1**3*x2**5 + x1**3*x2**4*x3 + x1**3*x2**3*x3**2 + x1**3*x2**2*x3**3 + x1**3*x2*x3**4 + x1**3*x3**5 + x1**2*x2**6 + x1**2*x2**5*x3 + x1**2*x2**4*x3**2 + x1**2*x2**3*x3**3 + x1**2*x2**2*x3**4 + x1**2*x2*x3**5 + x1**2*x3**6 + x1*x2**7 + x1*x2**6*x3 + x1*x2**5*x3**2 + x1*x2**4*x3**3 + x1*x2**3*x3**4 + x1*x2**2*x3**5 + x1*x2*x3**6 + x1*x3**7 + x2**8 + x2**7*x3 + x2**6*x3**2 + x2**5*x3**3 + x2**4*x3**4 + x2**3*x3**5 + x2**2*x3**6 + x2*x3**7 + x3**8
#x2y2=x1**2*y1**2 + 2*x1**2*y1*y2 + 2*x1**2*y1*y3 + x1**2*y2**2 + 2*x1**2*y2*y3 + x1**2*y3**2 + 2*x1*x2*y1**2 + 4*x1*x2*y1*y2 + 4*x1*x2*y1*y3 + 2*x1*x2*y2**2 + 4*x1*x2*y2*y3 + 2*x1*x2*y3**2 + 2*x1*x3*y1**2 + 4*x1*x3*y1*y2 + 4*x1*x3*y1*y3 + 2*x1*x3*y2**2 + 4*x1*x3*y2*y3 + 2*x1*x3*y3**2 + x2**2*y1**2 + 2*x2**2*y1*y2 + 2*x2**2*y1*y3 + x2**2*y2**2 + 2*x2**2*y2*y3 + x2**2*y3**2 + 2*x2*x3*y1**2 + 4*x2*x3*y1*y2 + 4*x2*x3*y1*y3 + 2*x2*x3*y2**2 + 4*x2*x3*y2*y3 + 2*x2*x3*y3**2 + x3**2*y1**2 + 2*x3**2*y1*y2 + 2*x3**2*y1*y3 + x3**2*y2**2 + 2*x3**2*y2*y3 + x3**2*y3**2
    #x3y3=20*x1**3*y1**3 + 10*x1**3*y1**2*y2 + 10*x1**3*y1**2*y3 + 4*x1**3*y1*y2**2 + 4*x1**3*y1*y2*y3 + 4*x1**3*y1*y3**2 + x1**3*y2**3 + x1**3*y2**2*y3 + x1**3*y2*y3**2 + x1**3*y3**3 + 10*x1**2*x2*y1**3 + 12*x1**2*x2*y1**2*y2 + 6*x1**2*x2*y1**2*y3 + 9*x1**2*x2*y1*y2**2 + 6*x1**2*x2*y1*y2*y3 + 3*x1**2*x2*y1*y3**2 + 4*x1**2*x2*y2**3 + 3*x1**2*x2*y2**2*y3 + 2*x1**2*x2*y2*y3**2 + x1**2*x2*y3**3 + 10*x1**2*x3*y1**3 + 6*x1**2*x3*y1**2*y2 + 12*x1**2*x3*y1**2*y3 + 3*x1**2*x3*y1*y2**2 + 6*x1**2*x3*y1*y2*y3 + 9*x1**2*x3*y1*y3**2 + x1**2*x3*y2**3 + 2*x1**2*x3*y2**2*y3 + 3*x1**2*x3*y2*y3**2 + 4*x1**2*x3*y3**3 + 4*x1*x2**2*y1**3 + 9*x1*x2**2*y1**2*y2 + 3*x1*x2**2*y1**2*y3 + 12*x1*x2**2*y1*y2**2 + 6*x1*x2**2*y1*y2*y3 + 2*x1*x2**2*y1*y3**2 + 10*x1*x2**2*y2**3 + 6*x1*x2**2*y2**2*y3 + 3*x1*x2**2*y2*y3**2 + x1*x2**2*y3**3 + 4*x1*x2*x3*y1**3 + 6*x1*x2*x3*y1**2*y2 + 6*x1*x2*x3*y1**2*y3 + 6*x1*x2*x3*y1*y2**2 + 8*x1*x2*x3*y1*y2*y3 + 6*x1*x2*x3*y1*y3**2 + 4*x1*x2*x3*y2**3 + 6*x1*x2*x3*y2**2*y3 + 6*x1*x2*x3*y2*y3**2 + 4*x1*x2*x3*y3**3 + 4*x1*x3**2*y1**3 + 3*x1*x3**2*y1**2*y2 + 9*x1*x3**2*y1**2*y3 + 2*x1*x3**2*y1*y2**2 + 6*x1*x3**2*y1*y2*y3 + 12*x1*x3**2*y1*y3**2 + x1*x3**2*y2**3 + 3*x1*x3**2*y2**2*y3 + 6*x1*x3**2*y2*y3**2 + 10*x1*x3**2*y3**3 + x2**3*y1**3 + 4*x2**3*y1**2*y2 + x2**3*y1**2*y3 + 10*x2**3*y1*y2**2 + 4*x2**3*y1*y2*y3 + x2**3*y1*y3**2 + 20*x2**3*y2**3 + 10*x2**3*y2**2*y3 + 4*x2**3*y2*y3**2 + x2**3*y3**3 + x2**2*x3*y1**3 + 3*x2**2*x3*y1**2*y2 + 2*x2**2*x3*y1**2*y3 + 6*x2**2*x3*y1*y2**2 + 6*x2**2*x3*y1*y2*y3 + 3*x2**2*x3*y1*y3**2 + 10*x2**2*x3*y2**3 + 12*x2**2*x3*y2**2*y3 + 9*x2**2*x3*y2*y3**2 + 4*x2**2*x3*y3**3 + x2*x3**2*y1**3 + 2*x2*x3**2*y1**2*y2 + 3*x2*x3**2*y1**2*y3 + 3*x2*x3**2*y1*y2**2 + 6*x2*x3**2*y1*y2*y3 + 6*x2*x3**2*y1*y3**2 + 4*x2*x3**2*y2**3 + 9*x2*x3**2*y2**2*y3 + 12*x2*x3**2*y2*y3**2 + 10*x2*x3**2*y3**3 + x3**3*y1**3 + x3**3*y1**2*y2 + 4*x3**3*y1**2*y3 + x3**3*y1*y2**2 + 4*x3**3*y1*y2*y3 + 10*x3**3*y1*y3**2 + x3**3*y2**3 + 4*x3**3*y2**2*y3 + 10*x3**3*y2*y3**2 + 20*x3**3*y3**3
    #x4y4=70*x1**4*y1**4 + 35*x1**4*y1**3*y2 + 35*x1**4*y1**3*y3 + 15*x1**4*y1**2*y2**2 + 15*x1**4*y1**2*y2*y3 + 15*x1**4*y1**2*y3**2 + 5*x1**4*y1*y2**3 + 5*x1**4*y1*y2**2*y3 + 5*x1**4*y1*y2*y3**2 + 5*x1**4*y1*y3**3 + x1**4*y2**4 + x1**4*y2**3*y3 + x1**4*y2**2*y3**2 + x1**4*y2*y3**3 + x1**4*y3**4 + 35*x1**3*x2*y1**4 + 40*x1**3*x2*y1**3*y2 + 20*x1**3*x2*y1**3*y3 + 30*x1**3*x2*y1**2*y2**2 + 20*x1**3*x2*y1**2*y2*y3 + 10*x1**3*x2*y1**2*y3**2 + 16*x1**3*x2*y1*y2**3 + 12*x1**3*x2*y1*y2**2*y3 + 8*x1**3*x2*y1*y2*y3**2 + 4*x1**3*x2*y1*y3**3 + 5*x1**3*x2*y2**4 + 4*x1**3*x2*y2**3*y3 + 3*x1**3*x2*y2**2*y3**2 + 2*x1**3*x2*y2*y3**3 + x1**3*x2*y3**4 + 35*x1**3*x3*y1**4 + 20*x1**3*x3*y1**3*y2 + 40*x1**3*x3*y1**3*y3 + 10*x1**3*x3*y1**2*y2**2 + 20*x1**3*x3*y1**2*y2*y3 + 30*x1**3*x3*y1**2*y3**2 + 4*x1**3*x3*y1*y2**3 + 8*x1**3*x3*y1*y2**2*y3 + 12*x1**3*x3*y1*y2*y3**2 + 16*x1**3*x3*y1*y3**3 + x1**3*x3*y2**4 + 2*x1**3*x3*y2**3*y3 + 3*x1**3*x3*y2**2*y3**2 + 4*x1**3*x3*y2*y3**3 + 5*x1**3*x3*y3**4 + 15*x1**2*x2**2*y1**4 + 30*x1**2*x2**2*y1**3*y2 + 10*x1**2*x2**2*y1**3*y3 + 36*x1**2*x2**2*y1**2*y2**2 + 18*x1**2*x2**2*y1**2*y2*y3 + 6*x1**2*x2**2*y1**2*y3**2 + 30*x1**2*x2**2*y1*y2**3 + 18*x1**2*x2**2*y1*y2**2*y3 + 9*x1**2*x2**2*y1*y2*y3**2 + 3*x1**2*x2**2*y1*y3**3 + 15*x1**2*x2**2*y2**4 + 10*x1**2*x2**2*y2**3*y3 + 6*x1**2*x2**2*y2**2*y3**2 + 3*x1**2*x2**2*y2*y3**3 + x1**2*x2**2*y3**4 + 15*x1**2*x2*x3*y1**4 + 20*x1**2*x2*x3*y1**3*y2 + 20*x1**2*x2*x3*y1**3*y3 + 18*x1**2*x2*x3*y1**2*y2**2 + 24*x1**2*x2*x3*y1**2*y2*y3 + 18*x1**2*x2*x3*y1**2*y3**2 + 12*x1**2*x2*x3*y1*y2**3 + 18*x1**2*x2*x3*y1*y2**2*y3 + 18*x1**2*x2*x3*y1*y2*y3**2 + 12*x1**2*x2*x3*y1*y3**3 + 5*x1**2*x2*x3*y2**4 + 8*x1**2*x2*x3*y2**3*y3 + 9*x1**2*x2*x3*y2**2*y3**2 + 8*x1**2*x2*x3*y2*y3**3 + 5*x1**2*x2*x3*y3**4 + 15*x1**2*x3**2*y1**4 + 10*x1**2*x3**2*y1**3*y2 + 30*x1**2*x3**2*y1**3*y3 + 6*x1**2*x3**2*y1**2*y2**2 + 18*x1**2*x3**2*y1**2*y2*y3 + 36*x1**2*x3**2*y1**2*y3**2 + 3*x1**2*x3**2*y1*y2**3 + 9*x1**2*x3**2*y1*y2**2*y3 + 18*x1**2*x3**2*y1*y2*y3**2 + 30*x1**2*x3**2*y1*y3**3 + x1**2*x3**2*y2**4 + 3*x1**2*x3**2*y2**3*y3 + 6*x1**2*x3**2*y2**2*y3**2 + 10*x1**2*x3**2*y2*y3**3 + 15*x1**2*x3**2*y3**4 + 5*x1*x2**3*y1**4 + 16*x1*x2**3*y1**3*y2 + 4*x1*x2**3*y1**3*y3 + 30*x1*x2**3*y1**2*y2**2 + 12*x1*x2**3*y1**2*y2*y3 + 3*x1*x2**3*y1**2*y3**2 + 40*x1*x2**3*y1*y2**3 + 20*x1*x2**3*y1*y2**2*y3 + 8*x1*x2**3*y1*y2*y3**2 + 2*x1*x2**3*y1*y3**3 + 35*x1*x2**3*y2**4 + 20*x1*x2**3*y2**3*y3 + 10*x1*x2**3*y2**2*y3**2 + 4*x1*x2**3*y2*y3**3 + x1*x2**3*y3**4 + 5*x1*x2**2*x3*y1**4 + 12*x1*x2**2*x3*y1**3*y2 + 8*x1*x2**2*x3*y1**3*y3 + 18*x1*x2**2*x3*y1**2*y2**2 + 18*x1*x2**2*x3*y1**2*y2*y3 + 9*x1*x2**2*x3*y1**2*y3**2 + 20*x1*x2**2*x3*y1*y2**3 + 24*x1*x2**2*x3*y1*y2**2*y3 + 18*x1*x2**2*x3*y1*y2*y3**2 + 8*x1*x2**2*x3*y1*y3**3 + 15*x1*x2**2*x3*y2**4 + 20*x1*x2**2*x3*y2**3*y3 + 18*x1*x2**2*x3*y2**2*y3**2 + 12*x1*x2**2*x3*y2*y3**3 + 5*x1*x2**2*x3*y3**4 + 5*x1*x2*x3**2*y1**4 + 8*x1*x2*x3**2*y1**3*y2 + 12*x1*x2*x3**2*y1**3*y3 + 9*x1*x2*x3**2*y1**2*y2**2 + 18*x1*x2*x3**2*y1**2*y2*y3 + 18*x1*x2*x3**2*y1**2*y3**2 + 8*x1*x2*x3**2*y1*y2**3 + 18*x1*x2*x3**2*y1*y2**2*y3 + 24*x1*x2*x3**2*y1*y2*y3**2 + 20*x1*x2*x3**2*y1*y3**3 + 5*x1*x2*x3**2*y2**4 + 12*x1*x2*x3**2*y2**3*y3 + 18*x1*x2*x3**2*y2**2*y3**2 + 20*x1*x2*x3**2*y2*y3**3 + 15*x1*x2*x3**2*y3**4 + 5*x1*x3**3*y1**4 + 4*x1*x3**3*y1**3*y2 + 16*x1*x3**3*y1**3*y3 + 3*x1*x3**3*y1**2*y2**2 + 12*x1*x3**3*y1**2*y2*y3 + 30*x1*x3**3*y1**2*y3**2 + 2*x1*x3**3*y1*y2**3 + 8*x1*x3**3*y1*y2**2*y3 + 20*x1*x3**3*y1*y2*y3**2 + 40*x1*x3**3*y1*y3**3 + x1*x3**3*y2**4 + 4*x1*x3**3*y2**3*y3 + 10*x1*x3**3*y2**2*y3**2 + 20*x1*x3**3*y2*y3**3 + 35*x1*x3**3*y3**4 + x2**4*y1**4 + 5*x2**4*y1**3*y2 + x2**4*y1**3*y3 + 15*x2**4*y1**2*y2**2 + 5*x2**4*y1**2*y2*y3 + x2**4*y1**2*y3**2 + 35*x2**4*y1*y2**3 + 15*x2**4*y1*y2**2*y3 + 5*x2**4*y1*y2*y3**2 + x2**4*y1*y3**3 + 70*x2**4*y2**4 + 35*x2**4*y2**3*y3 + 15*x2**4*y2**2*y3**2 + 5*x2**4*y2*y3**3 + x2**4*y3**4 + x2**3*x3*y1**4 + 4*x2**3*x3*y1**3*y2 + 2*x2**3*x3*y1**3*y3 + 10*x2**3*x3*y1**2*y2**2 + 8*x2**3*x3*y1**2*y2*y3 + 3*x2**3*x3*y1**2*y3**2 + 20*x2**3*x3*y1*y2**3 + 20*x2**3*x3*y1*y2**2*y3 + 12*x2**3*x3*y1*y2*y3**2 + 4*x2**3*x3*y1*y3**3 + 35*x2**3*x3*y2**4 + 40*x2**3*x3*y2**3*y3 + 30*x2**3*x3*y2**2*y3**2 + 16*x2**3*x3*y2*y3**3 + 5*x2**3*x3*y3**4 + x2**2*x3**2*y1**4 + 3*x2**2*x3**2*y1**3*y2 + 3*x2**2*x3**2*y1**3*y3 + 6*x2**2*x3**2*y1**2*y2**2 + 9*x2**2*x3**2*y1**2*y2*y3 + 6*x2**2*x3**2*y1**2*y3**2 + 10*x2**2*x3**2*y1*y2**3 + 18*x2**2*x3**2*y1*y2**2*y3 + 18*x2**2*x3**2*y1*y2*y3**2 + 10*x2**2*x3**2*y1*y3**3 + 15*x2**2*x3**2*y2**4 + 30*x2**2*x3**2*y2**3*y3 + 36*x2**2*x3**2*y2**2*y3**2 + 30*x2**2*x3**2*y2*y3**3 + 15*x2**2*x3**2*y3**4 + x2*x3**3*y1**4 + 2*x2*x3**3*y1**3*y2 + 4*x2*x3**3*y1**3*y3 + 3*x2*x3**3*y1**2*y2**2 + 8*x2*x3**3*y1**2*y2*y3 + 10*x2*x3**3*y1**2*y3**2 + 4*x2*x3**3*y1*y2**3 + 12*x2*x3**3*y1*y2**2*y3 + 20*x2*x3**3*y1*y2*y3**2 + 20*x2*x3**3*y1*y3**3 + 5*x2*x3**3*y2**4 + 16*x2*x3**3*y2**3*y3 + 30*x2*x3**3*y2**2*y3**2 + 40*x2*x3**3*y2*y3**3 + 35*x2*x3**3*y3**4 + x3**4*y1**4 + x3**4*y1**3*y2 + 5*x3**4*y1**3*y3 + x3**4*y1**2*y2**2 + 5*x3**4*y1**2*y2*y3 + 15*x3**4*y1**2*y3**2 + x3**4*y1*y2**3 + 5*x3**4*y1*y2**2*y3 + 15*x3**4*y1*y2*y3**2 + 35*x3**4*y1*y3**3 + x3**4*y2**4 + 5*x3**4*y2**3*y3 + 15*x3**4*y2**2*y3**2 + 35*x3**4*y2*y3**3 + 70*x3**4*y3**4
    #fml=sp.factor(IntCuad.intet3(3,3))
    #c=IntCuad.cf(fml)
    #return x3y3#fml/c

def var(i,j):
    r=0
    if((i>=0)&(j>=0)&(i+j>0)):
        if(i>0):
            x1,x2,x3=sp.symbols('x1,x2,x3')#'x%i'%(e+1))globals()['x%i'%(e+1)]
        if(j>0):
            y1,y2,y3=sp.symbols('y1,y2,y3')#'y%i'%(e+1))globals()['y%i'%(e+1)]
        mn=min(i,j)
        if(mn==0):
            if(i>0):
                globals()['sx']=x1+x2+x3
                r=sp.expand(sx**i)
            else:
                globals()['sy']=y1+y2+y3
                r=sp.expand(sy**j)
        else:
            globals()['sy']=y1+y2+y3
            globals()['sx']=x1+x2+x3
            r=sp.expand(sx**i*sy**j)
    return r

def cmpl(x):
    r=[]
    if(len(x)>=0):
        r=list(set(range(3))-set(x))
    return r

def pcn(Mi,c,g):
    p=[]
    if((len(Mi)>0)&(g in [0,1])&(c in [0,1])):
        v=Mi[g*3:(g+1)*3]
        p=np.where((v==0)&(c==0)|(v!=0)&(c!=0))[0]
    return p

def intr(u,v):
    return list(set(u).intersection(set(v)))

def intr2(u,v):
    r=[]
    l=len(u)
    i=0
    while(i<l):
        if(u[i]==v[i]):
            r+=[i]
        i+=1
    return r

def efi(Mi,i,g):
    r=np.zeros(1).astype(int)
    if((len(Mi)>0)&(len(i)>0)&(g in [0,1])):
        ii=[3*g+j for j in i];r=Mi[ii]
    return r

def cmpv(u,v,esp):
    b=False
    l=len(u)
    if((l==len(v))&(l>0)&(b in [True,False])):
        if(esp):
            b=sum(u==v)==l
        else:
            b=set(u)==set(v)
    return b

def avance(formula):
    ky=list(formula.as_coefficients_dict().keys())
    vl=list(formula.as_coefficients_dict().values())
    #primera agrupacion
    uq=list(set(vl))
    #uqc=[]
    #for i in uq:
    #    uqc+=[vl.count(i)]
    Vl=np.array(vl)
    Ky=np.array(ky)
    mti=[list(np.where(Vl==i)[0])for i in uq]
    #l1=[list(Vl[i])for i in mti]
    l=[list(Ky[i])for i in mti]
    return [uq,l]

def expg(l):
    me=np.zeros((len(l),6)).astype(int)
    for i in range(len(l)):
        for j in range(3):
            me[i,j]=dg(l[i],globals()['x%i'%(j+1)])
            me[i,3+j]=dg(l[i],globals()['y%i'%(j+1)])
    return me

def agrc(llg):
    r=1
    i=0
    while((r>=0)&(i<len(llg))):
        l=len(llg[i])
        if(l!=3)&(l!=6)&(l!=1):
            r=0
            if((l%3!=0)&(l!=1)):
                #print('\x1b[%im Problema de agrupacion... \x1b[0m'%41)
                r=-1
        i+=1
    return r

def agrc2(l):
    def pbt(e):
        b=True
        i=0
        while(i<3):
            ex=list(e[i][:3]);ey=list(e[i][3:])
            j=0;ix=[];iy=[]
            while(j<3):
                if(ex.count(ex[j])>1):
                    ix+=[j]
                if(ey.count(ey[j])>1):
                    iy+=[j]
                j+=1
            tr=intr(ix,iy)
            if(len(tr)!=2):
                b=False
                break
            i+=1
        return b
    r=agrc(l)
    if(r==1):
        i=0
        while(i<len(l)):
            if(len(l[i])==3):
                e=expg(l[i])
                if not pbt(e):
                    r=0
                    break
            elif(len(l[i])==1):
                if(len(set(expg(l[i])[0]))>2):
                    r=0
                    break
            i+=1
    return r

def mns(l):
    s=0
    if(len(l)>0):
        for i in l:
            s+=len(i)
    return s

def agr(formula,formula2):
    [co,lo]=avance(formula)
    ky=list(formula2.as_coefficients_dict().keys())
    vl=list(formula2.as_coefficients_dict().values())
    #ng=np.zeros((len(ky),2)).astype(int)
    #k=0
    nl=[];nc=[]
    for i in range(len(co)):
        lt=[]
        for j in range(len(lo[i])):
            ii=ky.index(lo[i][j])
            lt+=[vl[ii]]
        lta=np.array(lt)
        uq=list(set(lt))
        isg=[list(np.where(lta==j)[0])for j in uq]
        nl+=[list(np.array(lo[i])[j])for j in isg]
        nc+=[int(co[i])for j in range(len(isg))]
    return [nc,nl]

def aut(l):
    r=0
    if(len(l)==6):
        Me=expg(l)
        ex=Me[:,:3];ey=Me[:,3:]
        x0=np.where(ex[0]==0)[0];y0=np.where(ey[0]==0)[0]
        tr0=set(x0).intersection(set(y0))
        if(len(tr0)>0):
            r=1
    return r

def agr2(cB,lB,frm):
    def bsi(l,Cr,Lr):
        r=[];cl=[];cr=[]
        i=0
        while(i<len(l)):
            cl+=[i]
            if(l[i] in Lr):
                cr+=[Cr[Lr.index(l[i])]]
            else:
                cr+=[-1]
            i+=1
        u=list(set(cr))
        r=[[cl[i] for i in list(np.where(np.array(cr)==j)[0])]for j in u]
        return r
    nl=[];nc=[]
    if((len(cB)>0)&(len(lB)==len(cB))):
        d=frm.as_coefficients_dict()
        k=list(d.keys())
        v=list(d.values())
        C=cB.copy();L=lB.copy()
        while(len(L)>0):
            idx=bsi(L[0],v,k)
            if(len(idx)>1):
                nl+=[[L[0][i]for i in j]for j in idx]
                vv=[[L[0][i]for i in j]for j in idx]
                nc+=[[C[0],aut(vv[j])]for j in range(len(idx))]
            else:
                nl+=[L[0]]
                nc+=[[C[0],aut(L[0])]]
            C.remove(C[0])
            L.remove(L[0])
    return [nc,nl]

def agrx(cg,llg):
    def crG(lg,lng,M,j):
        [f,c]=M.shape
        if((f>0)&(c>0)&(len(lg)>0)):
            lng+=[lg[j]]
            M=np.delete(M,j,0)
            lg.remove(lg[j])
        return [lg,lng,M]
    nl=[];nc=[]
    if(True|(agrc(llg)>-1)):
        while(0!=len(cg)):
            lt=llg[0].copy()
            ct=cg[0]
            llg.remove(lt)
            cg.remove(ct)
            a=0
            if(len(lt)in[1,3]):
                #print('Antes %i'%len(lt),end='\t')#;print(lt)#for i in nl: #    print(i,end='\n')#print('.........................')#nl+=[lt.copy()]#nc+=[[ct,0]] #print('Despues %i'%len(lt),end='\t'#for i in nl:    print(i,end='\n')#print('')
                nl+=[lt.copy()]
                nc+=[[ct,a]]
            elif(len(lt)==6):
                while(len(lt)!=0):
                    a=0
                    Me=expg(lt)
                    me=Me[0,:]; Me=np.delete(Me,0,0)
                    l0=lt[0]; lt.remove(l0)
                    lt1=[l0]
                    pcx0=pcn(me,0,0); pcy0=pcn(me,0,1)#np.where(me[3:]==0)[0]
                    j=0
                    while(j<len(Me)):
                        pcx=pcn(Me[j,:],0,0); pcy=pcn(Me[j,:],0,1)#np.where(Me[j,3:]==0)[0]#pnx=np.where(Me[j,:3]!=0)[0];pny=np.where(Me[j,3:]!=0)[0]
                        if((len(pcx0)==len(pcx))&(len(pcy0)==len(pcy))):
                            [lt,lt1,Me]=crG(lt,lt1,Me,j)
                        else:
                            j+=1
                    if(len(lt1)==6):#Grupo de seis aceptado
                        me=expg(lt1[:1])[0]
                        pc1=pcn(me,0,0); pc2=pcn(me,0,1)#np.where(me[0,:3]==0)[0]np.where(me[0,3:]==0)[0]#pnc1=np.where(me[0,:3]!=0)[0];pnc2=np.where(me[0,3:]!=0)[0];print(pc1,end='\t');print(pc2,end='\t');print(pnc1,end='\t');print(pnc2,end='\t');print(me)
                        if(len(intr(pc1,pc2))>0):#|(len(set(pnc1).intersection(set(pnc2)))==2)):set(pc1).intersection(set(pc2))
                            a=1
                    nl+=[lt1.copy()]
                    nc+=[[ct,a]]#print(lt,end='\t');print(a,end='\n\n')
            else:
                Me=expg(lt)
                while(len(lt)!=0):#print('len(cg): %i\t len(lt): %i\tlen(Me): %i'%(len(cg),len(lt),len(Me)))
                    a=0
                    me=Me[0,:]
                    l0=lt[0]#;print(l0)
                    lt.remove(l0)
                    Me=np.delete(Me,0,0)
                    lt1=[l0]
                    pcx0=pcn(me,0,0); pcy0=pcn(me,0,1)#np.where(me[:3]==0)[0]np.where(me[3:]==0)[0]
                    pnx0=pcn(me,1,0); pny0=pcn(me,1,1)#np.where(me[:3]!=0)[0]np.where(me[3:]!=0)[0]
                    if((len(pcx0)>0)&(len(pcy0)>0)):
                        trs0=intr(pcx0,pcy0)#list(set(pcx0).intersection(set(pcy0)))
                        j=0
                        while(j<len(Me)):
                            a=0#print(lt,end='\t');print(l0)
                            pcx=pcn(Me[j,:],0,0);pcy=pcn(Me[j,:],0,1)#np.where(Me[j,:3]==0)[0]np.where(Me[j,3:]==0)[0]
                            pnx=pcn(Me[j,:],1,0);pny=pcn(Me[j,:],1,1)#np.where(Me[j,:3]!=0)[0]np.where(Me[j,3:]!=0)[0]#print('\t%i'%len(Me))#print(pcx,end='\t');
                            if((len(pcx)>0)&(len(pcy)>0)):
                                trs=intr(pcx,pcy)#list(set(pcx).intersection(set(pcy)))
                                if(len(trs0)==2):#print(len(trs),end='\t');print(len(trs0))
                                    if(len(trs)==2):
                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                        a=1
                                    else:
                                        j+=1
                                elif(len(trs0)==1):
                                    if(len(trs)==1):
                                        tr0=intr(pnx0,pny0);tr=intr(pnx,pny)#list(set(pnx0).intersection(set(pny0)))list(set(pnx).intersection(set(pny)))
                                        if(len(tr0)==2):
                                            if(len(tr)==2):#caso x1^ex.x2^ex2.y1^ey.y2^ey2
                                                if((np.max(me[:3])==np.max(Me[j,:3]))&(np.max(me[3:])==np.max(Me[j,3:]))):
                                                    ex0=efi(me,tr0,0); ey0=efi(me,tr0,1); ex=efi(Me[j,:],tr,0); ey=efi(Me[j,:],tr,1)#me[tr0]me[list(3+np.array(tr0))]Me[j,tr]Me[j,list(3+np.array(tr))]#print(me[:3],end='\t');print(me[3:],end='\t');print(Me[j,:3],Me[j,3:])
                                                    if((ex0[0]==ex0[1])&(ey0[0]==ey0[1])&(ex[0]==ex[1])&(ey[0]==ey[1])): #((ex0[0]==ey0[0])&(ex[0]==ey[0])):# caso x1^i.x2.y1^i.y2
                                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                    elif((ex0[0]==ex0[1])&(ex[0]==ex[1])&(max(ey0)==max(ey))|(ey0[0]==ey0[1])&(ey[0]==ey[1])&(max(ex0)==max(ex))):#((ex0[0]!=ey0[0])&(ex[0]!=ey[0])):#caso x1^i.x2^(m-i).y1^j.y2^(n-j)
                                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)#por separar
                                                    elif((max(ex0)==max(ex))&(max(ey0)==max(ey))&((ex0[0]==ex[0])&(ey0[0]==ey[0])|(ex0[0]!=ex[0])&(ey0[0]!=ey[0]))):
                                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)#por separar
                                                    else:
                                                        j+=1
                                                else:
                                                    j+=1
                                        else:#(len(tr0)==1):caso: x1^i.x2^(n-i).y1^j.y3^(n-j) [n=i 0 i=0 o j=0 o n=j]
                                            if((np.max(me[:3])==np.max(Me[j,:3]))&(np.max(me[3:])==np.max(Me[j,3:]))):
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            else:
                                                j+=1 #lt1+=[lt[j]]#Me=np.delete(Me,j,0)#lt.remove(lt[j])
                                        a=1
                                    else:
                                        j+=1
                                else:#caso x1^i.x2^(n-i).y1^j.y3^(n-j)
                                    if(len(trs)==0):
                                        if((len(pcx0)==len(pcx))&(len(pcy0)==len(pcy))):#caso no necesario
                                            if((np.max(me[:3])==np.max(Me[j,:3]))&(np.max(me[3:])==np.max(Me[j,3:]))):
                                                tr0=intr(pnx0,pny0);tr=intr(pnx,pny)#list(set(pnx0).intersection(set(pny0)))list(set(pnx).intersection(set(pny)))
                                                if(len(tr0)==1):
                                                    if((len(tr0)==len(tr))&(me[tr0]==Me[j,tr])):
                                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                    else:
                                                        j+=1
                                                else:
                                                    [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            else:
                                                j+=1
                                        else:
                                            j+=1
                                    else:
                                        j+=1
                            else:
                                j+=1
                    elif((len(pcx0)==2)|(len(pcx0)==1)|(len(pcy0)==2)|(len(pcy0)==1)):
                        tr0=intr(pnx0,pny0)
                        ##    pct=np.copy(pcx0)#    li=list(range(3))#else:#    pct=np.copy(pcy0)
                        #    li=list(range(3,6))#print(lt);print(mE);print(pct,end='\t');print(pnx0,end='\t');print(pny0,end='\t');print(set(pnx0).intersection(set(pny0))) if((len(pct)==len(pc))&(np.max(Me[j,li])==np.max(me[li]))):
                        a=0#if(len(set(pnx0).intersection(set(pny0)))==2):#    a=1
                        j=0#;print('Me');print(Me)
                        while(j<len(Me)):
                            pnx=pcn(Me[j,:],1,0); pny=pcn(Me[j,:],1,1)
                            pcx=pcn(Me[j,:],0,0); pcy=pcn(Me[j,:],0,1) #np.where(Me[j,li]==0)[0]
                            if((len(pcx0)==len(pcx))&(len(pcy0)==len(pcy))):
                                tr=intr(pnx,pny)#;print(tr)
                                if(len(tr0)==2):#Caso xi^exi.xj^exj.xk^exk.yi^eyi.yj^eyj
                                    if(len(tr)==2):
                                        ex0=efi(me,tr0,0);ey0=efi(me,tr0,1)#;print('Caso tr=2');print(me);print(ex0,ey0)
                                        ex=efi(Me[j,:],tr,0);ey=efi(Me[j,:],tr,1)#;print('lt[j],ex,ey');print(lt[j]);print(ex,ey)
                                        ctr0=cmpl(tr0);ctr=cmpl(tr)#;print('pcx0',pcx0)
                                        ec0=efi(me,ctr0,1-len(pcx0)); ec=efi(Me[j,:],ctr,1-len(pcx))
                                        if((cmpv(ex,ex0,False))&(cmpv(ey,ey0,False))&(ec==ec0)):#Caso xi^4.xj^2.xk^ec.yi^2.yj^4
                                            if((cmpv(ex,ey,True))&(cmpv(ex0,ey0,True))):#Caso xi^2.xj^4.xk^ec.yi^2.yj^4
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j) #lt1+=[lt[j]];Me=np.delete(Me,j,0);lt.remove(lt[j])
                                            elif((not cmpv(ex,ey,True))&(not cmpv(ex0,ey0,True))):#Caso xi^4.xj^2.xk^ec.yi^2.yj^4
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            else:
                                                j+=1
                                        else:
                                            j+=1
                                    else:
                                        j+=1
                                elif(len(tr0)==1):#Caso x1^i.x2^j.x3^k.y1^l
                                    ex0=efi(me,tr0,0); ey0=efi(me,tr0,1)
                                    ex=efi(Me[j,:],tr,0); ey=efi(Me[j,:],tr,1)
                                    if(len(tr)==1):
                                        ctr0=cmpl(tr0); ctr=cmpl(tr)#; print('ex0,ey0,ex,ey',ex0,ey0,ex,ey)
                                        xy=1-len(pnx0)//2; ec0=efi(me,ctr0,xy); ec=efi(Me[j,:],ctr,xy)#; print('Me[j,:], me',me,Me[j,:])
                                        if((ex==ex0)&(ey==ey0)):
                                            if(cmpv(ec,ec0,False)):
                                                if((ex0==ey0)):
                                                    [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                elif((ex0!=ey0)):
                                                    [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                else:
                                                    j+=1
                                            else:
                                                j+=1
                                        else:
                                            j+=1
                                    else:
                                        j+=1
                                else:
                                    j+=1
                            else:
                                j+=1
                    else:
                        a=0
                        j=0
                        while(j<len(Me)):
                            if((len(pnx0)==3)&(len(pny0)==3)): #Caso x1^i.x2^j.x3^k.y1^l.y2^h.y3^m
                                pnx=pcn(Me[j,:],1,0); pny=pcn(Me[j,:],1,1)
                                if((len(pnx)==3)&(len(pny)==3)):
                                    ex0=efi(me,[0,1,2],0); ex=efi(Me[j,:],[0,1,2],0); ey0=efi(me,[0,1,2],1); ey=efi(Me[j,:],[0,1,2],1)
                                    if((cmpv(ex0,ex,False))&(cmpv(ey0,ey,False))): # iz y der de me y Me[j] tienen mismos exp (son analogos)
                                        lsx0=len(set(ex0)); lsx=len(set(ex))
                                        if((lsx0==len(set(ey0)))&(lsx==len(set(ey)))):
                                            if((lsx0==3)&(lsx==3)): #parte iz y der mismos exp
                                                tr0=intr2(ex0,ey0); tr=intr2(ex,ey)
                                                if((len(tr0)==len(tr)==1)): #mismo exp comun xi^e.yi^e
                                                    if(ex0[tr0[0]]==ex[tr[0]]):
                                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                    else:
                                                        j+=1
                                                elif((len(tr0)==len(tr)==3)&(cmpv(ex0,ex,True))): #mismos exp x1^a.x2^b.x3^c.y1^a.y2^b.y3^c 
                                                    [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                else:#mismos exp sin coincidencia x1^a.x2^b.x3^c.y1^b.y2^c.y3^a
                                                    ix=np.random.randint(3);xe0=ex0[ix];ye0=ey0[ix];ix=np.where(ex==xe0)[0][0];ye=ey[ix]
                                                    if(ye0==ye):
                                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                                    else:
                                                        j+=1
                                            elif((lsx0==2)&(lsx==2)):
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            elif((lsx0==1)&(lsx==1)):
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            elif((lsx==list(set([1,2,3])-{lsx0})[0])):
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            elif((lsx==list(set([1,2,3])-{lsx0})[1])):
                                                [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                            else:
                                                j+=1
                                        else:
                                            [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                    else:
                                        j+=1
                                else:
                                    j+=1
                            else: #Caso x1^i.x2^j.x3^k o y1^k.y2^l.y3^m
                                pnx=pcn(Me[j,:],1,0); pny=pcn(Me[j,:],1,1)
                                if(len(pnx)+len(pny)==3): #caso len(tr0)=0
                                    if(cmpv(me,Me[j,:],False)):
                                        [lt,lt1,Me]=crG(lt,lt1,Me,j)
                                    else:
                                        j+=1
                                else:
                                    j+=1
                    if(len(lt1)>0):#print(a,end='\t');print(lt1)
                        nl+=[lt1.copy()]
                        nc+=[[ct,a]]
    return[nc,nl]

def agrp(i,j,c,l):
    c1=[];l1=[]
    if((len(c)>0)&(len(l)==len(c))&(i>=0)&(j>=0)):
        b=False
        if(fls.idF(i,j)):
            [_,Fs2]=fls.lrF(i,j)
            b=True
        else:
            Fs=sms([],i,j,0)
            Fs2=sms([],i,j,1)
            fls.grF(i,j,Fs,Fs2)
            del Fs
        L=len(Fs2)
        #dt=0;t1=tm.time()
        k=0
        while(k<L):
            #t2=tm.time()
            #dt=list(tm.gmtime(t2-t1)[3:6])
            #t1=t2
            #prnt.pbc2(k,L,dt)
            if b:
                f=Fs2[k]
            else:
                f=IntCuad.frm3(Fs2[k])
            [c1,l1]=agr2(c,l,f)
            if(max([len(li)for li in l1])<=6):
                [c2,l2,f1,f2,f3]=grps(c1,l1)#;print(c1,l1)
                T=frms(c2,l2,Fs2)
                if smc(T,f1,f2,f3):
                    fls.grT(i,j,T,f1,f2,f3)
                    break
            k+=1
        #t2=tm.time();dt=list(tm.gmtime(t2-t1)[3:6])
        #prnt.pbc2(L,L,dt)
    return [c1,l1]

def grps(cg,llg):
    c=[];l=[];f1=0;f2=0;f3=0
    n=len(cg)
    if((n==len(llg))&(n>0)):
        ua=list(np.where(np.array(cg)[:,1]==1)[0])
        uac=list(set(range(n))-set(ua))
        lg=np.zeros((len(uac),1)).astype(int)
        for i in range(len(uac)):
            lg[i,0]=len(llg[uac[i]])
        u3=list(np.array(uac)[np.where(lg.T[0]==3)[0]])#;print(lg.T,np.where(lg.T[0]==3)[0],end='\t');print(uac)
        u1=list(np.array(uac)[np.where(lg.T[0]==1)[0]])#;print(set(uac)-set(u3)-set(u1),end='\t');print(u3,u1)
        uc=list(set(uac)-set(u3)-set(u1))
        f1=len(ua)
        f2=len(uc)
        f3=len(u3)#;print(ua+uc+u3+u1)
        for i in ua+uc+u3+u1:
            #print(i,end='\t');print(llg[i])
            l+=[np.sum(np.array(llg[i]))]
            c+=[cg[i][0]]
    return [c,l,f1,f2,f3]

#No es optimo, esta para revisar y mejorar
def frms(Cg,Lg,Fs):
    #lt=sms([],3,3,1)
    #[Cg,Lg,f1,f2,f3]=grps(cg,llg)
    f=len(Cg)
    c=len(Fs)
    t=np.zeros((f,c)).astype(int)
    i=0
    while(i<c):
        fsi=sp.expand(Fs[i])
        Lt=list(fsi.as_coefficients_dict().keys())
        Cf=list(fsi.as_coefficients_dict().values())
        j=0
        while(j<f):
            h=list(Lg[j].as_coefficients_dict().keys())
            hh=h[np.random.randint(len(h))]
            if(hh in Lt):
                t[j,i]=Cf[Lt.index(hh)]
            j+=1
        #print(len(h),end='\t')
        #print(Fs[i],end='\t');print(t[:,i])
        i+=1
    return t

def frms2(Cg,Lg,Fs):
    f=len(Cg)
    c=len(Fs)
    t=np.zeros((f,c)).astype(int)
    i=0
    while(i<c):
        Lt=list(Fs[i].as_coefficients_dict().keys())
        Cf=list(Fs[i].as_coefficients_dict().values())
        j=0
        while(j<f):
            h=list(Lg[j].as_coefficients_dict().keys())
            hh=h[np.random.randint(len(h))]
            if(hh in Lt):
                t[j,i]=Cf[Lt.index(hh)]
            j+=1
        i+=1
    return t

def smc(T,f1,f2,f3):
    [f,c]=T.shape
    b=True
    if((f>1)&(c>1)&(f1>1)&(f2>1)&(f3>1)&(f>=f1+f2+f3)):
        r=np.zeros((1,c)).astype(int)
        for j in range(c):
            r[0,j]=sum(T[:f1+f2,j])*6+sum(T[f1+f2:f1+f2+f3,j])*3+sum(T[f1+f2+f3:,j])
        i=0
        while(b&(i<c)):
            e=int(mt.log(r[0,i])/mt.log(3))
            if not(r[0,i]%(3**e)==0):
                b=False
            else:
                i+=1
    return b

def rarT(T,f1,f2,f3):
    [f,c]=T.shape;F=[];C=[]
    if((c>1)&(f>1)&(smc(T,f1,f2,f3))):
        e=np.zeros((1,c)).astype(int)
        s=np.zeros((1,c)).astype(int)
        for i in range(c):
            e[0,i]=len(np.where(T[:,i]!=0)[0])
            s[0,i]=sum(T[:,i])
        isce=e.argsort()[0,::-1]
        iss=s[0,isce].argsort()[::-1]#print(T[:,isce[iss]]) solucion momentanea
        C=isce[iss]#[np.where(s[0,iu[iu2]]>2)[0]] 
        mM=np.array([np.sort(T[i,C])[[0,len(C)-1]]for i in range(f)])
        fe=np.where((mM[:,0]==mM[:,1])&(mM[:,0]==1))[0][0]
        F=np.where((mM[:,0]!=mM[:,1])|(mM[:,0]!=1))[0]
        F=list(F)+[fe]
        iup=np.array([np.where(T[:,i]==1)[0][0]for i in C[-f1-1:-1]])
        iup=list(np.argsort(iup))
        C[-f1-1:-1]=C[-f1-1:-1][iup]
        #fsd=np.where(np.array([sum(T[i,C])for i in range(f)])==len(C))[0]
        #if(len(fsd)>0):
        #    if(len(fsd)>1):
        #        ir=fsd[np.where(np.array([T[i,:]==np.ones((1,len(C)).astype(int))for i in fsd]))[0]]
        #    else:
        #        ir=fsd[0]
        #    print(ir)
        #    F=list(set(range(f))-{ir})
        #else:
        #    print('\x1b[044m %s\x1b[0m'%'Error No se encuentra la fila referente a "repositorio"')
        #print(s[0,iu[iu2]],e[0,iu[iu2]])
        #i=0
        #while(i<c):
        #    isv=np.where(e[0,iu]==e[0,i])[0]
        #    isv2=np.argsort(s[isv])[::-1]
        #    iu[i:len(isv)]=isv2
        #    i+=len(isv)
        #    print(isv2,end='\t');print(i)
    return [F,C]

def smu(l,i,j):
    lt=l.copy()#1,0;2,0;1,1;2,1;2,2
    if((len(l)>=0)&((i==0)|(j==0))&(i+j>0)):
        n=i+j
        vr=(1-i//n)*'y'+(i//n)*'x'
        if(i+j==1):
            lt+=[globals()['s'+vr]]
        elif(i+j==2):
            lt+=[globals()['s'+vr]**2,globals()['s'+vr+str(2)]]
        #elif(i+j==3):
        #    lt+=[globals()['s'+vr+str(3)],globals()['s'+vr]*globals()['s'+vr+str(2)],globals()['s'+vr]**3]
        else:
            i0=0;j0=0
            for h in range(n,0,-1):
                if(h==n):
                    lt+=[globals()['s'+vr+str(h)]]
                else:
                    if(i==0):
                        j0=n-h
                    else:
                        i0=n-h
                    lt2=[]
                    lt2=smu(lt2,i0,j0)
                    for k in lt2:
                        if(h>1):
                            lt+=[globals()['s'+vr+str(h)]*k]
                        else:
                            lt+=[globals()['s'+vr]*k]
    return list(set(lt))

def smm(l,i,j):
    lt=l.copy()
    if((len(l)>=0)&(i>=1)&(j>=1)):
        if(i+j==2):
            lt+=[sxy]
        elif(i+j==3):
            sr=(1-i//2)*'sy'+(i//2)*'sx'
            sxiyj=(1-i//2)*'xy2'+(i//2)*'x2y'
            lt+=[globals()[sr]*sxy,globals()['s'+sxiyj]]
        #elif(i+j==4):
        #    if(i==j):
        #        lt+=[sxy**2,sxy*sx*sy,sx2y*sy,sx2y2,sxy2*sx]
        #    else:
        #        lxy=[]
        #        if(i==3):
        #            lx=smu(lxy,2,0)
        #            lt+=[sx2y*sx,sx3y]
        #            lt+=[sxy*v for v in lx]
        #        else:
        #            ly=smu(lxy,0,2)
        #            lt+=[sxy2*sy,sxy3]
        #            lt+=[sxy*v for v in ly]
        else:
            for sm in range(2,i+j+1):#h<=sm-1,i sm-h<=j ==> h>=sm-j
                for h in range(max(1,sm-j),min(sm-1,i)+1):
                    i0=h;j0=sm-h
                    #if((i==3)&(j==3)):
                    #    print(i0,j0)
                    if((i0==1)|(j0==1)):
                        if((i0==1)&(j0==1)):
                            vxy='sxy'
                        elif(j0==1):
                            vxy='sx'+str(i0)+'y'
                        else:
                            vxy='sxy'+str(j0)
                    else:
                        vxy='sx'+str(i0)+'y'+str(j0)
                    lt2=[]#;print(vxy,end='\t')
                    if(i0+j0==i+j):
                        lt+=[globals()[vxy]]
                    else:
                        if(min(i-i0,j-j0)==0):
                            lt2=smu(lt2,i-i0,j-j0)
                        else:
                            lt2=smm(lt2,i-i0,j-j0)#;print(i-i0,j-j0)
                            lx=[];ly=[]
                            lx=smu(lx,i-i0,0)
                            ly=smu(ly,0,j-j0)
                            lt2+=[ux*uy for uy in ly for ux in lx]
                        #print('lista para %i,%i'%(i-i0,j-j0),end='\t');print(lt2)
                        for v in lt2:
                            li=globals()[vxy]*v#;print(li)
                            if not( li in lt):
                                lt+=[li]
    return lt

def smm2(l,i,j):
    lt=l.copy()
    if((len(l)>=0)&(i>=1)&(j>=1)):
        if((i==1)|(j==1)):
            if(i==j):
                lt+=[sxy]
            else:
                m=max(i,j)
                for e in range(1,m+1):
                    if(e==1):
                        i0=i-1;j0=j-1
                        vxy='sxy'
                    else:
                        if(i==1):
                            i0=0;j0=j-e
                            vxy='sxy%s'%e
                        else:
                            i0=i-e;j0=0
                            vxy='sx%iy'%e
                    if(i0+j0==0):
                        lt+=[globals()[vxy]]
                    else:
                        lt2=[]
                        lt2=smu(lt2,i0,j0)
                        for f in lt2:
                            li=globals()[vxy]*f
                            if not(li in lt):
                                lt+=[li]
        else:
            for sm in range(2,i+j+1):
                for h in range(max(1,sm-j),min(sm-1,i)+1):
                    i0=h;j0=sm-h
                    if((i0==1)|(j0==1)):
                        if(i0==j0):
                            vxy='sxy'
                        else:
                            m=max(i0,j0)
                            vxy=(1-i0//m)*('sxy%i'%j0)+(i0//m)*('sx%iy'%i0)
                    else:
                        vxy='sx%iy%i'%(i0,j0)
                    if(i0+j0==i+j):
                        lt+=[globals()[vxy]]
                    else:
                        lt2=[]
                        if(min(i-i0,j-j0)==0):
                            lt2=smu(lt2,i-i0,j-j0)
                        else:
                            lt2=smm2(lt2,i-i0,j-j0)
                            lx=[];ly=[]
                            lx=smu(lx,i-i0,0)
                            ly=smu(ly,0,j-j0)
                            lt2+=[ux*uy for uy in ly for ux in lx]
                        for pxy in lt2:
                            li=pxy*globals()[vxy]
                            if not(li in lt):
                                lt+=[li]

    return lt

def sms(l,i,j,lg):
    if(lg==0):
        smdf(i,j)
    elif(lg==1):
        dfvr(i,j)
    lt=l.copy()
    if((len(l)>=0)&((i>0)|(j>0))):
        if((i==0)|(j==0)):
            m=max(i,j)
            vr=(1-i//m)*'sy'+(i//m)*'sx'
            if(m==1):
                lt+=[globals()[vr]]
            elif(m==2):
                lt+=[globals()[vr+str(m)],globals()[vr]**m]
            else:
                lt+=[globals()[vr+str(m)]]
                for e in range(1,m):
                    (i0,j0)=(1-i//m)*(0,m-e)+(i//m)*(m-e,0)
                    lt2=[]
                    lt2=sms(lt2,i0,j0,lg)
                    e1=1-(m-abs(1-e))//m
                    for f in lt2:
                        li=globals()[vr+e1*str(e)]*f
                        if not(li in lt):
                            lt+=[li]
        elif((i==1)|(j==1)):
            if(i==j):
                lt+=[sxy,sx*sy]
            else:
                m=max(i,j)
                for e in range(1+m):
                    if(e<2):
                        vxy='s'+((1+2*e-i//m)//(e+1))*'x'+((2*e+i//m)//(e+1))*'y'
                    else:
                        vxy=((1-i//m)*'sxy%i'+(i//m)*'sx%iy')%e
                    (i0,j0)=(1-i//m)*(0,m-e)+(i//m)*(m-e,0)
                    if(i0+j0==0):
                        lt+=[globals()[vxy]]
                    else:
                        lt2=[]
                        lt2=sms(lt2,i0,j0,lg)
                        for f in lt2:
                            li=globals()[vxy]*f
                            if not(li in lt):
                                lt+=[li]
        else:
            for sm in range(1,i+j+1):
                p=1-(sm-abs(1-sm))//sm
                for e in range(max(p,sm-j),min(sm-p,i)+1):
                    ex=e;ey=sm-e;M=max(ex,ey);m=min(ex,ey)
                    if(m==0):
                        if(ex==0):
                            lx=[]
                            lx=sms(lx,i,0,lg)
                        else:
                            ly=[]
                            ly=sms(ly,0,j,lg)
                            lt+=[p*q for q in ly for p in lx]
                    else:
                        u=(M-abs(1-M))//M;v=(m-abs(1-m))//m
                        vxy=v*((1-u)*(((1-ex//M)*'sxy%i'+(ex//M)*'sx%iy')%M)+u*'sxy')+(1-v)*('sx%iy%i'%(ex,ey))
                        #print(vxy)
                        if(sm==i+j):
                            lt+=[globals()[vxy]]
                        else:
                            lt2=[]
                            lt2=sms(lt2,i-ex,j-ey,lg)
                            if(min(i-ex,j-ey)>0):
                                lx=[];ly=[]
                                lx=sms(lx,i-ex,0,lg)
                                ly=sms(ly,0,j-ey,lg)
                                lt2+=[p*q for q in ly for p in lx]
                            for f in lt2:
                                li=f*globals()[vxy]
                                if not(li in lt):
                                    lt+=[li]
    return lt

def cmp(i,j):
    l=[]
    lu1=smu(l,i,0)
    lu2=smu(l,0,j)
    lm=smm(l,i,j)
    lt=sms(l,i,j,0)
    if(min(i,j)==0):
        r=len(lu1)+len(lu2)==len(lt)
    else:
        r=len(lu1)*len(lu2)+len(lm)==len(lt)
    return r

def cmp2(i,j,ope):
    if((not fls.idT(i,j))|ope):
        [c,l]=sgG(i,j)
        [c1,l1]=agrx(c,l)
        [c2,l2,f1,f2,f3]=grps(c1,l1)
        if(fls.idF(i,j)):
            [Fs,Fs2]=fls.lrF(i,j)
        else:
            Fs=coefs.sms([],i,j,0)
            Fs2=coefs.sms([],i,j,1); Fs2=[sp.expand(i)for i in Fs2]
            fls.grF(i,j,Fs,Fs2)
        T=frms2(c2,l2,Fs2)
        fls.grT(i,j,T,f1,f2,f3,c2)
    else:
        [T,f1,f2,f3,c]=fls.lrT(i,j)
    return smc(T,f1,f2,f3)

def gI(i,j):
    r=0
    if(fls.idI(i,j)):
        r=fls.lrI(i,j)
    else:
        r=IntCuad.intet3(i,j)
        r=IntCuad.frm2(r,i,j)
        fls.grI(i,j,r)
    return r

def sgG(i,j):
    if(fls.idG(i,j)):
        [c,l]=fls.lrG(i,j)
    else:
        fr1=gI(i,j)
        fr2=var(i,j)
        [c,l]=agr(fr1,fr2)
        fls.grG(i,j,c,l)
    return [c,l]

def tstagr(i,j):
    [c,l]=sgG(i,j)
    [c,l]=agrx(c,l) #;print( '\x1b[033m (%i,%i) \x1b[0m'%(i,j))
    r=[]
    if(not agrc2(l)):
        #print('\x1b[041m No esta bien agrupado (%i,%i) \x1b[0m'%(i,j))
        r=[i,j]
    return r

def tstagr2(i,j):
    f=gI(i,j)
    [c,l]=avance(f)
    [c,l]=agrx(c,l)
    r=[]
    if(not agrc2(l)):
        r=[i,j]
    return r

def tstagr3(i,j):
    r=[]
    f=gI(i,j)
    f2=var(i,j)
    [c,l]=agr(f,f2)
    [cg,lg]=sgG(i,j)
    if((c!=cg)|(lg!=l)):
        r=[i,j]
    return r

def tst():
    li=[]
    t0=tm.time(); t1=t0; g0=2; gf=14
    for g in range(g0,gf+1):
        for i in range(g+1):
            T=(gf+1)*(gf+2)//2; T0=g0*(g0+1)//2; Ti=(g-g0)*(g-g0+1)//2+(g-g0)*g0
            prnt.pbc3(Ti+i,T-T0,t0,t1); t0=t1
            r=tstagr(i,g-i)
            if(len(r)>0):
                li+=[r]
            t1=tm.time()
        prnt.pbc3(T-T0,T-T0,t0,t1)
    return li

def tst2(i,j):
    def mel(l):
        b=False
        x=[len(i.args)for i in l]
        if((max(x)==6)&(len(l)>6)):
            b=True
        return b
    I=gI(i,j)
    [_,l]=avance(I)
    cr=[];lr=[]
    for i in range(len(l)):
        if(mel(l[i])):
            lr+=[l[i]]
            cr+=[i]
    return [cr,lr]

def tst3(i,j):
    I=gI(i,j)
    [c,l]=avance(I)
    [_,lx]=agrx(c,l)
    le=[]
    for i in lx:
        if(len(i)==1):
            le+=[expg(i)]
    return le

def tst4():
    li=[]
    t0=tm.time(); t1=t0; g0=2; gf=10
    for g in range(g0,gf+1):
        for i in range(g+1):
            T=(gf+1)*(gf+2)//2; T0=g0*(g0+1)//2; Ti=(g-g0)*(g-g0+1)//2+(g-g0)*g0
            prnt.pbc3(Ti+i,T-T0,t0,t1); t0=t1
            r=tst3(i,g-i)
            if(len(r)>0):
                li+=[[i,g-i]]
            t1=tm.time()
    prnt.pbc3(T-T0,T-T0,t0,t1)
    return li

def tst5():
    li=[]
    t0=tm.time(); t1=t0; g0=11; gf=14
    for g in range(g0,gf+1):
        for i in range(g+1):
            T=(gf+1)*(gf+2)//2; T0=g0*(g0+1)//2; Ti=(g-g0)*(g-g0+1)//2+(g-g0)*g0
            prnt.pbc3(Ti+i,T-T0,t0,t1); t0=t1
            r=cmp2(i,g-i,False)
            if(r):
                li+=[[i,g-i]]
            t1=tm.time()
    prnt.pbc3(T-T0,T-T0,t0,t1)
    return li

def crrybrr(GI):
    def nm(GI,i,j,an):
        return GI+str(i)+an*'_'+str(j)+'.dc'
    #def brr(art,nrt):
    #    if(fls.xtF(art)):
    #        if(fls.xtF(nrt)):
    #            fls.brF(nrt)
    #        os.rename(art,nrt)
    def prD(aGI,nGI,art,nrt,GI):
        if(GI=='G'):
            ac='c'+aGI; nc='c'+nGI
            al='l'+aGI; nl='l'+nGI
            D=fls.lrD(nrt); c=D[ac]; l=D[al]
            D=dict(); locals()[nc]=c; locals()[nl]=l
            for i in [nc,nl]:
                D[i]=eval(i)
            fls.svD(nrt,D)
        elif(GI=='I'):
            aI='I'+aGI; nI='I'+nGI
            D=fls.lrD(art); I=D[aI]
            D=dict(); locals()[nI]=I
            for i in [nI]:
                D[i]=eval(i)
            fls.svD(nrt,D); fls.brF(art)
    dr='.\\memproc\\'; ls=os.listdir(dr); na=[]
    for i in ls:
        if(i[0]==GI):
            na+=[i]
    bf=[]
    for i in na:
        if('_'in list(i)):
            [n1,n2]=i[1:-3].split('_')
            ni=int(n1); nj=int(n2)
            aGI=nm(GI,ni,nj,0); nGI=nm(GI,ni,nj,1)
            art=dr+aGI; nrt=dr+nGI
            prD(aGI[1:-3],nGI[1:-3],art,nrt,GI)
        else:
            if(len(i)==7):
                t=list(i)[1:4]
                ni=int(t[0]); nj=int(''.join(t[1:]))
                i2=int(''.join(t[:2])); j2=int(t[2])
                nA=str(ni)+str(nj); nB=str(i2)+str(j2)
                a=(ni<15)&(nj<15); b=(i2<15)&(j2<15)
                if((a&b)&(nA==nB)):
                    if(fls.xtF(dr+GI+nA+'.dc')):
                        os.remove(dr+GI+nA+'.dc')
                        print('\x1b[031mRemovidos:\x1b[0m ',dr+GI+nA+'.dc')
                elif((a&(nA==i[1:4]))|(b&(i[1:4]==nB))):
                    if(a&(nA==i[1:4])):
                        aGI=nm(GI,ni,nj,0); nGI=nm(GI,ni,nj,1)
                        art=dr+aGI; nrt=dr+nGI
                        prD(aGI[1:-3],nGI[1:-3],art,nrt,GI)
                        #brr(art,nrt)
                    else:
                        aGI=nm(GI,i2,j2,0); nGI=nm(GI,i2,j2,1)
                        art=dr+aGI; nrt=dr+nGI
                        prD(aGI[1:-3],nGI[1:-3],art,nrt,GI)
                        #brr(art,nrt)
                    bf+=[aGI]
            else:
                t=list(i)[1:3]
                ni=int(t[0]); nj=int(t[1])
                aGI=nm(GI,ni,nj,0); nGI=nm(GI,ni,nj,1)
                art=dr+aGI; nrt=dr+nGI
                prD(aGI[1:-3],nGI[1:-3],art,nrt,GI)
                #brr(art,nrt)
                bf+=[aGI]
    return bf

def cmp3(i,j):
    r=[]
    if(fls.idT(i,j)):
        [T,f1,_,_]=fls.lrT(i,j)
        if(f1==0):
            r=[i,j]
    return r

def cmp4(i,j):
    r=[]
    if(fls.idG(i,j)):
        [c,l]=fls.lrG(i,j)
        me=expg(l[np.random.randint(len(l))])
        if ((not sum(np.ones(len(me)).astype(int)*(i+j)==sum(me.T))==len(me))|(sum(c)==0)):
            r=[i,j]
    return r

def cmp5(i,j):
    r=[]
    if(fls.idI(i,j)):
        I=fls.lrI(i,j)
        if( (sum(expg([I.args[np.random.randint(len(I.args))]])[0,:3])!=i)|(sum(expg([I.args[np.random.randint(len(I.args))]])[0,3:])!=j) ):
            r=[i,j]
    return r

def tst6():
    li=[]
    t0=tm.time(); t1=t0; g0=2; gf=12
    for g in range(g0,gf+1):
        for i in range(g+1):
            T=(gf+1)*(gf+2)//2; T0=g0*(g0+1)//2; Ti=(g-g0)*(g-g0+1)//2+(g-g0)*g0
            prnt.pbc3(Ti+i,T-T0,t0,t1); t0=t1
            r=cmp3(i,g-i)
            if(len(r)>0):
                li+=[r]
            t1=tm.time()
    prnt.pbc3(T-T0,T-T0,t0,t1)
    return li