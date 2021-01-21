import numpy as np
import sympy as sp
import json as js
import os
import time as tm
#Primer imprimir matriz
def pM(A):
    [f,c]=A.shape
    for i in range(f):
        print('|',end='\t')
        for j in range(c):
            print(A[i,j],end='\t')
        print('|')

#Imprime matriz, minimo espacio
def pM2(A):
    [f,c]=A.shape
    At=np.zeros((f,c)).astype(int)
    ci=np.zeros((1,c)).astype(int)
    for i in range(f):
        for j in range(c):
            At[i,j]=len(str(A[i,j]))
    for i in range(c):
        ci[0,i]=np.max(At[:,i])
    for i in range(f):
        spr=', '
        e=' '
        for j in range(c):
            eij=str(A[i,j])
            t=ci[0,j]-len(eij)
            dr=t//2;iz=t-dr
            if j==c-1:
                sgt='\n'
            else:
                sgt=spr
            print(iz*e+eij+dr*e,end=sgt)

#Primera table
def Tbls(A,b,ZC):
    [f,c]=A.shape
    T=np.zeros((f+1,c+1)).astype(int)
    T[:f,:c]=A
    T[:f,c]=b
    T[f,:c]=ZC
    pM2(T)

#Imprime texto "txt" del color "c 30,31,...40,41,..."
def clt(txt,c):
    return '\x1b[%im%s\x1b[0m'%(c,txt)

#Imprime el inicio o fin de la tabla con "c" columnas, de una tabla formateada
def hif(v,c,l,i):
    e1=js.loads('"\\u2554"');e2=js.loads('"\\u2557"');e3=js.loads('"\\u255a"');e4=js.loads('"\\u255d"')
    h1=js.loads('"\\u2566"');h2=js.loads('"\\u2569"');h3=js.loads('"\\u2564"');h4=js.loads('"\\u2567"');h5=js.loads('"\\u2550"');h6=js.loads('"\\u2500"')
    print((1-i)*e1+i*e3,end='')
    for j in range(c+3):
        print(h5*v[j],end='')
        if(j==0):
            print(h5,end='')
        elif(j in l):
            print((1-i)*h3+i*h4,end='')
        elif(j<c+2):
            print((1-i)*h1+i*h2,end='')
    print((1-i)*e2+i*e4)

#Imprime una tabla, A:matriz de coeficientes de las variables,b:costos,Bb:Base,C:coef funcion objetivo, coloreada la fila fi y columna cj pivote
def Tbl(A,b,Bb,Z,C,fi,cj):
    [f,c]=A.shape
    T=sp.zeros(f+4,c+3)
    T[2:f+2,2:c+2]=A
    T[1,2:c+3]=C
    T[f+2,2:c+3]=Z
    T[f+3,2:c+3]=Z-C
    T[2:f+2,c+2]=b
    l=[]
    for i in range(c):
    #    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
        l+=['x%i'%(i+1)]
        T[0,2+i]=str(l[i])
    T[2:f+2,0]=C[0,Bb].T
    T[2:f+2,1]=np.array(l)[Bb]
    v1=js.loads('"\\u2560"');v2=js.loads('"\\u2563"');v3=js.loads('"\\u255f"');v4=js.loads('"\\u2562"');v5=js.loads('"\\u2551"');v6=js.loads('"\\u2502"')
    h1=js.loads('"\\u2566"');h2=js.loads('"\\u2569"');h3=js.loads('"\\u2564"');h4=js.loads('"\\u2567"');h5=js.loads('"\\u2550"');h6=js.loads('"\\u2500"')
    c1=js.loads('"\\u256c"');c2=js.loads('"\\u253c"');c3=js.loads('"\\u256b"');c4=js.loads('"\\u256a"')
    At=np.zeros((f+4,c+3)).astype(int)
    ci=np.zeros((1,c+3)).astype(int)
    for i in range(f+4):
        for j in range(c+3):
            At[i,j]=len(str(T[i,j]))
    for i in range(c+3):
        ci[0,i]=np.max(At[:,i])
    #lf=list(set(range(f+4))-{1,f+1})
    lc=list(set(range(c+3))-{1,c-len(Bb)+1,c+1,c+2})
    hif(ci[0,:],c,lc,0)
    for i in range(f+4):#f+4):
        print(v5,end='')
        if(i<f+4):
            if(i<2):
                h=0
            else:
                h=1
            k=0
            if(i==f+1):
                k=1
            l=0
            if((i==f+2)|(i==f+3)):
                l=1
            for j in range(c+3):
                eij=str(T[i,j])
                t=ci[0,j]-len(eij)
                dr=t//2;iz=t-dr
                e=' '
                if(j<2):
                    if(l==0):
                        print((1-h)*ci[0,j]*e+h*(iz*e+eij+dr*e),end='')
                    else:
                        if(j==1):
                            t=ci[0,j-1]+ci[0,j]+1
                            if(i==f+2):
                                tt='Z'
                            else:
                                tt='Z-C'
                            t-=len(tt)
                            dr2=t//2;iz2=t-dr2
                            print(iz2*e+tt+dr2*e,end='')
                else:
                    if(j==cj+2):
                        if(i==fi+2):
                            print(iz*e+'\x1b[%im%s\x1b[0m'%(47,eij)+dr*e,end='')
                        else:
                            print(iz*e+'\x1b[46m%s\x1b[0m'%eij+dr*e,end='')
                    else:
                        if(i==fi+2):
                            print(iz*e+'\x1b[%im%s\x1b[0m'%(45,eij)+dr*e,end='')
                        else:
                            print(iz*e+eij+dr*e,end='')
                if(j==0):
                    print((1-l)*((1-h)*e+h*v6)+l*'',end='')
                elif(j in lc):
                    print(v6,end='')
                else:
                    print(v5,end='')
            print('')
            if(i<f+3):
                ii=i
                if((i==1)|(i==f+1)):
                    ii=1
                if(i==f+1):
                    h=0
                print( (1-h)*((1-ii)*v5+ii*v1)+h*v3,end='')
                for j in range(c+3):
                    fx=(f+2-abs(1-ii))//(f+2)
                    if(j<2):
                        print( ci[0,j]*((1-k)*((1-h)*((1-i)*e+i*h5)+h*h6)+k*h5) ,end='')
                    else:
                        print(ci[0,j]*((1-fx)*h6+fx*h5),end='')

                    if(j==0):
                        print((1-l)*((1-k)*((1-h)*((1-i)*e+i*h3)+h*c2)+k*h4)+l*h6,end='')
                    elif(j==1):
                        print((1-l)*((1-k)*((1-h)*((1-i)*v3+i*c1)+h*c3)+k*c1)+l*c3,end='')
                    elif(j in lc):
                        print((1-fx)*c2+fx*c4,end='')
                    elif(j==c+2):
                        print((1-fx)*v4+fx*v2,end='')
                    else:
                        print((1-fx)*c3+fx*c1,end='')
                print('')
    hif(ci[0,:],c,lc,1)

#Imprime resultados
def Tbr(X,Xr,fo):
    l1=len(X)
    l2=len(Xr)
    if((l1==l2)&(l1>0)):
        v1=js.loads('"\\u2560"');v2=js.loads('"\\u2563"');v3=js.loads('"\\u255f"');v4=js.loads('"\\u2562"');v5=js.loads('"\\u2551"');v6=js.loads('"\\u2502"')
        h1=js.loads('"\\u2566"');h2=js.loads('"\\u2569"');h3=js.loads('"\\u2564"');h4=js.loads('"\\u2567"');h5=js.loads('"\\u2550"');h6=js.loads('"\\u2500"')
        c1=js.loads('"\\u256c"');c2=js.loads('"\\u253c"');c3=js.loads('"\\u256b"');c4=js.loads('"\\u256a"')
        e=' '
        def hif(vl,i):
            e1=js.loads('"\\u2554"');e2=js.loads('"\\u2557"');e3=js.loads('"\\u255a"');e4=js.loads('"\\u255d"')
            h1=js.loads('"\\u2566"');h2=js.loads('"\\u2569"');h3=js.loads('"\\u2564"');h4=js.loads('"\\u2567"');h5=js.loads('"\\u2550"');h6=js.loads('"\\u2500"')
            print((1-i)*e1+i*e3,end='')
            for j in range(len(vl)):
                print(vl[j]*h5,end='')
                j1=(1-abs(j-1))
                if(j<len(vl)-1):
                    print(((1-i)*h3+i*h4)*(1-j1)+j1*((1-i)*h1+i*h2),end='')
            print((1-i)*e2+i*e4)
            return 0
        C1=np.ones((1,l1)).astype(int)
        C2=np.ones((1,l2)).astype(int)
        zr=str(fo)
        #print(Xr,end='\t');print(X)
        for i in range(l1):
            #print('Xr[i]',end='\t');print(Xr[i],end='\t');print('str(Xr[i])',end='\t');print(str(Xr[i]));print('len(str(Xr[i]))',end='\t');print(len(str(Xr[i])))
            C1[0,i]=len(str(X[i]))
            C2[0,i]=len(str(Xr[i]))
        vl=np.array([np.max(C1),np.max(C2),len(zr)])
        Hd1='X_i';Hd2='Valor';Hd3='VFO'
        vl[0]=max(3,vl[0]);vl[1]=max(5,vl[1]);vl[2]=max(3,vl[2])
        hif(vl,0)
        hlf=l1//2+l1%2#=(l1+1)//2
        for i in range(l1+1):
            if(i==0):
                cnt=np.array([Hd1,Hd2,Hd3])
            else:
                cnt=np.array([str(X[i-1]),str(Xr[i-1]),zr])
            print(v5,end='')
            t=vl[2]-len(zr)
            iz=t-t//2;dr=t-iz
            zr=iz*e+zr+dr*e
            lh=(l1-abs(hlf-i))//l1
            for j in range(3):
                t=vl[j]-len(cnt[j])
                iz=t-t//2;dr=t-iz
                h=(l1-i)//l1+(1-(l1-i)//l1)*(1-j//2)# (1-r)*e*vl+r*( (1-hl)*e*vl+hl*zr )=e*vl( 1-r +r*(1-hl))+r*hl*zr
                print(h*(iz*e+cnt[j]+dr*e)+(1-h)*( e*vl[j]*(1-(l1%2)*lh)+(l1%2)*lh*zr ),end='')
                h=(2-j)//2
                print(h*v6+(1-h)*v5,end='')
            print('')
            fx=(l1-i)//l1
            if(i<l1):
                print(((1-fx)*v3+fx*v1),end='')
                for j in range(3):
                    print((1-fx)*(vl[j]*(1-j//2)*h6+(j//2)*(vl[j]*(1-lh)*e+lh*((1-l1%2)*zr+(l1%2)*vl[j]*e)))+vl[j]*fx*h5,end='')
                    if(j<2):
                        print((1-j)*((1-fx)*c2+fx*c4)+j*((1-fx)*v4+fx*c1),end='')
                print((1-fx)*v5+fx*v2)
        hif(vl,1)
    return 0

def ctp(smh):
    return str(smh[0])+' horas, '+str(smh[1])+' min, '+str(smh[2])+' seg'

def eb(e):
    return e*'.'

def spb(p):
    return p*'='

def ct(t):
    return '\x1b[033m%s\x1b[0m'%t

def pb(i,N,W):
    r=''
    if((i>=0)&(i in range(N+1))&(W>10)):
        pr=str(100*i//N)+'%'
        w=W-7
        ip=w*i//N;ib=w-ip
        r=ct(spb(ip))+'|'+eb(ib)+'| '+ct(pr)
    return r

def pb2(i,N,W,ctp):
    pr='|'+str(100*i//N)+'%'; w=W-5;l=len(ctp)
    p0=(w-l)//2
    ip=w*i//N
    if(ip==0):
        r=eb(p0-1)+ctp+eb(w-l-p0+1)+ct(pr)
    elif((ip>0)&(ip<=p0-1)):
        r=ct(spb(ip-1))+ct('|')+eb(p0-1-ip)+ctp+eb(w-l-p0+1)+ct(pr)
    elif((ip>p0-1)&(ip<p0+l)):
        r=ct(spb(p0-1))+ct(ctp[:(ip+1-p0)])+ctp[ip+1-p0:]+eb(w-l-p0+1)+ct(pr)
    elif((ip>=p0+l)&(ip<w)):
        r=ct(spb(p0-1))+ct(ctp)+ct(eb(ip-p0-l))+ct('|')+eb(w-ip)+ct(pr)
    elif(ip==w):
        r=ct(spb(p0-1))+ct(ctp)+ct(eb(ip-l-p0+1))+ct(pr)
    return r

def pbc(i,N):
    def br(b):
        return b*'\u0008'
    if((i>=0)&(i in range(N+1))):
        W=os.get_terminal_size()[0]
        if(i==0):
            print(pb(i,N,W),end=br(W))
        else:
            print('\r',end='')
            print(pb(i,N,W),end=br(W))
    tm.sleep(0.4)

def pbc2(i,N,smh):
    t=ctp(smh); lt=len(t); W=os.get_terminal_size()[0]
    if((i>=0)&(i in range(N+1))&(W>10)&(len(smh)==3)&(lt<W-7)):
        t=ctp(smh);lt=len(t)
        if(i==0):
            print(pb2(i,N,W,t),end='\r')
        else:
            print('\r',end='')
            print(pb2(i,N,W,t),end='\r')

def clct(i,N,t1,t2):
    r=0
    if((t1<t2)&(i<N)&(i>0)):
        r=(t2-t1)*(N-i)
    return r

def pbc3(i,N,t1,t2):
    r=clct(i,N,t1,t2)
    lt=list(tm.gmtime(r)[3:6])
    pbc2(i,N,lt)

def tst():
    t0=tm.time()
    t1=t0
    W=os.get_terminal_size()[0]
    i=0
    while(i<W):
        t2=list(tm.gmtime(clct(i,W,t0,t1))[3:6])
        pbc2(i,W,t2);tm.sleep(1.0)
        t0=t1;t1=tm.time()
        i+=1
    pbc2(W,W,list(tm.gmtime(t1-t0)[3:6]))