import sympy as sp
#import scipy.special as ss
import math as mt
x,y=sp.symbols('x,y')#,x1,x2,x3,y1,y2,y3,A,sx,sx2,sx3,sx4,sy,sy2,sy3,sy4,sxy,sx2y,sxy2,sx2y2,sx3y,sxy3,px,py
for i in range(3):
    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
    globals()['y%i'%(i+1)]=sp.symbols('y%i'%(i+1))
A=(x1*y2-x1*y3+y3*x2-y1*x2+y1*x3-y2*x3)/2

#sx=x1+x2+x3
#sx2=x1**2+x2**2+x3**2
#sx3=x1**3+x2**3+x3**3
#sx4=x1**4+x2**4+x3**4
#sx5=x1**5+x2**5+x3**5
#sx6=x1**6+x2**6+x3**6
#sx7=x1**7+x2**7+x3**7
#sx8=x1**8+x2**8+x3**8;
#sy=y1+y2+y3
#sxy=x1*y1+x2*y2+x3*y3
#sx2y=x1**2*y1+x2**2*y2+x3**2*y3
#sx3y=x1**3*y1+x2**3*y2+x3**3*y3
#sx4y=x1**4*y1+x2**4*y2+x3**4*y3
#sx5y=x1**5*y1+x2**5*y2+x3**5*y3
#sx6y=x1**6*y1+x2**6*y2+x3**6*y3
#sx7y=x1**7*y1+x2**7*y2+x3**7*y3;
#sy2=y1**2+y2**2+y3**2
#sxy2=x1*y1**2+x2*y2**2+x3*y3**2
#sx2y2=x1**2*y1**2+x2**2*y2**2+x3**2*y3**2
#sx3y2=x1**3*y1**2+x2**3*y2**2+x3**3*y3**2
#sx4y2=x1**4*y1**2+x2**4*y2**2+x3**4*y3**2
#sx5y2=x1**5*y1**2+x2**5*y2**2+x3**5*y3**2
#sx6y2=x1**6*y1**2+x2**6*y2**2+x3**6*y3**2;
#sy3=y1**3+y2**3+y3**3
#sxy3=x1*y1**3+x2*y2**3+x3*y3**3
#sx2y3=x1**2*y1**3+x2**2*y2**3+x3**2*y3**3
#sx3y3=x1**3*y1**3+x2**3*y2**3+x3**3*y3**3
#sx4y3=x1**4*y1**3+x2**4*y2**3+x3**4*y3**3
#sx5y3=x1**5*y1**3+x2**5*y2**3+x3**5*y3**3;
#sy4=y1**4+y2**4+y3**4
#sxy4=x1*y1**4+x2*y2**4+x3*y3**4
#sx2y4=x1**2*y1**4+x2**2*y2**4+x3**2*y3**4
#sx3y4=x1**3*y1**4+x2**3*y2**4+x3**3*y3**4
#sx4y4=x1**4*y1**4+x2**4*y2**4+x3**4*y3**4;
#sy5=y1**5+y2**5+y3**5
#sxy5=x1*y1**5+x2*y2**5+x3*y3**5
#sx2y5=x1**2*y1**5+x2**2*y2**5+x3**2*y3**5
#sx3y5=x1**3*y1**5+x2**3*y2**5+x3**3*y3**5
#sy6=y1**6+y2**6+y3**6
#sxy6=x1*y1**6+x2*y2**6+x3*y3**6;
#sx2y6=x1**2*y1**6+x2**2*y2**6+x3**2*y3**6
#sy7=y1**7+y2**7+y3**7
#sxy7=x1*y1**7+x2*y2**7+x3*y3**7
#sy8=y1**8+y2**8+y3**8;
#px=x1*x2*x3;py=y1*y2*y3
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
                    print(globals()['sx%iy%i'%(i,j)])

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

def mtbl(gx,gy):
    r=0
    #dfvr(gx,gy)
    smdf(gx,gy)
    if(gx==0):
        if(gy==0):
            r=1
        elif(gy==1):
            r=sy
        elif(gy==2):
            r=sy2+sy**2
        elif(gy==3):
            r=2*sy3+sy**3+3*sy*sy2
    elif(gx==1):
        if(gy==0):
            r=sx
        elif(gy==1):
            r=sxy+sx*sy
        elif(gy==2):
            r=sx*sy2+sx*sy**2+2*sxy*sy+2*sxy2
    elif(gx==2):
        if(gy==0):
            r=sx2+sx**2
        elif(gy==1):
            r=sy*sx2+sx**2*sy+2*sxy*sx+2*sx2y
    elif(gx==3):
        if(gy==0):
            r=2*sx3+sx**3+3*sx*sx2
    return r

def table(gx,gy):
    dfvr(gx,gy)
    I=0
    if(gx==0):
        if(gy==0):
            I=A
        if(gy==1):
            I=A/3*sy
        if(gy==2):
            I=A/12*(sy2+sy**2)
        if(gy==3):
            I=A/60*(2*sy3+sy*(sy**2+3*sy2))
        elif(gy==4):
            I=A/30*(sy4+sy2*sy**2)
    elif(gx==1):
        if(gy==0):
            I=A/3*sx
        if(gy==1):
            I=A/12*(sxy+sx*sy)
        if(gy==2):
            I=A/60*(sx*(sy2+sy**2)+2*sxy*sy+2*sxy2)
        elif(gy==3):
            I=A/60*(2*sxy3+sxy*sy2+sx*sy2*sy)
    elif(gx==2):
        if(gy==0):
            I=A/12*(sx2+sx**2)
        if(gy==1):
            I=A/60*(sy*(sx2+sx**2)+2*sxy*sx+2*sx2y)
        elif(gy==2):
            I=A/180*(2*sxy**2+4*sx2y*sy+4*sxy2*sx+sx2*sy2+sx**2*sy**2)
    elif(gx==3):
        if(gy==0):
            I=A/60*(2*sx3+sx*(sx**2+3*sx2))
        if(gy==1):
            I=A/60*(2*sx3y+sxy*sx**2+sx*sx2*sy)
        elif(gy==2):
            I=A/840*((sx**3+sx3)*(sy**2+sy2)+2*(sx3-sx*sx2)*sy2+6*sx2y*(sx*sy+sxy)+2*sxy*(sx*sxy+sx2*sy)+12*sx*sx2y2+6*sx2*sxy2+4*sx3y*sy-2*sx3y2)#5
        elif(gy==3):
            I=A/5040*( sx**3*(sy**3+sy3)+(sx**3+sx3)*sy**3+9*sxy2*(3*sx2y+sx**2*sy)+9*sx2y*(2*sxy2+sy**2*sx)+5*sx3*sy3+54*sx2y2*sxy+54*sx3y2*sy+54*sx*sx2y3+18*sx3y*sy2+18*sx2*sxy3-90*sx3y3) #6
    elif(gx==4):
        if(gy==0):
            I=A/30*(sx4+sx2*sx**2)
        elif(gy==1):
            I=A/210*(4*sx4y+2*sx*(sxy*sx2+sx2y*sx)+sy*(sx2*sx**2+sx4))#5
        elif(gy==2):
            I=A/2520*( -3*sx4y2+sx**4*sy**2+sx3*sx*sy**2+6*sx2y*sx2*sy+12*sx2y*sx*sxy+sx4*sy**2+sx3*sx*sy2+2*sx3*sxy*sy+14*sx3y*sx*sy+2*sxy2*sx**3+6*sx2y2*sx**2+3*sx2y**2+10*sx3y2*sx+2*sx4*sy2+10*sx3y*sxy+8*sx3*sxy2+12*sx2y2*sx2+2*sx4y*sy ) #6
    #nuevo
    elif(gx==5):
        if(gy==0):
            I=A/42*(2*sx5+sx*(sx*sx3-sx4)+sx2*(sx*sx2-sx3))#5
        elif(gy==1):
            I=A/5040*( -36*sx5y+2*sx**5*sy+18*sx4*sx*sy+9*sx3*sx2*sy+18*sx3*sx*sxy+sx**2*sx3*sy+10*sx**3*sx2y+9*sx**2*sx3y+54*sx4y*sx+12*sx4*sxy+51*sx3y*sx2+32*sx2y*sx3 ) #6
    elif(gx==6):
        if(gy==0):
            I=A/2520*( 9*sx6+sx**6+27*sx4*sx**2+27*sx3*sx2*sx+sx3*sx**3+7*sx3**2+18*sx4*sx2 )#6
    #dfvr(gx,gy)
    return I

def cmb(x,y):
    r=0
    if((x%1==0)&(y%1==0)&(y>=0)&(x>=y)):
        n=x
        if(2*y>=n):
            m=n-y
        else:
            m=y
        D=1;d=1
        for i in range(m):
            D*=n-i
            d*=i+1
        r=D//d
    return r

def intet1(gx,gy):
    r=0
    if((gx>=0)&(gy>=0)):#&(len(p1)==len(p2))&(len(p1)==3)
        for h in range(gx+1):
            for i in range(gy+1):
                for j in range(h+1):
                    for k in range(i+1):
                        D=1;d=1
                        for l in range(j+k+1):
                            d*=h+i-j-k+1+l
                            if(l<j+k-1):
                                D*=j+k-l
                        r+=cmb(gx,h)*cmb(gy,i)*cmb(h,j)*cmb(i,k)*x3**(gx-h)*y3**(gy-i)*(x1-x3)**(h-j)*(y1-y3)**(i-k)*(x2-x3)**j*(y2-y3)**k*D/d
    return r

def intet2(gx,gy):
    r=0
    if((gx>=0)&(gy>=0)):
        c=mt.factorial(gx)*mt.factorial(gy)/mt.factorial(gx+gy+2)
        for k in range(gx+1):
            for l in range(gx+1-k):
                r0=((k+l)%2)*(-1)*(x2-x3)**k/(y2-y3)**(k+1)*cmb(gx+gy+2,gy+k+l+2)
                r+=r0*((x1-x3)**l/(y1-y3)**(l+1)*x3**(gx-k-l)*y3**(gy+k+l+2)-(x1-x2)**l/(y1-y2)**(l+1)*x2**(gx-k-l)*y2**(gy+k+l+2)+((x1-x2)**l/(y1-y2)**(l+1)-(x1-x3)**l/(y1-y3)**(l+1))*x1**(gx-k-l)*y1**(gy+k+l+2))
    return r

def intet3(gx,gy):
    r=0
    if((gx>=0)&(gy>=0)):
        for h in range(gx+1):
            for i in range(gy+1):
                for j in range(h+1):
                    for k in range(i+1):
                        D=mt.factorial(i+h-j-k)*mt.factorial(j+k)*x
                        d=mt.factorial(gx-h)*mt.factorial(h-j)*mt.factorial(j)*mt.factorial(gy-i)*mt.factorial(i-k)*mt.factorial(k)*mt.factorial(i+h+2)
                        #print("%i\t%i\t%i\t%i\t%i-%i\n"%(h,i,j,k,D,d))
                        r+=D/d*x3**(gx-h)*y3**(gy-i)*(x1-x3)**(h-j)*(x2-x3)**j*(y1-y3)**(i-k)*(y2-y3)**k
        r*=mt.factorial(gx)*mt.factorial(gy)/x
    return r

def cf(fml):
    cp=fml.subs({x1:1,x2:0,x3:0,y1:0,y2:1,y3:0})
    return cp

def cf2(gx,gy):
    cf=x*mt.factorial(gx)*mt.factorial(gy)/mt.factorial(gx+gy+2)
    return cf/x

def frm(fml):
    tst=sp.factor(fml)
    c=cf(tst)
    return tst/c

def frm2(fml,gx,gy):
    tst=sp.factor(fml)
    c=cf2(gx,gy)
    return tst/c

def frm3(fml):
    return sp.expand(fml)

def correcto(gx,gy):
    r=False
    if((gx>=0)&(gy>=0)):
        tst=frm(table(gx,gy)/A)
        tst2=frm2(intet3(gx,gy),gx,gy)
        r=tst==tst2
    return r

def correcto2(fml,fml2,gx,gy):#fml: integracion real, fml2: formula para comparar
    tst2=frm2(fml,gx,gy)
    tst=frm(fml2)
    r=tst==tst2
    return r

def correcto3(gx,gy):
    f1=frm(sp.expand(mtbl(gx,gy)))
    f2=frm2(intet3(gx,gy),gx,gy)
    return f1==f2

def correcto4(fml,fml2):
    c=cf(fml2)
    return fml2/c==fml

def intT(gx,gy,i):
    r=0
    I=table(gx,gy)
    if(i==3):
        r=I.subs({x1:1,x2:0,x3:0,y1:0,y2:1,y3:0})
    elif(i==1):
        r=I.subs({x1:1,x2:1,x3:0,y1:0,y2:1,y3:1})
    elif(i==2):
        r=I.subs({x1:2,x2:1,x3:1,y1:1,y2:2,y3:1})
    elif(i==6):
        r=I.subs({x1:2,x2:2,x3:1,y1:1,y2:2,y3:2})
    return r

def dFr(i,j,frm):
    dfvr(i,j)
    k=list(frm.as_coefficients_dict().keys())
    v=list(frm.as_coefficients_dict().values())
    r=sp.expand(frm)
    return r