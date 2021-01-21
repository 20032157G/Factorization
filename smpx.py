import sympy as sp
import numpy as np
import json as js
import prnt
import fls
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x,N=sp.symbols('x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x,N')
rt='.\\memproc\\tmp.bd'
rt2='.\\memproc\\dc.bd'
#n=3

#Ejemplo x^8, tipo 1
def ej1_0():
    f=11;c=14
    M=sp.zeros(f,c)
    M[0,0]=2;M[0,4]=12;M[0,6]=6;M[0,7]=20;M[0,13]=N
    M[1,1]=1;M[1,4]=12;M[1,6]=3;M[1,7]=30;M[1,13]=N
    M[2,2]=2;M[2,4]=6;M[2,7]=30;M[2,13]=N
    M[3,3]=1;M[3,4]=4;M[3,7]=25;M[3,13]=N
    M[4,5]=2;M[4,7]=20;M[4,13]=N
    M[5,0]=2;M[5,1]=1;M[5,3]=1;M[5,4]=4;M[5,6]=3;M[5,7]=5;M[5,8]=1;M[5,13]=N
    M[6,0]=1;M[6,1]=1;M[6,2]=2;M[6,4]=6;M[6,5]=1;M[6,6]=3;M[6,7]=10;M[6,9]=1;M[6,13]=N
    M[7,1]=1;M[7,3]=1;M[7,4]=4;M[7,5]=2;M[7,6]=1;M[7,7]=11;M[7,10]=1;M[7,13]=N
    M[8,2]=2;M[8,3]=2;M[8,4]=2;M[8,7]=10;M[8,11]=1;M[8,13]=N
    M[9,0]=2;M[9,1]=2;M[9,2]=3;M[9,3]=3;M[9,4]=15;M[9,5]=2;M[9,6]=6;M[9,7]=35;M[9,12]=-1;M[9,13]=3*N
    M[10,4]=-42;M[10,6]=-6;M[10,7]=-185;M[10,13]=11*N/2
    return M

#Ejemplo x^8, tipo 2
def ej1_2():
    f=10;c=14
    M=sp.zeros(f,c)
    M[:9,13]=N*sp.ones(9,1)
    M[0,0]=8;M[0,1]=2;M[0,2]=1;M[0,4]=1;M[0,5]=4;M[0,7]=3;M[0,8]=5;M[0,9]=1
    M[1,0]=28;M[1,1]=1;M[1,2]=1;M[1,3]=2;M[1,5]=6;M[1,6]=1;M[1,7]=3;M[1,8]=10;M[1,10]=1
    M[2,0]=56;M[2,2]=1;M[2,4]=1;M[2,5]=4;M[2,6]=2;M[2,7]=1;M[2,8]=11;M[2,11]=1
    M[3,0]=70;M[3,3]=2;M[3,4]=2;M[3,5]=2;M[3,8]=10;M[3,12]=1
    M[4,0]=56;M[4,1]=2;M[4,5]=12;M[4,7]=6;M[4,8]=20
    M[5,0]=168;M[5,2]=1;M[5,5]=12;M[5,7]=3;M[5,8]=30
    M[6,0]=420;M[6,3]=2;M[6,5]=6;M[6,8]=30
    M[7,0]=280;M[7,4]=1;M[7,5]=4;M[7,8]=25
    M[8,0]=672;M[8,6]=2;M[8,8]=20
    M[9,0]=-161;M[9,1]=-2;M[9,2]=-2;M[9,3]=-3;M[9,4]=-3;M[9,5]=-15;M[9,6]=-2;M[9,7]=-6;M[9,8]=-35;M[9,13]=-3*N
    return M

#Acomodando los datos del ejemplo x^8
def ej1_3():
    f=15;c=24
    M=sp.zeros(f,c)
    Mt=ej1_2()
    M[:4,:9]=Mt[:4,:9]
    M[f-1,:9]=Mt[9,:9]
    M[:4,c-1]=Mt[:4,13]
    M[f-1,c-1]=Mt[9,13]
    for i in range(5):
        M[4+2*i,:9]=Mt[4+i,:9]
        M[4+2*i+1,:9]=Mt[4+i,:9]
        M[4+2*i,c-1]=Mt[4+i,13]
        M[4+2*i+1,c-1]=Mt[4+i,13]
        M[4+2*i+1,:]*=-1
    M[:f-1,9:c-1]=sp.eye(14)
    return M

#Ejemplo x^6
def ej2():
    f=7;c=10
    M=sp.zeros(f,c)
    M[:6,9]=N*sp.ones(6,1)
    M[0,0]=1;M[0,1]=2;M[0,3]=2;M[0,5]=3;M[0,6]=6;M[0,7]=1
    M[1,0]=1;M[1,1]=1;M[1,3]=3;M[1,4]=3;M[1,5]=3;M[1,6]=15;M[1,8]=1
    #M[2,0]=1;M[2,1]=2;M[2,2]=-1;M[2,3]=4;M[2,4]=2;M[2,5]=5;M[2,6]=20;M[2,9]=-1
    M[2,0]=1;M[2,3]=4;M[2,5]=3;M[2,6]=60
    M[3,1]=2;M[3,3]=2;M[3,5]=6;M[3,6]=30
    M[4,0]=2;M[4,2]=2;M[4,3]=4;M[4,5]=2;M[4,6]=20
    M[5,3]=6;M[5,4]=6;M[5,6]=90
    M[6,0]=-1;M[6,1]=-2;M[6,2]=1;M[6,3]=-4;M[6,4]=-2;M[6,5]=-5;M[6,6]=-20;M[6,9]=-N
    return M

#Adaptar el ejemplo x^6
def ej2_2():
    Mt=ej2()
    f=11;c=18
    M=sp.zeros(f,c)
    M[:2,:7]=Mt[:2,:7]
    M[f-1,:7]=Mt[6,:7]
    M[:2,c-1]=Mt[:2,9]
    M[f-1,c-1]=Mt[6,9]
    for i in range(4):
        M[2+2*i,:7]=Mt[2+i,:7]
        M[2+2*i+1,:7]=Mt[2+i,:7]
        M[2+2*i,c-1]=Mt[2+i,9]
        M[2+2*i+1,c-1]=Mt[2+i,9]
        M[2+2*i+1,:]*=-1
    M[:f-1,7:c-1]=sp.eye(10)
    return M

#Ejemplo x^ y^
def ej3():
    f=12;c=15
    M=sp.zeros(f,c)
    M[0,0]=3;M[0,1]=2;M[0,3]=1;M[0,5]=2;M[0,6]=1;M[0,7]=2;M[0,8]=1;M[0,9]=1;M[0,14]=6*N
    M[1,0]=6;M[1,1]=2;M[1,2]=1;M[1,3]=1;M[1,7]=3;M[1,8]=2;M[1,10]=1;M[1,14]=6*N
    M[2,0]=2;M[2,2]=1;M[2,3]=1;M[2,4]=2;M[2,7]=1;M[2,8]=2;M[2,11]=1;M[2,14]=4*N
    M[3,0]=3;M[3,2]=1;M[3,5]=1;M[3,6]=1;M[3,7]=1;M[3,8]=1;M[3,12]=1;M[3,14]=3*N
    M[4,0]=1;M[4,4]=1;M[4,6]=1;M[4,8]=1;M[4,13]=1;M[4,14]=N
    M[5,0]=12;M[5,1]=2;M[5,7]=2;M[5,14]=4*N
    M[6,0]=6;M[6,5]=2;M[6,7]=2;M[6,14]=3*N
    M[7,0]=6;M[7,3]=1;M[7,7]=2;M[7,8]=2;M[7,14]=3*N
    M[8,0]=6;M[8,2]=1;M[8,7]=1;M[8,8]=2;M[8,14]=2*N
    M[9,0]=2;M[9,4]=2;M[9,8]=2;M[9,14]=N
    M[10,0]=3;M[10,6]=1;M[10,8]=1;M[10,14]=N
    M[11,0]=-14;M[11,1]=-2;M[11,2]=-2;M[11,3]=-2;M[11,4]=-2;M[11,5]=-2;M[11,6]=-2;M[11,7]=-6;M[11,8]=-6;M[11,14]=-10*N
    return M

#Adaptando el ejemplo x^y^
def ej3_2():
    f=18;c=27
    M=sp.zeros(f,c)
    Mt=ej3()
    M[:5,:9]=Mt[:5,:9]
    M[f-1,:9]=Mt[11,:9]
    M[:5,c-1]=Mt[:5,14]
    M[f-1,c-1]=Mt[11,14]
    M[:f-1,9:c-1]=sp.eye(17)
    for i in range(6):
        M[5+2*i,:9]=Mt[5+i,:9]
        M[5+2*i+1,:9]=Mt[5+i,:9]
        M[5+2*i,c-1]=Mt[5+i,14]
        M[5+2*i+1,c-1]=Mt[5+i,14]
        M[5+2*i+1,:]*=-1
    return M

def ini(i):
    if(i==1):
        M=ej1_3()
        M0=ej1_3()
    elif(i==2):
        M=ej2_2()
        M0=ej2_2()
    elif(i==3):
        M=ej3_2()
        M0=ej3_2()
    return [M,M0]

#[M,M0]=ini(n);[f,c]=M.shape

def ngt(M):
    [f,c]=M.shape
    ng=0
    for i in range(c-1):
        if(M[f-1,i]<0):
            ng+=1
    return ng

#Operacion elemental volver ceros a la columna pivote excepto el elemento pivote
def ope(M,i,j):
    [f,c]=M.shape
    m=M
    if (( i in range(f-1))&(j in range(c-1))):
        if(m[i,j]!=0):
            m[i,:]/=m[i,j]
            for h in range(f):
                if((m[h,j]!=0)&(h!=i)):
                    m[h,:]-=m[i,:]*m[h,j]
    return m

#Operacion elememtal volver ceros la columna pivote excepto elemento pivote, tratando de ahorrar procesos de operaciones sobre ceros
def opeE(M,i,j):
    [f,c]=M.shape
    if((i in range(f-1))&(j in range(c-1))&(M[i,j]!=0)):
        Mt=sp.zeros(f,c)
        u=list(set(range(f))-{i});u=[i]+u
        fl=0
        while(fl<f):
            cl=0
            if(u[fl]==i):
                while(cl<c):
                    if(M[u[fl],cl]!=0):
                        Mt[u[fl],cl]=M[u[fl],cl]/M[i,j]
                    cl+=1
            else:
                while(cl<c):
                    if((M[i,cl]!=0)&(M[u[fl],j]!=0)):
                        Mt[u[fl],cl]=M[u[fl],cl]-Mt[i,cl]*M[u[fl],j]
                    elif(M[u[fl],cl]!=0):
                        Mt[u[fl],cl]=M[u[fl],cl]
                    cl+=1
            fl+=1
        Mt[i,j]=1
    else:
        Mt=M
    return Mt
#Aplicar ope al menor cociente columna pivote y costos (busca la fila pivote)
def ope2(M,i):
    [f,c]=M.shape
    r=-1
    if(i in range(c-1)):
        p=0
        for j in range(f-1):
            if((M[j,i]>0)):
                p+=1
                t=M[j,c-1]/M[j,i]
                if(p>1):
                    if(t2.subs(N,1)>t.subs(N,1)):
                        t2=t;r=j
                else:
                    t2=t;r=j
    m=M
    if(r>=0):
        m=ope(M,r,i)
    return m

#Similar a ope2, usando "where" y ademas la columna pivote puede ser negativa u/v>0
def ope2_2(M,i):
    [f,c]=M.shape
    r=-1
    if(i in range(c-1)):
        u=np.array(M[:f-1,i].T)[0]
        v=np.array(M[:f-1,c-1].T.subs(N,1))[0]
        l=np.where((u!=0)&(u*v>0))[0]
        r=l[np.argmin(v[l]/u[l])]
    m=M
    if(r>=0):
        m=ope(M,r,i)
    return m

#Aplica ope2 buscando la columna pivote
def ope3(M):
    [f,c]=M.shape
    r=-1
    ng=0#;print('%i\t%i\t%i'%(f,c,r));print(M.shape)
    for i in range(c-1):
        if(M[f-1,i]<0):
            ng+=1
            t=M[f-1,i]
            if(ng>1):
                if(t<tm):
                    tm=t;r=i
            else:
                tm=t;r=i
    if(r>=0):
        M=ope2(M,r)
    return M

#Similar a ope3, usea where y argmin
def ope3_2(M):
    [f,c]=M.shape
    r=-1
    u=np.array(M[f-1,:c-1])[0]
    v=np.where(u<0)[0]
    if(len(v)>0):
        if(len(v)==1):
            r=v[0]
        else:
            r=v[np.argmin(u[v])]
    if(r>=0):
        M=ope2_2(M,r)
    return M

#Resuelve el prob de maximizacion
def ope4(M):
    ng=ngt(M)
    while(ng>0):
        M=ope3(M)
        ng=ngt(M)
    return M

#Resuelve el prob de maximizacion con opei_2
def ope4_2(M):
    [f,c]=M.shape
    u=np.array(M[f-1,:c-1])
    ng=len(np.where(u<0)[0])
    while(ng>0):
        M=ope3_2(M)
        ng=len(np.where(np.array(M[f-1,:c-1].T)<0)[0])
    return M

#Primera presentacion tabla
def ope5(M):
    [f,c]=M.shape
    MM=sp.zeros(f+1,c)
    l=[]
    for i in range(1,c):
        globals()['x%i'%i]=sp.symbols('x%i'%i)
        l+=['x%i'%i]
    MM[0,:c-1]=sp.Matrix([l])#sp.Matrix([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]])
    MM[1:f+1,:]=M
    return MM

#Primer intento de verificacion de resultados, dada la matriz le multiplicariamos el vector de resultado
def ope6(M):
    [f,c]=M.shape
    MM=ope5(M)
    V=sp.zeros(f,1)
    for i in range(1,f+1):
        s=0
        for j in range(c-1):
            s+=MM[0,j]*MM[i,j]
        V[i-1]=s
    return V

#Evalua, depues de aplicar ope6, las respuestas con el fin de mostrar la veracidad de los resultados
def ope7(M,mm):
    [f,c]=M.shape
    r=ope6(mm)
    for i in range(c-1):
        u=np.array(M[:,i].T)[0]
        v=np.where(u!=0)[0]
        if((len(v)==1)&(u[v[0]]==1)): #vector canonico
            r=r.subs(globals()['x%i'%(i+1)],M[v[0],c-1])
        if(M[f-1,i]>0):
            r=r.subs(globals()['x%i'%(i+1)],0)
        #r=r.subs(globals()['x%i'%(i+1)],globals()['X%i'%(i+1)])
    return r

#Realiza la prueba mostrando la diferencia de lo que debe resultar y resulta.
def ope8(M0,M):
    [_,c]=M0.shape
    return ope7(M,M0)-M0[:,c-1]

#En caso tengamos <= y >= aparecen variables negativas se puede completar con variables articifiales y seguir con el metodo de Big M o dos fases, u optar por
#no agregar variables artificiales y usar el metodo de simplex dual
#En caso del metodo de maximizacion se busca el mas negativo en el caso de minimizacion el mas positivo para escoger la variable el cual ingresa a la base
#En caso de minimizacion se busca z-c<=0 y maximizacion z-c>=0

#Convertir a Datos de entrada con los minimos elementos (Caso especifico donde el vector de indices de la funcion objetivo y otra restriccion estan en la matriz A)
def C2Ej(A,N0,f1): #A: solo matriz de indices, N0:vector de costos y ademas parte del vector objetivo (n*N, cantidad de elementos del "repositorio") 
    [f,c]=A.shape
    l=len(N0)
    ff=f1+2*(f-f1)+1;cc=c+ff
    M=np.zeros((ff,cc)).astype(int)
    b=sp.zeros(ff,1)
    Bb=list(range(c,cc))
    C=sp.zeros(1,cc+1)
    tmp=np.zeros((1,c)).astype(int)[0]
    if((f==l-1)&(c>2)&(f>2)&(f1>0)):
        M[1:f1+1,:c]=A[:f1,:]
        b[1:f1+1,0]=N0[:f1,0]
        for i in range(f-f1):
            M[f1+1+2*i,:c]=A[f1+i,:]
            M[f1+1+2*i+1,:c]=-A[f1+i,:]
            b[f1+1+2*i,0]=N0[f1+i,0]
            b[f1+1+2*i+1,0]=-N0[f1+i,0]
        for i in range(f1):
            tmp+=A[i,:]
            C[0,cc]+=N0[i,0]
        C[0,:c]=[tmp]
        C[0,:c]-=np.ones((1,c)).astype(int)
        C[0,cc]-=N0[f,0]
        M[0,:]=-C[0,:cc]
        b[0,0]=-C[0,cc]
        M[:,c:]=np.eye(ff)
    return [M,b,Bb,C]

def CvMT(A,b,Bb,C):
    [f,c]=A.shape
    M=sp.zeros(f+1,c+1)
    M[:f,:c]=A
    M[:f,c]=b
    M[f,:]=-C
    Cb=C[0,Bb]
    M[f,:]+=np.dot(Cb,M[:f,:])
    return M

#Convertir Problema de Datos Basicos a problema de datos basicos para Problema 2 Fases 
def C2PF(A,N0,f1): 
    [f,c]=A.shape
    l=len(N0)
    M=np.zeros((f+1,c)).astype(int)
    b=sp.zeros(f+1,1)
    d=np.zeros((f+1,1)).astype(int)
    C=sp.zeros(1,c+1)
    tmp=np.zeros((1,c)).astype(int)[0]
    if((f==l-1)&(c>2)&(f>2)&(f1>0)):
        M[1:,:]=A
        b[1:,0]=N0[:f,0]
        d[0,0]=-1
        for i in range(1,f1+1):
            d[i,0]=1
        for i in range(f1):
            tmp+=A[i,:]
            C[0,c]+=N0[i,0]
        C[0,:c]=[tmp]
        C[0,:c]-=np.ones((1,c)).astype(int)
        C[0,c]-=N0[f,0]
        M[0,:]=-C[0,:c]
        b[0,0]=-C[0,c]
    return [M,b,d,C]

#Convertir a entrada de datos para el metodo de 2 Fases con un minimo de elementos
def C2ej(A,b,d,C):
    [f,c]=A.shape
    M=np.zeros((1,1)).astype(int)
    bb=np.zeros((1,1)).astype(int).astype(object)
    Bb=[]
    Ar=[]
    Cr=sp.zeros(1,1)
    if((f==len(b))&(f==len(d))&(c+1==len(C))&(len(C)>0)&(f>0)):
        bi=np.where(np.array(b.T.subs(N,1))[0]<0)[0]
        dt=np.copy(d);dt[bi,0]*=-1
        dic=list(np.where(d==0)[0])#indices para ceros
        diM=list(np.where(dt<0)[0])#indices para >=
        ff=f
        nM=len(diM)
        if(len(dic)>0):
            #ff+=len(dic)
            #nM+=len(dic)
            cc=c+nM+ff
            M=np.zeros((ff,cc)).astype(int)
            bb=np.zeros((ff,1)).astype(int).astype(object)
            Bb=list(range(cc-ff,cc))
            Cr=sp.zeros(1,cc+1);Cr[0,:c]=C[0,:c];Cr[0,cc]=C[0,c]
            dsp=list(set(range(f))-set(bi))#-set(dic)
            M[bi,:c]=-A[bi,:]
            bb[bi,0]=-b.T[0,bi]
            M[dsp,:c]=A[dsp,:]
            bb[dsp,0]=b.T[0,dsp]
            M[diM,c]=-np.eye(nM).astype(int)
            M[:,cc-ff:]=np.eye(f).astype(int)
            Ar=list(np.array(diM+dic)+c)
            #vxc=np.array(range(len(dic)))+dic
            #lt=list(vxc)
            #lt2=list(vxc+1)
            #M[lt,:c]=A[dic,:]
            #M[lt2,:c]=-A[dic,:]
            #bb[lt,0]=b.T[0,dic]
            #bb[lt2,0]=-b.T[0,dic]
            #hn=list(diM)+lt2
            #M[hn,c:c+nM]=-np.eye(nM).astype(int)
            #M[:,cc-ff:]=np.eye(ff).astype(int)
            #Ar=[cc-ff+np.where(M[i,cc-ff:]==1)[0][0] for i in hn]
        else:
            cc=c+nM+ff
            M=np.zeros((ff,cc)).astype(int)
            bb=np.zeros((ff,1)).astype(int).astype(object)
            Bb=list(range(cc-ff,cc))
            Cr=sp.zeros(1,cc+1);Cr[0,:c]=C[0,:c];Cr[0,cc]=C[0,c]
            dsp=list(set(range(f))-set(bi))
            M[bi,:c]=-A[bi,:]
            M[dsp,:c]=A[dsp,:]
            bb[bi,0]=-b.T[0,bi]
            bb[dsp,0]=b.T[0,dsp]
            M[list(diM),c:c+nM]=-np.eye(nM).astype(int)
            M[:,cc-ff:]=np.eye(ff).astype(int)
            #Ar=list(range(cc-ff-nM,cc-ff))
            Ar=[cc-ff+np.where(M[i,cc-ff:]==1)[0][0]for i in diM]
    return [M,bb,Ar,Bb,Cr]

#Verificar si cumple q es multiplo de 9 la suma de columnas q representan gpos de(6,3,1)
def vrM(A,f3,f4):
    r=False
    [f,c]=A.shape
    if((f3>0)&(f>f3)&(c>0)&(f4>=0)&(f>f4)):
        S=np.zeros((1,c)).astype(int)
        for i in range(f):
            if(i<f-f3):
                S[0,:]+=A[i,:]*6#;print('i<f-f3:  %i'%i,end=', ')
            elif(i<f-f4):
                S[0,:]+=A[i,:]*3#;print('i<f-f4:  %i'%i,end=', ')
            else:
                S[0,:]+=A[i,:]#;print('else:  %i'%i)#
        S+=3;print(S)
        r=True
        i=0
        while(r&(i<c)):
            r=S[0,i]%9==0
            i+=1
    return r
           
def Ejsmx():
    f=3;c=6
    A=np.zeros((f,c)).astype(int)
    A[0,0]=2;A[0,1]=1;A[0,2]=1
    A[1,0]=1;A[1,1]=1;A[1,3]=1
    A[2,0]=1;A[2,1]=2;A[2,4]=-1;A[2,5]=1

    b=sp.Matrix([[20,18,12]]).T

    Bb=[2,3,5]

    C=sp.zeros(1,c+1)
    C[0,0]=5;C[0,1]=4;C[0,c-1]=-N
    return [A,b,Bb,C]

def EjD():
    f=2;c=6
    A=np.zeros((f,c)).astype(int)
    A[0,0]=-1;A[0,1]=-6;A[0,2]=-3;A[0,3]=-1;A[0,4]=1
    A[1,0]=-2;A[1,1]=5;A[1,2]=-1;A[1,3]=3;A[1,5]=1

    b=sp.Matrix([[-2,-3]]).T

    Bb=[4,5]

    C=sp.zeros(1,c+1)
    C[0,0]=2;C[0,1]=15;C[0,2]=5;C[0,3]=6
    return [A,b,Bb,C]

def EjD2():
    f=2;c=4
    A=np.zeros((f,c)).astype(int)
    A[0,0]=-5;A[0,1]=-12;A[0,2]=1
    A[1,0]=10;A[1,1]=6;A[1,3]=1
    b=sp.Matrix([[-40,60]]).T
    Bb=[2,3]
    C=sp.zeros(1,c+1)
    C[0,:2]=sp.Matrix([[-30,48]])
    return [A,b,Bb,C]

#Ejemplo problema de 2fases
def Ej2F():
    f=2;c=4
    A=np.zeros((f,c)).astype(int)
    A[0,:]=np.array([1,6,3,1])
    A[1,:]=np.array([-2,5,-1,3])
    b=sp.Matrix([[2,-3]]).T
    d=np.array([[-1,1]]).T
    C=sp.zeros(1,c+1)
    C[0]=2;C[1]=15;C[2]=5;C[3]=6
    return [A,b,d,C]

#Ejemplo especifico
def Ejx3y2():
    f1=5;f2=3;f3=3;f=f1+2*(f2+f3)+1;c1=10;c=c1+f
    A=np.zeros((f,c)).astype(int)
    A[1,0]=3;A[1,1]=1;A[1,2]=2;A[1,4]=1;A[1,5]=3;A[1,6]=1;A[1,7]=1;A[1,8]=2
    A[2,0]=6;A[2,1]=2;A[2,2]=3;A[2,3]=1;A[2,4]=1;A[2,7]=2
    A[3,0]=2;A[3,1]=2;A[3,2]=1;A[3,3]=1;A[3,4]=1;A[3,9]=2
    A[4,0]=3;A[4,1]=1;A[4,2]=1;A[4,3]=1;A[4,5]=3;A[4,6]=1;A[4,8]=1
    A[5,0]=1;A[5,1]=1;A[5,5]=1;A[5,6]=1;A[5,9]=1

    A[6,0]=6;A[6,1]=2;A[6,2]=2;A[6,4]=1
    A[8,0]=6;A[8,1]=2;A[8,2]=1;A[8,3]=1
    A[10,0]=3;A[10,1]=1;A[10,5]=3;A[10,6]=1

    A[12,0]=12;A[12,2]=4;A[12,7]=2
    A[14,0]=6;A[14,2]=2;A[14,5]=6;A[14,8]=2
    A[16,0]=2;A[16,1]=2;A[16,9]=2
    b=sp.zeros(f,1)
    b[1,0]=6;b[2,0]=6;b[3,0]=4;b[4,0]=3;b[5,0]=1; b[6,0]=3;b[8,0]=2;b[10,0]=1;b[12,0]=4;b[14,0]=3;b[16,0]=1
    for i in range(6):
        A[6+2*i+1,:]=-A[6+2*i,:]
        b[6+2*i+1,0]=-b[6+2*i,0]
    zz=np.zeros((1,f+c1)).astype(int);zz[0,:c1]=np.ones((1,c1)).astype(int)
    A[0,:]=A[1,:]+A[2,:]+A[3,:]+A[4,:]+A[5,:]-zz;A[0,:]*=-1
    b[0,0]=10-b[1,0]-b[2,0]-b[3,0]-b[4,0]-b[5,0]
    b*=N

    Bb=list(range(c1,c))

    C=sp.zeros(1,c+1)
    C[0,:c]=[-A[0,:]]
    C[0,c]=-b[0,0]
    A[:,c1:]=np.eye(f)
    return [A,b,Bb,C]

#Ejemplo especifico
def Ejx8():
    f1=3;f2=2;f3=4;f=f1+f2+f3;c=12
    A=np.zeros((f,c)).astype(int)
    #A[0,0]=8;A[0,1]=2;A[0,2]=1;A[0,4]=1;A[0,5]=4;A[0,7]=3;A[0,8]=5
    #A[1,0]=28;A[1,1]=1;A[1,2]=1;A[1,3]=2;A[1,5]=6;A[1,6]=1;A[1,7]=3;A[1,8]=10
    #A[2,0]=56;A[2,2]=1;A[2,4]=1;A[2,5]=4;A[2,6]=2;A[2,7]=1;A[2,8]=11
    #A[3,0]=168;A[3,2]=1;A[3,5]=12;A[3,7]=3;A[3,8]=30
    #A[4,0]=280;A[4,4]=1;A[4,5]=4;A[4,8]=25
    #A[5,0]=70;A[5,3]=2;A[5,4]=2;A[5,5]=2;A[5,8]=10
    #A[6,0]=56;A[6,1]=2;A[6,5]=12;A[6,7]=6;A[6,8]=20
    #A[7,0]=420;A[7,3]=2;A[7,5]=6;A[7,8]=30
    #A[8,0]=560;A[8,6]=2;A[8,8]=20
    A[0,:]=np.array([8,6,5,4,4,2,3,1,1,0,2,0])
    A[1,:]=np.array([28,16,10,8,6,1,3,0,1,2,1,1])
    A[2,:]=np.array([56,26,11,12,4,2,1,1,1,0,0,2])
    A[3,:]=np.array([168,66,30,20,12,0,3,0,1,0,0,0])
    A[4,:]=np.array([280,90,25,28,4,4,0,1,0,0,0,0])
    A[5,:]=np.array([70,30,10,14,2,4,0,2,0,2,0,0])
    A[6,:]=np.array([56,30,20,12,12,2,6,0,0,0,2,0])
    A[7,:]=np.array([420,120,30,32,6,0,0,0,0,2,0,0])
    A[8,:]=np.array([560,140,20,40,0,2,0,0,0,0,0,2])
    N0=N*np.ones((f+1,1)).astype(int)
    return [A,N0,f1]

#Ejemplo especifico
def Ejx5y():
    f1=5;f2=4;f3=2;f=f1+f2+f3;c=12
    A=np.zeros((f,c)).astype(int)
    #A[0,0]=1;A[0,2]=1;A[0,3]=1;A[0,5]=2;A[0,6]=3;A[0,7]=5;A[0,8]=2
    #A[1,0]=1;A[1,2]=1;A[1,4]=1;A[1,7]=5;A[1,8]=2
    #A[2,1]=1;A[2,3]=1;A[2,4]=2;A[2,5]=1;A[2,6]=3;A[2,7]=10;A[2,8]=1
    #A[3,1]=1;A[3,2]=1;A[3,3]=1;A[3,6]=1;A[3,7]=10;A[3,8]=1
    #A[4,0]=1;A[4,1]=1;A[4,7]=1;A[4,8]=1
    #A[5,0]=1;A[5,7]=5;A[5,8]=2
    #A[6,1]=1;A[6,7]=10;A[6,8]=1
    #A[7,2]=1;A[7,7]=20;A[7,8]=2
    #A[8,3]=1;A[8,6]=3;A[8,7]=30
    #A[9,4]=2;A[9,7]=30
    #A[10,5]=2;A[10,6]=6;A[10,7]=20;A[10,8]=2
    A[0,:]=np.array([5,3,2,4,2,3,1,0,1,1,0,2])
    A[1,:]=np.array([5,3,2,1,1,0,1,0,1,0,1,0])
    A[2,:]=np.array([10,4,1,6,2,3,0,1,0,1,2,1])
    A[3,:]=np.array([10,4,1,4,2,1,0,1,1,1,0,0])
    A[4,:]=np.array([1,1,1,0,0,0,1,1,0,0,0,0])
    A[5,:]=np.array([5,3,2,0,0,0,1,0,0,0,0,0])
    A[6,:]=np.array([10,4,1,0,0,0,0,1,0,0,0,0])
    A[7,:]=np.array([20,6,2,4,2,0,0,0,1,0,0,0])
    A[8,:]=np.array([30,6,0,12,2,3,0,0,0,1,0,0])
    A[9,:]=np.array([30,6,0,6,2,0,0,0,0,0,2,0])
    A[10,:]=np.array([20,6,2,12,2,6,0,0,0,0,0,2])
    N0=N*np.array([[5,2,4,3,1,1,1,2,3,2,4,6]]).T
    return [A,N0,f1]

#Ejemplo especifico
def Ejx6():
    f1=2;f2=1;f3=3;f=f1+f2+f3;c=7
    M=np.zeros((f,c)).astype(int)
    M[0,0]=6;M[0,1]=3;M[0,2]=2;M[0,3]=1;M[0,4]=2
    M[1,0]=15;M[1,1]=3;M[1,2]=3;M[1,3]=1;M[1,4]=1;M[1,5]=3
    M[2,0]=60;M[2,1]=3;M[2,2]=4;M[2,3]=1
    M[3,0]=20;M[3,1]=2;M[3,2]=4;M[3,3]=2;M[3,6]=2
    M[4,0]=30;M[4,1]=6;M[4,2]=2;M[4,4]=2
    M[5,0]=90;M[5,2]=6;M[5,5]=6
    N0=N*np.ones((f+1,1)).astype(int)#;b[0,0]*=-1;b=b.T[0]
    #for i in range(4):
    #    M[3+2*i+1,:]=-M[3+2*i,:]
    #    b[3+2*i+1]*=-1

    #Bb=list(range(c-f,c))

    #C=sp.zeros(1,c+1)
    #C[0,:c]=-M[0,:]
    #C[0,c]=-b[0]
    #C[0,0]=20;C[0,1]=5;C[0,2]=4;C[0,3]=1;C[0,4]=2;C[0,5]=2;C[0,6]=-1
    #M[:,7:]=sp.eye(f)
    return [M,N0,f1]

#Ejemplo especifico
def Ejx4y4():
    f1=11;f2=22;f3=8;f=f1+f2+f3;c=59
    A=np.zeros((f,c)).astype(int)
    A[0,0]=4;A[0,1]=3;A[0,2]=4;A[0,3]=1;A[0,4]=2;A[0,5]=1;A[0,6]=4;A[0,8]=2;A[0,9]=3;A[0,10]=1;A[0,11]=1;A[0,12]=1;A[0,13]=4;A[0,15]=2;A[0,17]=1;A[0,19]=1;A[0,21]=1;A[0,22]=2;A[0,24]=2;A[0,25]=1;A[0,26]=4;A[0,28]=2;A[0,31]=3;A[0,33]=1;A[0,35]=1;A[0,38]=1;A[0,40]=1;A[0,45]=1;A[0,48]=1;A[0,49]=1;A[0,53]=2
    A[1,0]=4;A[1,1]=3;A[1,2]=1;A[1,3]=4;A[1,4]=2;A[1,5]=1;A[1,7]=4;A[1,8]=2;A[1,9]=1;A[1,10]=3;A[1,11]=1;A[1,12]=1;A[1,14]=4;A[1,16]=2;A[1,18]=1;A[1,19]=1;A[1,20]=1;A[1,23]=2;A[1,24]=1;A[1,25]=2;A[1,27]=4;A[1,29]=2;A[1,32]=3;A[1,34]=1;A[1,36]=1;A[1,37]=1;A[1,39]=1;A[1,46]=1;A[1,47]=1;A[1,49]=1;A[1,54]=2
    A[2,0]=4;A[2,1]=1;A[2,2]=4;A[2,3]=1;A[2,4]=2;A[2,5]=1;A[2,6]=4;A[2,9]=1;A[2,11]=1;A[2,13]=4;A[2,15]=2;A[2,17]=1;A[2,19]=1;A[2,21]=1;A[2,26]=4;A[2,31]=1;A[2,33]=1;A[2,35]=1;A[2,42]=1;A[2,47]=1
    A[3,0]=4;A[3,1]=1;A[3,2]=1;A[3,3]=4;A[3,4]=2;A[3,5]=1;A[3,7]=4;A[3,10]=1;A[3,12]=1;A[3,14]=4;A[3,16]=2;A[3,18]=1;A[3,19]=1;A[3,20]=1;A[3,27]=4;A[3,32]=1;A[3,34]=1;A[3,36]=1;A[3,41]=1;A[3,48]=1
    A[4,0]=6;A[4,1]=3;A[4,2]=6;A[4,4]=2;A[4,5]=1;A[4,6]=6;A[4,7]=2;A[4,8]=1;A[4,9]=3;A[4,11]=1;A[4,13]=6;A[4,14]=2;A[4,15]=2;A[4,16]=2;A[4,17]=1;A[4,18]=1;A[4,20]=2;A[4,22]=1;A[4,23]=1;A[4,24]=1;A[4,26]=6;A[4,28]=1;A[4,30]=1;A[4,31]=3;A[4,33]=1;A[4,39]=1;A[4,41]=1;A[4,43]=1;A[4,50]=1;A[4,51]=1;A[4,53]=1;A[4,55]=2
    A[5,0]=6;A[5,1]=3;A[5,3]=6;A[5,4]=2;A[5,5]=1;A[5,6]=2;A[5,7]=6;A[5,8]=1;A[5,10]=3;A[5,12]=1;A[5,13]=2;A[5,14]=6;A[5,15]=2;A[5,16]=2;A[5,17]=1;A[5,18]=1;A[5,21]=2;A[5,22]=1;A[5,23]=1;A[5,25]=1;A[5,27]=6;A[5,29]=1;A[5,30]=1;A[5,32]=3;A[5,34]=1;A[5,40]=1;A[5,42]=1;A[5,44]=1;A[5,50]=1;A[5,52]=1;A[5,54]=1;A[5,56]=2
    A[6,0]=24;A[6,1]=12;A[6,2]=6;A[6,4]=4;A[6,5]=2;A[6,7]=8;A[6,8]=2;A[6,9]=3;A[6,11]=1;A[6,14]=8;A[6,16]=4;A[6,18]=2;A[6,20]=2;A[6,23]=2;A[6,24]=1; A[6,29]=2;A[6,37]=1;A[6,39]=1;A[6,41]=1;A[6,45]=1;A[6,52]=2
    A[7,0]=24;A[7,1]=12;A[7,3]=6;A[7,4]=4;A[7,5]=2;A[7,6]=8;A[7,8]=2;A[7,10]=3;A[7,12]=1;A[7,13]=8;A[7,15]=4;A[7,17]=2;A[7,21]=2;A[7,22]=2;A[7,25]=1;A[7,28]=2;A[7,38]=1;A[7,40]=1;A[7,42]=1;A[7,46]=1;A[7,51]=2
    A[8,0]=16;A[8,1]=10;A[8,2]=4;A[8,3]=4;A[8,4]=4;A[8,5]=2;A[8,8]=4;A[8,9]=3;A[8,10]=3;A[8,11]=1;A[8,12]=1;A[8,19]=1;A[8,24]=2;A[8,25]=2;A[8,30]=2;A[8,43]=1;A[8,44]=1;A[8,49]=1;A[8,57]=2
    A[9,0]=16;A[9,1]=6;A[9,2]=4;A[9,3]=4;A[9,4]=4;A[9,5]=2;A[9,9]=1;A[9,10]=1;A[9,11]=1;A[9,12]=1;A[9,19]=1;A[9,30]=2;A[9,43]=1;A[9,44]=1;A[9,45]=1;A[9,46]=1;A[9,47]=1;A[9,48]=1
    A[10,[0,2,3,4,6,7,13,14,15,16,19,20,21,26,27,35,36,55,56]]=sp.ones(1,19)
    A[11,0]=4;A[11,2]=4;A[11,3]=1;A[11,4]=2;A[11,6]=4;A[11,13]=4;A[11,15]=2;A[11,19]=1;A[11,21]=1;A[11,26]=4;A[11,35]=1
    A[12,0]=4;A[12,2]=1;A[12,3]=4;A[12,4]=2;A[12,7]=4;A[12,14]=4;A[12,16]=2;A[12,19]=1;A[12,20]=1;A[12,27]=4;A[12,36]=1
    A[13,0]=12;A[13,1]=3;A[13,2]=12;A[13,4]=2;A[13,5]=1;A[13,6]=12;A[13,9]=3;A[13,11]=1;A[13,13]=12;A[13,15]=2;A[13,17]=1;A[13,26]=12;A[13,31]=3;A[13,33]=1
    A[14,0]=12;A[14,1]=3;A[14,3]=12;A[14,4]=2;A[14,5]=1;A[14,7]=12;A[14,10]=3;A[14,12]=1;A[14,14]=12;A[14,16]=2;A[14,18]=1;A[14,27]=12;A[14,32]=3;A[14,34]=1
    A[15,0]=48;A[15,1]=21;A[15,2]=12;A[15,4]=4;A[15,5]=1;A[15,8]=4;A[15,9]=6;A[15,24]=2
    A[16,0]=48;A[16,1]=15;A[16,2]=12;A[16,4]=4;A[16,5]=1;A[16,9]=3;A[16,11]=1;A[16,45]=1
    A[17,0]=48;A[17,1]=12;A[17,2]=12;A[17,4]=4;A[17,5]=2;A[17,9]=3;A[17,11]=1;A[17,30]=2;A[17,43]=1
    A[18,0]=48;A[18,1]=21;A[18,3]=12;A[18,4]=4;A[18,5]=1;A[18,8]=4;A[18,10]=6;A[18,25]=2
    A[19,0]=48;A[19,1]=15;A[19,3]=12;A[19,4]=4;A[19,5]=1;A[19,10]=3;A[19,12]=1;A[19,46]=1
    A[20,0]=48;A[20,1]=12;A[20,3]=12;A[20,4]=4;A[20,5]=2;A[20,10]=3;A[20,12]=1;A[20,30]=2;A[20,44]=1
    A[21,0]=24;A[21,1]=9;A[21,2]=6;A[21,4]=4;A[21,5]=1;A[21,7]=8;A[21,8]=2;A[21,9]=3;A[21,11]=1;A[21,14]=8;A[21,16]=4;A[21,18]=1;A[21,20]=2;A[21,23]=2;A[21,24]=1;A[21,39]=1
    A[22,0]=24;A[22,1]=3;A[22,2]=6;A[22,4]=4;A[22,5]=1;A[22,7]=8;A[22,14]=8;A[22,16]=4;A[22,18]=1;A[22,20]=2;A[22,41]=1
    A[23,0]=24;A[23,1]=9;A[23,3]=6;A[23,4]=4;A[23,5]=1;A[23,6]=8;A[23,8]=2;A[23,10]=3;A[23,12]=1;A[23,13]=8;A[23,15]=4;A[23,17]=1;A[23,21]=2;A[23,22]=2;A[23,25]=1;A[23,40]=1
    A[24,0]=24;A[24,1]=3;A[24,3]=6;A[24,4]=4;A[24,5]=1;A[24,6]=8;A[24,13]=8;A[24,15]=4;A[24,17]=1;A[24,21]=2;A[24,42]=1
    A[25,0]=16;A[25,1]=9;A[25,2]=4;A[25,3]=4;A[25,4]=4;A[25,5]=1;A[25,8]=4;A[25,9]=3;A[25,10]=3;A[25,11]=1;A[25,12]=1;A[25,19]=1;A[25,24]=2;A[25,25]=2;A[25,49]=1
    A[26,0]=16;A[26,1]=3;A[26,2]=4;A[26,3]=4;A[26,4]=4;A[26,5]=1;A[26,9]=1;A[26,11]=1;A[26,19]=1;A[26,47]=1
    A[27,0]=16;A[27,1]=3;A[27,2]=4;A[27,3]=4;A[27,4]=4;A[27,5]=1;A[27,10]=1;A[27,12]=1;A[27,19]=1;A[27,48]=1
    A[28,0]=16;A[28,1]=1;A[28,2]=4;A[28,3]=4;A[28,4]=4;A[28,5]=1;A[28,19]=1
    A[29,0]=72;A[29,1]=27;A[29,4]=4;A[29,5]=1;A[29,7]=24;A[29,8]=2;A[29,14]=24;A[29,16]=4;A[29,18]=1;A[29,23]=2;A[29,29]=4;A[29,37]=1
    A[30,0]=72;A[30,1]=27;A[30,4]=4;A[30,5]=1;A[30,6]=24;A[30,8]=2;A[30,13]=24;A[30,15]=4;A[30,17]=1;A[30,22]=2;A[30,28]=4;A[30,38]=1
    A[31,0]=144;A[31,1]=45;A[31,4]=4;A[31,5]=1
    A[32,0]=36;A[32,1]=9;A[32,4]=4;A[32,5]=1;A[32,6]=12;A[32,7]=12;A[32,8]=1;A[32,13]=12;A[32,14]=12;A[32,15]=4;A[32,16]=4;A[32,17]=1;A[32,18]=1;A[32,22]=1;A[32,23]=1;A[32,30]=1;A[32,50]=1
    A[33,0]=12;A[33,1]=6;A[33,2]=12;A[33,4]=2;A[33,6]=12;A[33,8]=2;A[33,9]=6;A[33,13]=12;A[33,15]=2;A[33,22]=2;A[33,24]=2;A[33,26]=12;A[33,28]=2;A[33,31]=6;A[33,53]=2
    A[34,0]=12;A[34,1]=6;A[34,3]=12;A[34,4]=2;A[34,7]=12;A[34,8]=2;A[34,10]=6;A[34,14]=12;A[34,16]=2;A[34,23]=2;A[34,25]=2;A[34,27]=12;A[34,29]=2;A[34,32]=6;A[34,54]=2
    A[35,0]=6;A[35,2]=6;A[35,4]=2;A[35,6]=6;A[35,7]=2;A[35,13]=6;A[35,14]=2;A[35,15]=2;A[35,16]=2;A[35,20]=2;A[35,26]=6;A[35,55]=2
    A[36,0]=6;A[36,3]=6;A[36,4]=2;A[36,6]=2;A[36,7]=6;A[36,13]=2;A[36,14]=6;A[36,15]=2;A[36,16]=2;A[36,21]=2;A[36,27]=6;A[36,56]=2
    A[37,0]=144;A[37,1]=54;A[37,4]=4;A[37,5]=2;A[37,8]=4;A[37,30]=2;A[37,57]=2
    A[38,0]=36;A[38,1]=18;A[38,4]=4;A[38,5]=2;A[38,6]=12;A[38,7]=12;A[38,8]=2;A[38,13]=12;A[38,14]=12;A[38,15]=4;A[38,16]=4;A[38,17]=2;A[38,18]=2;A[38,22]=2;A[38,23]=2;A[38,28]=4;A[38,29]=4;A[38,30]=2;A[38,37]=2;A[38,38]=2;A[38,50]=2;A[38,57]=2;A[38,58]=2
    A[39,0]=72;A[39,1]=18;A[39,4]=4;A[39,5]=2;A[39,6]=24;A[39,13]=24;A[39,15]=4;A[39,17]=2;A[39,28]=2;A[39,51]=2
    A[40,0]=72;A[40,1]=18;A[40,4]=4;A[40,5]=2;A[40,7]=24;A[40,14]=24;A[40,16]=4;A[40,18]=2;A[40,29]=2;A[40,52]=2
    N0=N*np.array([[35,35,5,5,15,15,30,30,40,16,1,1,1,5,5,20,12,8,20,12,8,10,3,10,3,20,4,4,2,18,18,18,6,15,15,1,1,24,36,9,9,70]]).T
    return [A,N0,f1]

#Muestra si la resolucion del prob es correcta
def rslc(A,b,Bb,br):
    r=False
    [f,c]=A.shape
    if((len(br)==f)&(len(b)==f)&(len(Bb)==f)&(f>1)&(c>1)):
        r=True
        Xr=sp.zeros(c,1)
        for i in range(f):
            Xr[Bb[i],0]=br[i]
        r=A*Xr==b
    return r

def lrD2(dt):#Por el momento no tiene uso, podria cargar las variables: 'A','b','Bb','M','Bbc','mxmn','C','pd','NC','NI','fc','hst'|'A','b','mxmn','Bb','C','NI'
    if(len(dt)!=0):
        #locals().update(dt)
        if(len(dt)==6):
            [A,b,mxmn,Bb,C,NI]=dt
        else:
            [A,b,Bb,M,Bbc,mxmn,C,pd,NC,NI,fc,hst]=dt
            locals()[M]=eval(M)
            locals()[Bbc]=eval(Bbc)
            locals()[pd]=eval(pd)
            locals()[NC]=eval(NC)
            locals()[fc]=eval(fc)
            locals()[hst]=eval(hst)
        locals()[A]=eval(A)
        locals()[b]=eval(b)
        locals()[mxmn]=eval(mxmn)
        locals()[Bb]=eval(Bb)
        locals()[C]=eval(C)
        locals()[NI]=eval(NI)
    return dt

def cmb(Bb,i,j):
    #L=fls.lr2(rt)
    #Ls=[[int(i)for i in j[:-1].split(',')]for j in L]
    #c=0
    #if(Bb in Ls):
    #    c=Ls.count(Bb)
    print('\x1b[032m de: %i a: %i \x1b[0m '%(Bb[i],j))#El cambio es \x1b[033m %i \x1b[0m

#Paso 1: seleccionar las variables que formaran la base
#Paso 2: Obtener B^-1
#Paso 3: Obtener B^-1A, B^-1b
#Paso 4: Obtener CbB^-1A-C, CbB^-1b
#Paso 5: Si CbB^-1A-C>=0, terminamos. De lo contrario regresar al paso 1

#Metodo simplex maximizacion, metodo matricial con matriz inversa, uniq: en caso se use como parte de algun otro metodo tomando valor entero>=0, sino valor -1
#;)
def smx(A,b,Bb,C,step,uniq):#Incluye metodo big M
    #fact=False
    [f,c]=A.shape
    nt=uniq
    A2=np.zeros((f,c)).astype(int)
    b2=sp.zeros(f,1)
    z=sp.zeros(1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        #fact=True
    #l=[]
    #for i in range(c):
    #    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
    #    l+=['x%i'%(i+1)]
    #X=np.array(l)#;print('Vector X');print(X)
        B=A[:,Bb];B=sp.Matrix(B)#;print('Matriz B');print(B)
        Cb=np.zeros(f).astype(int)#;print('Vector Cb');print(Cb)
        Cb=C[0,Bb]
        b2=np.linalg.linalg.matmul(B.inv(),b)#;print(b2)
        A2=np.linalg.linalg.matmul(B.inv(),A)#;print(A2[:,1])
        z=sp.zeros(1,c+1);z[0,:c]=np.linalg.linalg.matmul(Cb,A2);z[0,c]=np.dot(Cb,b2)#;print('Vector z');print(z)
        Z=z-C#;print('Vector Z');print(Z)
        zr=np.linalg.linalg.matmul(Cb,np.linalg.linalg.matmul(B.inv(),b))
        Zt=np.array(Z[0,:c].subs(N,100))[0]#;print('Vector Zt');print(Zt)
        u=list(np.where(Zt<0)[0])#;print('where Zt<0');print(np.where(Zt<0))
        while(len(u)>0):
            #print('Vector Z',end='\t');print(Z,end='\t');print('argmin Z[u]',end='\t');print(np.argmin(Zt[u]),end='\t');print('Vector u',end='\t');print(u)
            cl=u[np.argmin(Zt[u])]
            l=list(np.where(A2[:,cl]>0)[0])#;print('l',end='\t');print(l,end='\t');print('cl %i'%cl);print('where A2[:,cl]>0',end='\t');print(A2[:,cl]);print(b2[l,0])#;print(A2)
            fl=l[np.argmin(b2[l,0]/A2[l,cl])]#;print(b[l]/A2[l,cl])
            if (step==1):
                print('Tabla N%s%i'%(chr(176),nt+1));prnt.Tbl(A2,b2,Bb,z,C,fl,cl);input('Siguiente ...')
            elif(step==0):
                print('De la tabla (N%s%i), la base es: '%(chr(176),nt+1),end='\t');print(Bb)
            Bb[fl]=cl#;print('Bb:',end='\t');print(Bb,end='\t');print('%i\t%i'%(fl,cl))
            B[:,fl]=A[:,cl]#;print('B:',end='\t');print(B);print(B.inv())#;print('A[i,cl] y B[i,fl]');print('%f\t%f'%(A[i,cl],B[i,fl]))#;print('A');print(A)
            A2=np.linalg.linalg.matmul(B.inv(),A)#;print('A2');print(A2)
            b2=np.linalg.linalg.matmul(B.inv(),b)
            Cb=C[0,Bb]
            z[0,:c]=np.linalg.linalg.matmul(Cb,A2);z[0,c]=np.dot(Cb,b2)
            Z=z-C
            zr=np.dot(Cb,b2)
            Zt=np.array(Z[0,:c].subs(N,100))[0]
            u=np.where(Zt<0)[0]
            nt+=1
        if (step==1):
            #if(uniq==-1):
            print('Tabla Final N%s%i'%(chr(176),nt+1));prnt.Tbl(A2,b2,Bb,z,C,-3,-3);print(' ::: END ::: ')
        elif(step==0):
            print('Base resultante (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb)
            if(uniq==-1):
                Xr=sp.zeros(c,1)
                for i in range(len(b2)):
                    Xr[Bb[i],0]=b2[i]
                l=[]
                for i in range(c):
                    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                    l+=['x%i'%(i+1)]
                X=np.array(l)
                u=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
                v=list(np.array(Bb)[u])
                prnt.Tbr(X[v],np.array(Xr.T)[0][v],zr)
                print('::: END :::')
    else:
        print('\x1b[043m %s \x1b[0m'%'Problema con la validacion de datos')
    return [A2,b2,Bb,nt]

#Metodo simplex maximizacion, metodo por operaciones elementales
#;)
def smx2(A,b,Bb,C,step,uniq):#Incluye metodo Big-M
    prob=False
    [f,c]=A.shape
    nt=uniq
    M=sp.zeros(f+1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        #fact=True
        Cb=C[0,Bb]
        M[:f,:c]=A;M[:f,c]=b
        z=np.linalg.linalg.matmul(Cb,M[:f,:])
        M[f,:]=z-C
        Zt=np.array(M[f,:c].subs(N,100))[0]
        u=list(np.where(Zt<0)[0])
        while((not prob)&(len(u))):
            cl=u[np.argmin(Zt[u])]
            l=list(np.where(np.array(M[:f,cl].T)[0]>0)[0])
            fl=l[np.argmin(np.array(M[l,c].T)[0]/np.array(M[l,cl].T)[0])]
            if (step==1):
                print('Tabla N%s%i'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,z,C,fl,cl);input('Siguiente ...')
            elif(step==0):
                print('De la Tabla (N%s%i), el cambio en la base es: '%(chr(176),nt+1),end='');cmb(Bb,fl,cl)#;print(Bb)
            M=ope(M,fl,cl)
            Bb[fl]=cl
            prob=fls.svL(rt,Bb)
            Cb=C[0,Bb]
            z=np.linalg.linalg.matmul(Cb,M[:f,:])
            Zt=np.array(M[f,:c].subs(N,100))[0]
            u=list(np.where(Zt<0)[0])
            nt+=1
        if (step==1):
            #if(uniq==-1):
            print('Tabla Final (N%s%i)'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,z,C,-3,-3)#;print('\x1b[034m %s \x1b[0m'%'::: END :::')
        elif(step==0):
            print('Base Final (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb)
            if(uniq==-1):
                Xr=sp.zeros(c,1)
                for i in range(f):
                    Xr[Bb[i],0]=M[i,c]
                l=[]
                for i in range(c):
                    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                    l+=['x%i'%(i+1)]
                X=np.array(l)
                u=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
                v=list(np.array(Bb)[u])
                prnt.Tbr(X[v],np.array(Xr.T)[0][v],M[f,c])
                print('::: ~ . ~ :::')
    else:
        print('\x1b[043m %s \x1b[0m'%'Problema con los datos de entrada')
    return [M[:f,:c],M[:f,c],Bb,nt]

#Metodo simplex minimizacion
#;)
def smn(A,b,Bb,C,step,uniq):#Incluye big M, C contiene la variable simbolica N
    #fact=False, step: 0-solo base iter 1-muestra tablas -1 no muestra nada solo retorna resultado
    [f,c]=A.shape
    nt=uniq
    A2=np.zeros((f,c)).astype(int)
    b2=sp.zeros(f,1)
    z=sp.zeros(1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        #fact=True
        B=A[:,Bb];B=sp.Matrix(B)
        Cb=np.zeros(f).astype(int)
        Cb=C[0,Bb]#;print(C);print(Cb)
        A2=np.linalg.linalg.matmul(B.inv(),A)
        b2=np.linalg.linalg.matmul(B.inv(),b)
        z=sp.zeros(1,c+1);z[0,:c]=np.linalg.linalg.matmul(Cb,A2);z[0,c]=np.dot(Cb,b2)
        zr=np.dot(Cb,np.linalg.linalg.matmul(B.inv(),b))
        Z=z-C;Z=sp.Matrix(Z)
        Zt=np.array(Z[0,:c].subs(N,100))[0]#;print('Z',end='\t');print(Zt)
        u=list(np.where(Zt>0)[0])#;print('u',end='\t');print(u)
        while(len(u)>0):
            cl=u[np.argmax(Zt[u])]
            l=list(np.where(A2[:,cl]>0)[0])#;print('b/A',end='\t');print(b[l]/A2[l,cl])
            fl=l[np.argmin(b2[l,0]/A2[l,cl])]
            if (step==1):
                print('Tabla N%s%i'%(chr(176),nt+1));prnt.Tbl(A2,b2,Bb,z,C,fl,cl);input('Siguiente ...')
            elif(step==0):
                print('Actual Base (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb)
            Bb[fl]=cl
            B[:,fl]=A[:,cl]
            A2=np.linalg.linalg.matmul(B.inv(),A)
            b2=np.linalg.linalg.matmul(B.inv(),b)
            Cb=C[0,Bb]
            z=sp.zeros(1,c+1);z[0,:c]=np.linalg.linalg.matmul(Cb,A2);z[0,c]=np.dot(Cb,b2)
            Z=sp.Matrix(z-C)
            zr=np.dot(Cb,b2)
            Zt=np.array(Z[0,:c].subs(N,100))[0]#;print('Z',end='\t');print(Zt)
            u=np.where(Zt>0)[0]#;print('u',end='\t');print(u)
            nt+=1
        if (step==1):
            #if(uniq==-1):
            print('Tabla Final N%s%i'%(chr(176),nt+1));prnt.Tbl(A2,b2,Bb,z,C,-3,-3)#;print('\x1b[034m ::: END ::: \x1b[0m')
        elif(step==0):
            print('Base final (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb)
            if(uniq==-1):
                Xr=sp.zeros(c,1)
                for i in range(len(b2)):
                    Xr[Bb[i],0]=b2[i]
                l=[]
                for i in range(c):
                    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                    l+=['x%i'%(i+1)]
                X=np.array(l)
                u=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
                v=list(np.array(Bb)[u])
                prnt.Tbr(X[v],np.array(Xr.T)[0][v],zr)
                print('\x1b[044m %s \x1b[0m'%'::: FIN :::')
    else:
        print('\x1b[043m Problema con la validacion de datos \x1b[0m')
    return [A2,b2,Bb,nt]

#Metodo simplex minimizacion ope elementales
#;)
def smn2(A,b,Bb,C,step,uniq):#A: Matriz de coef, b:Vector de costes, Bb: Base Inicial, C:funcion objetivo, step: tabla x tabla, uniq: es solo un problema de min
    prob=False
    [f,c]=A.shape
    nt=uniq
    M=sp.zeros(f+1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        M[:f,:c]=A;M[:f,c]=b
        if(nt==0):
            fls.brr(rt,True)
        prob=False#fls.svL(rt,Bb)
        Cb=C[0,Bb]
        z=np.linalg.linalg.matmul(Cb,M[:f,:])
        M[f,:]=z-C
        Zt=np.array(M[f,:c].subs(N,100))[0]
        u=list(np.where(Zt>0)[0])
        while((not prob)&(len(u)>0)):
            cl=u[np.argmax(Zt[u])]
            l=list(np.where(np.array(M[:f,cl].T)[0]>0)[0])
            fl=l[np.argmin(np.array(M[l,c].subs(N,10).T)[0]/np.array(M[l,cl].T)[0])]
            if (step==1):
                print('Tabla N%s%i'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,z,C,fl,cl);input('Siguiente ... ')
            elif(step==0):
                print('De la Tabla (N%s%i), el cambio en la base es:'%(chr(176),nt+1),end=' ');cmb(Bb,fl,cl)#;print(Bb)
            M=ope(M,fl,cl)
            Bb[fl]=cl
            prob=fls.svL(rt,Bb)
            Cb=C[0,Bb]
            z=np.linalg.linalg.matmul(Cb,M[:f,:])
            Zt=np.array(M[f,:c].subs(N,100))[0]
            u=list(np.where(Zt>0)[0])
            nt+=1
        if (step==1):
            #if(uniq==-1):
            print('Tabla Final (N%s%i)'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,z,C,-3,-3)#;print('\x1b[034m %s \x1b[0m'%'::: END :::')
        elif(step==0):
            print('La Base resultante (N%s%i) es'%(chr(176),nt+1),end='\t');print(Bb)
            if(uniq==-1):
                Xr=sp.zeros(c,1)
                for i in range(f):
                    Xr[Bb[i],0]=M[i,c]
                l=[]
                for i in range(c):
                    globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                    l+=['x%i'%(i+1)]
                X=np.array(l)
                u=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
                v=list(np.array(Bb)[u])
                prnt.Tbr(X[v],np.array(Xr.T)[0][v],M[f,c])
                print('\x1b[044m %s \x1b[0m'%'::: ~.~ :::')
    else:
        print('\x1b[043m Problema con la validacion de datos \x1b[0m')
    return [M[:f,:c],M[:f,c],Bb,nt]
#Metodo simplex dual minimizacion, con operacion por matriz inversa
#A:matriz previamente preparada, b:vector de costos, Bb: lista base inicial, C: vector funcion objetivo, step: tabla por paso
#Salida: M:matriz final, b: Nuevo Vector de costes, zr: Valor final de la funcion objetivo, Xr: resultado de las variables no basicas
#s;)
def smnD(A,b,Bb,C,step):#Solo para problemas pequenos, problemas grandes hallar la inversa toma su tiempo
    #En el ejemplo se tenia al menos un negativo en el vector b, por lo q se opto por metodo simplex dual
    #Se comenzo con el problema de min inicialmente el vector z-C con todos los elementos negtivos
    #y el vector b son inicialmente todos negativos por lo q el problema es infactible pues es optima y b<0
    #Resolviendo el problema del dual q es de max se busca en el vector b los mas negativos(en este caso)
    fact=True
    nt=0
    [f,c]=A.shape
    A2=np.zeros((f,c)).astype(int)
    b2=sp.zeros(f,1)
    #zr=0
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        v6=js.loads('"\\u2502"')
        h6=js.loads('"\\u2500"')
        B=A[:,Bb];B=sp.Matrix(B)
        Cb=C[0,Bb]#;print('Cb',end='\t');print(Cb)#;print(B.inv()*A)
        A2=np.linalg.linalg.matmul(B.inv(),A)
        b2=np.dot(B.inv(),b)#;print(B.inv());print(b);print('producto B^-1 b' );print(b2)
        z=sp.zeros(1,c+1)
        z[0,:c]=np.dot(Cb,A2);z[0,c]=np.dot(Cb,b)
        Z=z-C
        #zr=np.dot(Cb,b2)#;print(np.array(sp.Matrix(b2).T.subs(N,1))[0])
        u=np.where(np.array(sp.Matrix(b2).T.subs(N,1))[0]<0)[0]
        v=np.where(np.array(Z[0,:c].subs(N,1000))>0)[0]
        hst=''

        while((fact)&((len(u)>0)|(len(v)>0))):
            if(len(u)>0):
                hst+=v6
            while(len(u)>0):
                fl=u[np.argmin(np.array(sp.Matrix(b2).T.subs(N,1))[0][u])]#;print('A2[fl.:]',end='\t');print(A2[fl,:])
                v=np.where(A2[fl,:]<0)[0]#;print('A[fl,:]<0',end='\t');print(v)
                if(len(v)>0):
                    #print('Z[0,algo]',end='\t');print(Z[0,list(v)]);print('Z',end='\t');print(Z);print('Z.shape',end='\t');print(Z.shape);print('v',end='\t');print(v);print('Z[v]',end='\t');print(Z[0,list(v)])
                    cl=v[np.argmin(Z[0,list(v)]/A2[fl,v])]#;print('Z',end='\t');print(np.array(Z[0,list(v)])[0]);print('A',end='\t');print(A2[fl,v],end='\t');print('v,z/A',end='\t');print(v,np.array(Z[0,list(v)])[0]/A2[fl,v])#;print('fl,cl',end='\t');print('%i\t%i'%(fl,cl),end='\t');
                    if (step==1):
                        print('TABLA N%s%i'%(chr(176),nt+1));prnt.Tbl(A2,b2,Bb,z,C,fl,cl);input('Siguiente... ')
                    elif(step==0):
                        print('De la tabla (N%s%i), la base es:'%(chr(176),nt+1),end='\t'); print(Bb)#;input('Siguiente...')
                    Bb[fl]=cl
                    Cb=C[0,Bb]#;print('Bb',end='\t');print(Bb);print('Cb',end='\t');print(Cb)#print('C');print(C);
                    B[:,fl]=A[:,cl]
                    A2=np.dot(B.inv(),A)#;print('A');pM2(A2)
                    b2=np.dot(B.inv(),b)#;print('\tb',end='\t');print(b2)
                    z[0,:c]=np.dot(Cb,A2);z[0,c]=np.dot(Cb,b2)
                    Z=z-C#;print('\tz',end='\t');print(z);print('\tz-C',end='\t');print(Z)
                    #zr=np.dot(Cb,b2)
                    u=np.where(np.array(sp.Matrix(b2).T.subs(N,1))[0]<0)[0]
                else:
                    fact=False
                    print('Problema INFACTIBLE')
                    u=[]
                nt+=1
            #pM2(A2);print(b2.T,end='\t');print(Z,end='...problema para optimizar\n')
            if fact:
                v=np.where(np.array(Z[0,:c].subs(N,1000))>0)[0]
                if(len(v)>0):
                    [A2,b2,Bb,nt]=smn(A2,b2,Bb,C,step,nt)
                    Cb=C[0,Bb]
                    z[0,:c]=np.linalg.linalg.matmul(Cb,A2);z[0,c]=np.dot(Cb,b2)
                    tmp=', Al resultado se le aplico Met Simplex Minimizacion'
                    u=np.where(np.array(sp.Matrix(b2).T.subs(N,1))[0]<0)[0]
                    v=[]
                    hst+=h6
                else:
                    tmp=''
                #pM2(A2);print(b2.T,end='\t');print(z-C,end='...problema optimizado, por ver si es factible\n')
                if((len(u)==0)&(len(v)==0)):
                    if (step==1):
                        print('Tabla final (N%s%i)%s'%(chr(176),nt+1,tmp));prnt.Tbl(A2,b2,Bb,z,C,-3,-3);print(hst)
                    elif(step==0):
                        print('La Base Final (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb);print(hst)
                        Xr=sp.zeros(c,1)
                        for i in range(len(b2)):
                            Xr[Bb[i],0]=b2[i]
                        l=[]
                        for i in range(c):
                            globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                            l+=['x%i'%(i+1)]
                        X=np.array(l)
                        #u=np.where(b2!=0)[0]
                        #for i,j in zip(X[Xr[u]],b2[u]):
                        #    print(str(i)+': '+str(j))
                        irnc=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
                        bir=list(np.array(Bb)[irnc])
                        prnt.Tbr(X[bir],np.array(Xr.T)[0][bir],(z-C)[0,c])
    else:
        print('\x1b[043m Problema con Validacion de datos \x1b[0m') 
    return [A2,b2,Bb]

#Metodo simplex Dual maximizacion, operacion por matriz inversa
#s;)
def smxD(A,b,Bb,C,step):
    fact=True
    [f,c]=A.shape
    nt=0
    A2=np.zeros((f,c)).astype(int)
    b2=sp.zeros(f,1)
    #zr=0
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        v6=js.loads('"\\u2502"')
        h6=js.loads('"\\u2500"')
        B=A[:,Bb];B=sp.Matrix(B)
        Cb=C[0,Bb]
        A2=np.linalg.linalg.matmul(B.inv(),A)
        b2=np.dot(B.inv(),b)
        z=sp.zeros(1,c+1); z[0,:c]=np.dot(Cb,A2); z[0,c]=np.dot(Cb,b2)
        Z=z-C
        #zr=np.dot(Cb,b2)
        u=np.where(np.array(sp.Matrix(b2).T.subs(N,1))[0]<0)[0]#;print('b',end='\t');print(b,end='\t');print('u',end='\t');print(u)#;print('A[u,:]');print(A2[u,:])
        v=np.where(np.array(Z[0,:c].subs(N,1000))<0)[0]
        hst=''
        while((fact)&((len(u)>0)|(len(v)>0))):
            if(len(u)>0):
                hst+=v6
            while(len(u)>0):
                fl=u[np.argmin(np.array(sp.Matrix(b2).T.subs(N,1))[0][u])]#;print(A2[fl,:])
                v=np.where(A2[fl,:]<0)[0]#;print('A[fl,:]<0',end='\t');print(v,end='\t');print('A2[fl,:]',end='\t');print(A2[fl,:])
                if(len(v)>0):
                    cl=v[np.argmin(abs(Z[0,list(v)]/A2[fl,v]))]
                    if (step==1):
                        print('TABLA N%s%i'%(chr(176),nt+1));prnt.Tbl(A2,b2,Bb,z,C,fl,cl);input('Siguiente...')#;print('fl y cl:',end='\t');print('%i\t%i'%(fl,cl));print('v y Z[v]/A[fl,v]',end='\t');print(v,end='\t');print(Z[v]/A[fl,v])
                    elif(step==0):
                        print('De la tabla (N%s%i), la base es:'%(chr(176),nt+1),end='\t');print(Bb)
                    Bb[fl]=cl
                    Cb=C[0,Bb]#;print('Bb');print(Bb);print('Cb');print(Cb)#print('C');print(C);
                    B[:,fl]=A[:,cl]
                    A2=np.linalg.linalg.matmul(B.inv(),A)
                    b2=np.dot(B.inv(),b)#;print('b',end='\t');print(b2)#;print('\tb',end='\t')
                    z[0,:c]=np.dot(Cb,A2);z[0,c]=np.dot(Cb,b2); Z=z-C#;print('\tz',end='\t');print(z);print('\tz-C',end='\t');print(Z)
                    #zr=np.dot(Cb,b2)
                    u=np.where(np.array(sp.Matrix(b2).T.subs(N,1))[0]<0)[0]
                else:
                    print('Problema INFACTIBLE');u=[]
                    fact=False
                nt+=1
            if fact:
                v=np.where(np.array(Z[0,:c].subs(N,1000))<0)[0]
                if(len(v)>0):
                    [A2,b2,Bb,nt]=smx(A2,b2,Bb,C,step,nt)
                    Cb=C[0,Bb]
                    z[0,:c]=np.linalg.linalg.matmul(Cb,A2);z[0,c]=np.dot(Cb,b2)
                    tmp=', Al resultado se le aplico Met Simplex Max'
                    u=np.where(np.array(sp.Matrix(b2).T.subs(N,1))<0)[0]
                    v=[]
                    hst+=h6
                else:
                    tmp=''
                if((len(u)==0)&(len(v)==0)):
                    if (step==1):
                        print('Table final (N%s%i)%s'%(chr(176),nt,tmp));prnt.Tbl(A2,b2,Bb,z,C,-3,-3);print(hst)
                    elif(step==0):
                        print('La Base Final (N%s%i) es:'%(chr(176),nt),end='\t');print(Bb);print(hst)
                        Xr=sp.zeros(c,1)
                        for i in range(len(b2)):
                            Xr[Bb[i],0]=b2[i]
                        l=[]
                        for i in range(c):
                            globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                            l+=['x%i'%(i+1)]
                        X=np.array(l)
                        irnc=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
                        bir=list(np.array(Bb)[irnc])
                        prnt.Tbr(X[bir],np.array(Xr.T)[0][bir],(z-C)[0,c])
    else:
        print('\x1b[043m Problema con la validacion de datos')
    return [A2,b2,Bb]

#Metodo simplex Dual minimizacion, solucion por operaciones elementales.
#A:matriz previamente preparada, b:vector de costos, Bb: lista base inicial, C: vector funcion objetivo, step: tabla por paso
#Salida: M:Matriz final, b: Nuevo Vector de costes, zr: Valor final de la funcion objetivo, Xr: resultado de las variables no basicas
#;)
def smnD2(A,b,Bb,C,step):#sin matriz inversa, solo operaciones elementales
    fact=True
    fls.brr(rt,True)
    prob=fls.svL(rt,Bb)
    nt=0
    [f,c]=A.shape
    M=sp.zeros(f+1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        v6=js.loads('"\\u2502"')
        h6=js.loads('"\\u2500"')
        M[:f,:c]=A
        M[:f,c]=b
        M[f,:]=-C
        Cb=C[0,Bb]
        M[f,:]+=np.dot(Cb,M[:f,:])
        u=list(np.where(np.array(M[:f,c].subs(N,1))<0)[0])
        v=list(np.where(np.array(M[f,:c].subs(N,1000))>0)[0])
        hst=''
        while((not prob)&(fact)&((len(u)>0)|(len(v)>0))):
            if(len(u)>0):
                hst+=v6
            while(fact&(len(u)>0)):
                #print('u',end='\t');print(u);print('M[u,c]',end='\t');print(np.array(M[u,c].subs(N,1)).T[0])
                fl=u[np.argmin(np.array(M[list(u),c].subs(N,1)))]#;print('A2[fl.:]',end='\t');print(A2[fl,:])
                v=list(np.where(np.array(M[fl,:c])[0]<0)[0])#;print('M[fl,:c]<0',end='\t');print(np.where(np.array(M[fl,:c])[0]<0)[0])
                if(len(v)>0):
                    cl=v[np.argmin(np.array(M[f,list(v)])[0]/np.array(M[fl,list(v)])[0])]
                    if (step==1):
                        print('TABLA N%s%i'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,M[f,:],C,fl,cl);input('Siguiente... ')
                    elif(step==0):
                        print('De la Tabla (N%s%i), el cambio en la base es:'%(chr(176),nt+1),end='');cmb(Bb,fl,cl)#print(Bb);input('Siguiente...')
                    Bb[fl]=cl
                    prob=fls.svL(rt,Bb)
                    Cb=C[0,Bb]#;print('Bb',end='\t');print(Bb);print('Cb',end='\t');print(Cb)#print('C');print(C);
                    M=ope(M,fl,cl)
                    #z=np.dot(Cb,M[:f,:])
                    u=list(np.where(np.array(M[:f,c].subs(N,1)).T[0]<0)[0])#;print('break?',end='\t');print(u)
                else:
                    print('Problema INFACTIBLE')
                    fact=False
                nt+=1
            if fact:
                v=np.where(np.array(M[f,:c].subs(N,1000))>0)[0]
                if(len(v)>0):
                    [M[:f,:c],M[:f,c],Bb,nt]=smn2(M[:f,:c],M[:f,c],Bb,C,step,nt)
                    Cb=C[0,Bb]
                    M[f,:]=np.linalg.linalg.matmul(Cb,M[:f,:])-C
                    tmp=', Al resultado se le aplico Met Simplex Min'
                    u=np.where(np.array(M[:f,c].subs(N,1))<0)[0]
                    v=[]
                    hst+=h6
                else:
                    tmp=''
                if((len(u)==0)&(len(v)==0)):
                    if (step==1):
                        print('Tabla final (N%s%i)%s'%(chr(176),nt+1,tmp));prnt.Tbl(M[:f,:c],M[:f,c],Bb,M[f,:]+C,C,-3,-3);print(hst)
                    elif(step==0):
                        print('La Base Final (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb);print(hst)
                        Xr=sp.zeros(c,1)
                        for i in range(f):
                            Xr[Bb[i],0]=M[i,c]
                        l=[]
                        for i in range(c):
                            globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                            l+=['x%i'%(i+1)]
                        X=np.array(l)
                        irnc=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])#;print('u',end='\t');print(u)
                        bir=list(np.array(Bb)[irnc])#;print('X',end='\t');print(X[v]);print('Xr.T',end='\t');print(np.array(Xr.T)[0][v],end='\t');print(np.array(Xr.T)[0][1])
                        #for i in range(len(u)):#zip(X[Bb[u]],Xr[Bb[u]]):
                        #    print(str(X[Bb[u[i]]])+': '+str(Xr[Bb[u[i]]]))
                        prnt.Tbr(X[bir],np.array(Xr.T)[0][bir],M[f,c])
    else:
        fact=False
        print('\x1b[042m %s \x1b[0m'%'Problema con datos de entrada')
    return [M[:f,:c],M[:f,c],Bb]


#Metodo Simplex Dual para maximizacion
def smxD2(A,b,Bb,C,step):#sin matriz inversa, solo operaciones elementales
    fact=True
    fls.brr(rt,True)
    prob=fls.svL(rt,Bb)
    nt=0
    [f,c]=A.shape
    M=sp.zeros(f+1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        v6=js.loads('"\\u2502"')
        h6=js.loads('"\\u2500"')
        M[:f,:c]=A
        M[:f,c]=b
        M[f,:]=-C
        Cb=C[0,Bb]
        M[f,:]+=np.dot(Cb,M[:f,:])
        u=list(np.where(np.array(M[:f,c].subs(N,1))<0)[0])
        v=np.where(np.array(M[f,:c].subs(N,1000))<0)[0]
        hst=''
        while((not prob)&(fact)&((len(u)>0)|(len(v)>0))):
            if(len(u)>0):
                hst+=v6
            while(fact&(len(u)>0)):
                #print('u',end='\t');print(u);print('M[u,c]',end='\t');print(np.array(M[u,c].subs(N,1)).T[0])
                fl=u[np.argmin(np.array(M[list(u),c].subs(N,1)))]#;print('A2[fl.:]',end='\t');print(A2[fl,:])
                v=list(np.where(np.array(M[fl,:c])[0]<0)[0])#;print('M[fl,:c]<0',end='\t');print(np.where(np.array(M[fl,:c])[0]<0)[0])
                if(len(v)>0):
                    cl=v[np.argmin(abs(np.array(M[f,list(v)])[0]/np.array(M[fl,list(v)])[0]))]
                    if (step==1):
                        print('TABLA N%s%i'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,M[f,:]+C,C,fl,cl);input('Siguiente... ')
                    elif(step==0):
                        print('De la Tabla (N%s%i), el cambio en la base es:'%(chr(176),nt+1),end=''); cmb(Bb,fl,cl)#print(Bb)#;input('Siguiente...')
                    Bb[fl]=cl
                    prob=fls.svL(rt,Bb)
                    Cb=C[0,Bb]#;print('Bb',end='\t');print(Bb);print('Cb',end='\t');print(Cb)#print('C');print(C);
                    M=ope(M,fl,cl)
                    #z=np.dot(Cb,M[:f,:])
                    u=list(np.where(np.array(M[:f,c].subs(N,1)).T[0]<0)[0])#;print('break?',end='\t');print(u)
                else:
                    print('Problema INFACTIBLE')
                    fact=False
                nt+=1
            if fact:
                v=np.where(np.array(M[f,:c].subs(N,1000))[0]<0)[0]
                if(len(v)>0):
                    [M[:f,:c],M[:f,c],Bb,nt]=smx2(M[:f,:c],M[:f,c],Bb,C,step,nt)
                    Cb=C[0,Bb]
                    M[f,:]=np.linalg.linalg.matmul(Cb,M[:f,:])-C
                    tmp=', Al resultado se le aplico Met Simplex Max'
                    u=np.where(np.array(sp.Matrix(M[:f,c].T.subs(N,1)))<0)[0]
                    v=[]
                    hst+=h6
                else:
                    tmp=''
                if((len(u)==0)&(len(v)==0)):
                    if (step==1):
                        print('Tabla final (N%s%i)%s'%(chr(176),nt+1,tmp));prnt.Tbl(M[:f,:c],M[:f,c],Bb,M[f,:]+C,C,-3,-3);print(hst)
                    elif(step==0):
                        print('La Base Final (N%s%i) es:'%(chr(176),nt+1),end='\t');print(Bb);print(hst)
                        Xr=sp.zeros(c,1)
                        for i in range(f):
                            Xr[Bb[i],0]=M[i,c]
                        l=[]
                        for i in range(c):
                            globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                            l+=['x%i'%(i+1)]
                        X=np.array(l)
                        irnc=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])#;print('u',end='\t');print(u)
                        bir=list(np.array(Bb)[irnc])#;print('X',end='\t');print(X[v]);print('Xr.T',end='\t');print(np.array(Xr.T)[0][v],end='\t');print(np.array(Xr.T)[0][1])
                        #for i in range(len(u)):#zip(X[Bb[u]],Xr[Bb[u]]):
                        #    print(str(X[Bb[u[i]]])+': '+str(Xr[Bb[u[i]]]))
                        prnt.Tbr(X[bir],np.array(Xr.T)[0][bir],M[f,c])
    else:
        fact=False
        print('\x1b[042m %s \x1b[0m'%'Problema con datos de entrada')
    return [M[:f,:c],M[:f,c],Bb]
#==================================== Dual Especial ================================================
def gstB(b,A,Bb):
    rt='.\\ByM.dc'
    if(b):
        if(not fls.xtF(rt)):
            D=dict()
            D['A0']=A
            D['Bb0']=Bb
            D['i']=1
            fls.svD(rt,D)
        else:
            D=fls.lrD(rt); i=D['i']
            i+=1; D['i']=i
            vA='A'+str(i); vBb='Bb'+str(i)
            D[vA]=A; D[vBb]=Bb
            fls.svD(rt,D)

def gstB2(b,NC):
    r=False
    if b:
        rt='.\\tmp\\Bb.dc'
        if(not fls.xtF(rt)):
            D=dict()
            D['i']=1
            D['j']=NC
            fls.svD(rt,D)
        else:
            D=fls.lrD(rt)
            i=D['i']
            j=D['j']
            if(NC-j==1):
                i+=1
            else:
                i-=1
            D['i']=i; D['j']=NC
            fls.svD(rt,D)
            if(i>=7):
                r=True
    return r

def fcp(f,c):
    u=list(np.array(f).astype(str)[0])
    v=list(np.array(c.T).astype(str)[0])
    us=','.join(u); vs=','.join(v)
    return us+'|'+vs+'\n'

def gstB3(b1,b2,M,Bb,ln,rt):
    r1=False
    if(b1):
        rt2=rt[:-3]+'_2'+rt[-3:]
        x=fls.lr2(rt2); l=len(x)
        if(l>7):
            L=fls.lr2(rt)
            r1=True
            for i in range(l):
                if(i==0):
                    j=L.index(x[i])
                else:
                    j0=j
                    j=L.index(x[i])
                    if(j-j0!=1):
                        r1=False
                        break
        fls.svL2(rt2,Bb)
    if(b2):
        rt4=rt[:-3]+'_4'+rt[-3:]
        fls.svL3(rt4,ln)
    #if(b3):
    #    rt6=rt[:-3]+'_6'+rt[-3:]
    #    i=0
    #    if(fls.xtF(rt6)):
    #        d=fls.lrD(rt6)
    #        i=d['i']+1
    #    fls.svM(rt6,M,i)
    return r1

def gstB4(iv,v,M,Bb,rt):
    r=-1
    i=0
    while(i<len(iv)):
        fl=v[iv[i]]
        x=list(np.where(np.array(M[fl,:-1])[0]<0)[0])
        if(len(x)>0):
            B=Bb.copy()
            cl=x[np.argmin(np.array(M[-1,x])[0]/np.array(M[fl,x])[0])]
            B[fl]=cl
            L=fls.isN2(rt)
            if(not fls.isRL2(L,B)):
                r=iv[i]
                break
        i+=1
    return r

def gstB5(ix,x,f,Bb,rt):
    r=-1
    i=0
    while(i<len(ix)):
        B=Bb.copy()
        c=x[ix[i]]
        B[f]=c
        L=fls.isN2(rt)
        if(not fls.isRL2(L,B)):
            r=ix[i]
            break
        i+=1
    return r

def gstB5(ix,x,c,Bb,rt):
    r=-1
    i=0
    while(i<len(iv)):
        B=Bb.copy()
        f=v[iv[i]]
        B[f]=c
        L=fls.isN2(rt)
        if(not fls.isRL2(L,B)):
            r=iv[i]
            break
        i+=1
    return r

#Metodo simplex especial y en mejora
def spxE(M,Bb,mxmn,NC,NI,rtBd):#mxmn: 1 max 0 min
    def gI(Z,mm):
        r=[]
        if(mm==1):
            r=list(np.where(Z<0)[0])
        elif(mm==0):
            r=list(np.where(Z>0)[0])
        return r
    def gI2(vx,mm):
        r=[]
        if(mm==1):
            r=list(np.where(vx==min(vx))[0])
        elif(mm==0):
            r=list(np.where(vx==max(vx))[0])
        return r
    prob=False#fls.svL(rt,Bb)
    Zt=np.array(M[-1,:-1].subs(N,10))[0]
    u=gI(Zt,mxmn)
    while(((NC<NI)|(NI==-1))&(not prob)&(len(u)>0)):
        ims=gI2(Zt[u],mxmn); cl=u[ims[0]]
        v=list(np.where(np.array(M[:-1,cl].T)[0]>0)[0])
        vv=np.array(M[v,-1].T)[0]/np.array(M[v,cl].T)[0]
        ims=gI2(vv,1); fl=v[ims[0]]
        if(len(ims)>1):
            id=gstB6(ims,v,c,Bb,rtBb)
            if(id>=0):
                fl=v[id]
            else:
                print('\x1b[041m No factible \x1b[0m')
        print('T(N%s%i), cambio es:'%(chr(176),NC+1),end=' ');cmb(Bb,fl,cl)
        M=opeE(M,fl,cl)
        Bb[fl]=cl
        prob=fls.svL2(rtBd,Bb) #; prob=gstB2(prob,NC) #gstB(prob,M,Bb)
        Zt=np.array(M[-1,:-1].subs(N,10))[0]
        u=gI(Zt,mxmn)
        NC+=1
    return [M,Bb,len(u)==0,NC]

#Metodo simplex dual especial    
def spxDE(M,Bb,mxmn,pd,NC,NI,ppd,rtBd):#M:matriz de la tabla, Bb:Base,C:objetivo,pd:0-primal 1-dual,NC:iteracion corriente,NI:iteracion max,ppd: |-
    def gI(Z,mm):
        r=[]
        if(mm==1):
            r=list(np.where(np.array(Z.subs(N,10))[0]<0)[0])
        elif(mm==0):
            r=list(np.where(np.array(Z.subs(N,10))[0]>0)[0])
        return r
    def qt(Zv,Fpv,mm):
        r=[]
        if(mm==1):
            r=abs(np.array(Zv)[0]/np.array(Fpv)[0])
        elif(mm==0):
            r=np.array(Zv)[0]/np.array(Fpv)[0]
        return r
    v6=js.loads('"\\u2502"')
    h6=js.loads('"\\u2500"')
    fact=True;prob=False
    if(NC==0):
        fls.brr(rtBd,True)
        prob=fls.svL(rtBd,Bb)
    u=list(np.where(np.array(M[:-1,-1].T.subs(N,1))[0]<0)[0])
    v=gI(M[-1,:-1],mxmn)
    if((len(u)==0)&(len(v)==0)):
        pd=-1
        print('\t\t\t\x1b[043m %s \x1b[0m'%ppd)
    while(((NC<NI)|(NI==-1))&(not prob)&(fact)&((len(u)>0)|(len(v)>0))):
        if(pd==1):
            if(len(u)>0):
                while(((NC<NI)|(NI==-1))&(not prob)&fact&(len(u)>0)):
                    vu=np.array(M[u,-1].subs(N,1).T)[0]
                    ims=np.where(vu==vu[np.argmin(vu)])[0]
                    fl=u[ims[0]]
                    v=list(np.where(np.array(M[fl,:-1])[0]<0)[0])
                    if(len(v)>0):
                        vv=qt(M[-1,v],M[fl,v],mxmn)
                        ims=list(np.where(vv==min(vv))[0])
                        cl=v[ims[0]]
                        if(len(ims)>1):
                            id=gstB5(ims,v,fl,Bb,rtBd)
                            if(id>=0):
                                cl=v[id]
                            else:
                                print('\x1b[041m No factible \x1b[0m')
                        print('T(N%s%i), Q.q.m.v. :\x1b[033m %i \x1b[0m'%(chr(176),NC+1,len(ims)))
                        Bb[fl]=cl
                        prob=fls.svL2(rtBd,Bb) #;prob=gstB3(prob,p2,M,Bb,ln,rtBd) #; prob=gstB2(prob,NC) #gstB(prob,M,Bb)
                        M=opeE(M,fl,cl)
                        u=list(np.where(np.array(M[:-1,-1].subs(N,1)).T[0]<0)[0])
                    else:
                        print('\x1b[041m Problema INFACTIBLE \x1b[0m')
                        fact=False
                    NC+=1
                if((len(u)==0)):
                    pd=0
                    ppd+=v6
            else:
                pd=0
        if((pd==0)&fact&((NC<NI)|(NI==-1))):
            v=gI(M[-1,:-1],mxmn)
            if(len(v)>0):
                [M,Bb,pmr,NC]=spxE(M,Bb,mxmn,NC,NI,rtBd)
                #Cb=C[0,Bb]
                #M[-1,:]=np.linalg.linalg.matmul(Cb,M[:-1,:])-C
                u=np.where(np.array(M[:-1,-1].subs(N,1))<0)[0]
                v=[]
                if pmr:
                    ppd+=h6
                    if(len(u)>0):
                        pd=1
            if((len(u)==0)&(len(v)==0)):
                pd=-1
                print('Base final es: ',Bb)
                print('\t\t\t\x1b[043m %s \x1b[0m'%ppd)
    return [M,Bb,NC,pd,ppd,fact]

def inipD(A,b,mxmn,Bb,C,NI):#Ruta asignada por el mismo modulo
    def grV(A,b,mxmn,Bb,C,NI,rt,dt):
        for i in ['A','b','mxmn','Bb','C','NI']:
            dt[i]=eval(i)
        fls.svD(rt,dt)
    dt=dict()
    grV(A,b,mxmn,Bb,C,NI,rt2,dt)

def iniPD(A,b,mxmn,Bb,C,NI,rtSt):
    def grV(A,b,mxmn,Bb,C,NI,ruta):
        dic=dict()
        for i in ['A','b','mxmn','Bb','C','NI']:
            dic[i]=eval(i)
        fls.svD(ruta,dic)
    grV(A,b,mxmn,Bb,C,NI,rtSt)

#Simplex Dual Especial menu. A:matriz coef,b:costes,mxmn: 0 min 1 maximizacion, Bb: base ini, C:Funcion objetivo,pd: 0-empiezaxprimal 1-xdual,NC:contador,NI:parte(x500),fc:factor(fc*NI),hst:inicio vacio('')'|',rt:ruta,dt:diccionario
def spxDEM(rtSt,rtBd):
    def grV(A,b,Bb,M,mxmn,C,pd,fact,NC,NI,fc,hst,rt,dt):
        for i in ['A','b','Bb','M','mxmn','C','pd','fact','NC','NI','fc','hst']:
            dt[i]=eval(i)
        fls.svD(rt,dt)
    br=np.ones((1,1)).astype(int);Bbc=[]
    fact=True
    if(fls.xtF(rtSt)):
        dt=fls.lrD(rtSt)
        #for k,v in dt.items():
        #    exec(k+'=v')
        #globals().update(dt)#;lrD2(dt)
        A=dt['A'];b=dt['b'];Bb=dt['Bb'];C=dt['C'];NI=dt['NI'];mxmn=dt['mxmn']
        if (len(dt)==6):
            NC=0;pd=1
            fc=1
            hst=''
            M=CvMT(A,b,Bb,C)
            [M,Bb,NC,pd,hst,fact]=spxDE(M,Bb,mxmn,pd,NC,fc*NI,hst,rtBd)
        else:
            if(fact):
                M=dt['M'];pd=dt['pd'];NC=dt['NC'];fc=dt['fc'];hst=dt['hst']
                [M,Bb,NC,pd,hst,fact]=spxDE(M,Bb,mxmn,pd,NC,fc*NI,hst,rtBd)
        if(fact):
            fc+=1
            grV(A,b,Bb,M,mxmn,C,pd,fact,NC,NI,fc,hst,rtSt,dt)
            if(pd==-1):
                print('\x1b[042m Solucion encontrada \x1b[0m')
                br=M[:-1,-1];Bbc=Bb.copy()
                #fls.brF(rt2)
    else:
        print('\x1b[041m No existe el archivo \x1b[0m')
    return [br,Bbc]

#::::::::::::::::::::::::::::::::::: Metodo 2 Fases :::::::::::::::::::::::::::::::
def spx2f(A,b,Ar,Bb,mnmx,C,step,uniq):
    def gI(Z,Ar,mm):
        r=[]
        if(mm==1):
            r=list(set(np.where(Z<0)[0])-set(Ar))
        elif(mm==0):
            r=list(set(np.where(Z>0)[0])-set(Ar))
        return r
    prob=False
    [f,c]=A.shape
    nt=uniq
    M=sp.zeros(f+1,c+1)
    if((len(C)==c+1)&(len(b)==f)&(len(Bb)==f)&(step in range(-1,2))&(f>1)&(c>1)):
        M[:f,:c]=A;M[:f,c]=b
        if(nt==0):
            fls.brr(rt,True)
        prob=False
        Cb=C[0,Bb]
        z=np.linalg.linalg.matmul(Cb,M[:f,:])
        M[f,:]=z-C
        Zt=np.array(M[f,:c].subs(N,100))[0]
        u=gI(Zt,Ar,mnmx)
        while((not prob)&(len(u)>0)):
            cl=u[np.argmax(Zt[u])]
            l=list(np.where(np.array(M[:f,cl].T)[0]>0)[0])
            fl=l[np.argmin(np.array(M[l,c].subs(N,10).T)[0]/np.array(M[l,cl].T)[0])]
            if (step==1):
                print('Tabla N%s%i'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,z,C,fl,cl);input('Siguiente ... ')
            elif(step==0):
                print('De la Tabla (N%s%i), el cambio en la base es:'%(chr(176),nt+1),end=' ');cmb(Bb,fl,cl)#;print(Bb)
            M=ope(M,fl,cl)
            Bb[fl]=cl
            prob=fls.svL(rt,Bb)
            Cb=C[0,Bb]
            z=np.linalg.linalg.matmul(Cb,M[:f,:])
            Zt=np.array(M[f,:c].subs(N,100))[0]
            u=gI(Zt,Ar,mnmx)
            nt+=1
        if (step==1):
            print('Tabla Final (N%s%i)'%(chr(176),nt+1));prnt.Tbl(M[:f,:c],M[:f,c],Bb,z,C,-3,-3)
        elif(step==0):
            print('La Base resultante (N%s%i) es'%(chr(176),nt+1),end='\t');print(Bb)
        elif(step==-1):
            Xr=sp.zeros(c,1)
            for i in range(f):
                Xr[Bb[i],0]=M[i,c]
            l=[]
            for i in range(c):
                globals()['x%i'%(i+1)]=sp.symbols('x%i'%(i+1))
                l+=['x%i'%(i+1)]
            X=np.array(l)
            u=list(np.where(np.array(Xr.subs(N,1).T)[0][Bb]!=0)[0])
            v=list(np.array(Bb)[u])
            prnt.Tbr(X[v],np.array(Xr.T)[0][v],M[f,c])
            print('\x1b[044m %s \x1b[0m'%'::: ~.~ :::')
    else:
        print('\x1b[043m Problema con la validacion de datos \x1b[0m')
    return [M[:f,:c],M[:f,c],Bb,nt]

#Parte del metodo de dos fases minimizacion, primera fase
def smnF1(A,b,Bb,Ar,step): #Ar y Bb: Variable artificial y base, step: -1 no muestra avisos 0: avisos minimos 1: tabla x tabla
    [_,c]=A.shape
    Ct=sp.zeros(1,c+1)#;print(C[0,Ar]);print(np.ones((1,len(Ar))))
    for i in Ar:
        Ct[0,i]=1
    [Ar,br,Bb,nt]=smn(A,b,Bb,Ct,step,0)
    #if(step==1):
    #    Cb=Ct[0,Bb]
    #    z=sp.zeros(1,c+1);z[0,:c]=np.linalg.linalg.matmul(Cb,Ar);z[0,c]=np.dot(Cb,br)
    #    print('Tabla Final (N%s%i) de la %i%s Fase'%(chr(176),nt+1,1,chr(176)))
    #    prnt.Tbl(Ar,br,Bb,z,Ct,-3,-3)
    #elif(step==0):
    #    print('Base final: ',end='\t');print(Bb)
    return [Ar,br,Bb,nt]

def smn2F1(A,b,Bb,Ar,step):
    [f,c]=A.shape
    M=sp.zeros(f+1,c+1)
    Ct=sp.zeros(1,c+1)
    for i in Ar:
        Ct[0,i]=1
    [M[:f,:c],M[:f,c],Bb,nt]=smn2(A,b,Bb,Ct,step,0)
    #if(step==1):
    #    Cb=Ct[0,Bb]
    #    M[f,:]=np.linalg.linalg.matmul(Cb,M[:f,:])-Ct
    #    print('Tabla Final (N%s%i) de la %i%s Fase'%(chr(176),nt+1,1,chr(176)))
    #    prnt.Tbl(M[:f,:c],M[:f,c],Bb,M[f,:]+Ct,Ct,-3,-3)
    #elif(step==0):
    #    print('Base final: ',end='\t');print(Bb)
    return [M[:f,:c],M[:f,c],Bb,nt]

#Metodo simplex minimizacion 2 Fases, A:matriz previamente preparada, b:vector de costos, Bb: lista base inicial, Ar: lista var artificiales, C: vector funcion objetivo
def smn2F(A,b,Bb,Ar,C,step):
    [A2,b2,Bb,nt]=smnF1(A,b,Bb,Ar,step)
    #[_,c]=A2.shape#;print(C,end='\t');print(c,end='\t');print('len(C)\t%i'%len(C[0,:]))
    #ln=list(set(range(c+1))-set(Ar))#;print(ln)
    #An=A2[:,ln[:c]]#;print(An)
    #c=len(ln)-1
    #Cn=C[0,ln]
    #Cn[0,-1]=C[0,-1]#;print(A2)
    [Ar,br,Bb,nt]=spx2f(A2,b2,Ar,Bb,0,C,step,nt+1)#smn(An,b2,Bb,Cn,step,nt+1)#;print(Ar)
    #if(step==1):
    #    Cb=Cn[0,Bb]
    #    z=sp.zeros(1,c+1);z[0,:c]=np.linalg.linalg.matmul(Cb,Ar);z[0,c]=np.dot(Cb,br)
    #    print('Tabla Final (N%s%i) de la %i%s Fase'%(chr(176),nt+1,2,chr(176)))
    #    prnt.Tbl(Ar,br,Bb,z,Cn,-3,-3)
    #elif(step==0):
    #    print('Base final:',end='\t');print(Bb)
    return [Ar,br,Bb]

#Metodo simplex maximizacion 2Fases, A:matriz previamente preparada, b:vector de costos, Bb: lista base inicial, Ar: lista var artificiales, C: vector funcion objetivo
def smx2F(A,b,Bb,Ar,C,step):
    [A2,b2,Bb,nt]=smnF1(A,b,Bb,Ar,step)
    #[_,c]=A2.shape#;print(C,end='\t');print(c,end='\t');print('len(C)\t%i'%len(C[0,:]))
    #ln=list(set(range(c+1))-set(Ar))
    #An=A2[:,ln[:c]]
    #c=len(ln)-1
    #Cn=sp.zeros(1,c+1)#;print(C2[0,:len(C)])
    #Cn=C[0,ln]#;print(A2)
    #Cn[0,-1]=C[0,-1]
    [Ar,br,Bb,nt]=spx2f(A2,b2,Ar,Bb,1,C,step,nt+1)#;print(Ar)
    #if(step==1):
    #    Cb=Cn[0,Bb]
    #    z=sp.zeros(1,c+1);z[0,:c]=np.linalg.linalg.matmul(Cb,Ar);z[0,c]=np.dot(Cb,br)
    #    print('Tabla Final (N%s%i) de la %i%s Fase'%(chr(176),nt+1,2,chr(176)))
    #    prnt.Tbl(Ar,br,Bb,z,Cn,-3,-3)
    #elif(step==0):
    #    print('Base final:',end='\t');print(Bb)
    return [Ar,br,Bb]

def spxEf(M,Ar,Bb,mxmn,Fi,NC,NI):#mxmn: 1 max 0 min, Fi: Fase1 o Fase2, Ar: indices Var Artificiales, C: funcion objetivo, NC: contador, NI: numero de parte ejm (NC/NI~10/100)
    def gI(Z,Ar,Fi,mm):
        r=[]
        if(mm==1):
            r=set(np.where(Z<0)[0])
            if(Fi in[-1,1]):
                r-=set(Ar)
        elif(mm==0):
            r=set(np.where(Z>0)[0])
            if(Fi in[-1,1]):
                r-=set(Ar)
        return list(r)
    prob=False
    if(NC==0):
        fls.brr(rt,True)
    Zt=np.array(M[-1,:-1].subs(N,10))[0]
    u=gI(Zt,Ar,Fi,mxmn)
    while(((NC<NI)|(NI<0))&(not prob)&(len(u)>0)):
        cl=u[np.argmax(Zt[u])]
        l=list(np.where(np.array(M[:-1,cl].T)[0]>0)[0])
        fl=l[np.argmin(np.array(M[l,-1].T.subs(N,10))[0]/np.array(M[l,cl].T)[0])]
        print('T(N%s%i), cambio es:'%(chr(176),NC+1),end=' ');cmb(Bb,fl,cl)
        M=opeE(M,fl,cl)
        Bb[fl]=cl
        prob=fls.svL(rt,Bb)
        Zt=np.array(M[-1,:-1].subs(N,10))[0]
        u=gI(Zt,Ar,Fi,mxmn)
        NC+=1
        if(len(u)==0):
            Fi=-1
    return [M,Bb,Fi,NC]

#;)
def smn2F2(A,b,Bb,Ar,C,step):
    [f,c]=A.shape
    M=sp.zeros(f+1,c+1)
    [M[:f,:c],M[:f,c],Bb,nt]=smn2F1(A,b,Bb,Ar,step)
    #ln=list(set(range(c+1))-set(Ar))
    #c=len(ln)-1
    #M2=sp.zeros(f+1,c+1)
    #M2[:f,:]=M[:f,ln]
    #Cn=C[0,ln]
    [M[:f,:c],M[:f,c],Bb,nt]=spx2f(M[:f,:c],M[:f,c],Ar,Bb,0,C,step,nt+1)#[M2[:f,:c],M2[:f,c],Bb,nt]=smn2f(M2[:f,:c],M2[:f,c],Ar,Bb,Cn,step,nt+1)
    #if(step==1):
    #    Cb=C[0,Bb]
    #    M[f,:]=np.linalg.linalg.matmul(Cb,M[:f,:])-C
    #    print('Tabla Final (N%s%i) de la %i%s Fase'%(chr(176),nt+1,2,chr(176)))
    #    prnt.Tbl(M[:f,:c],M[:f,c],Bb,M[f,:]+C,C,-3,-3)
    #elif(step==0):
    #    print('Base final:',end='\t');print(Bb)
    return [M[:f,:c],M[:f,c],Bb]

#;)
def smx2F2(A,b,Bb,Ar,C,step):
    [f,c]=A.shape
    M=sp.zeros(f+1,c+1)
    [M[:f,:c],M[:f,c],Bb,nt]=smn2F1(A,b,Bb,Ar,step)
    #ln=list(set(range(c+1))-set(Ar))
    #c=len(ln)-1
    #M2=sp.zeros(f+1,c+1)
    #M2[:f,:]=M[:f,ln]
    #Cn=C[0,ln]
    [M[:f,:c],M[:f,c],Bb,nt]=spx2f(M[:f,:c],M[:f,c],Ar,Bb,1,C,step,nt+1)
    #if(step==1):
    #    Cb=Cn[0,Bb]
    #    M2[f,:]=np.linalg.linalg.matmul(Cb,M2[:f,:])-Cn
    #    print('Tabla Final (N%s%i) de la %i%s Fase'%(chr(176),nt+1,2,chr(176)))
    #    prnt.Tbl(M2[:f,:c],M2[:f,c],Bb,M2[f,:]+Cn,Cn,-3,-3)
    #elif(step==0):
    #    print('Base final:',end='\t')
    return [M[:f,:c],M[:f,c],Bb]

def iniP2F(A,b,Ar,Bb,mnmx,C,NI,rt):
    def grV(A,b,Ar,Bb,mnmx,C,NI,ruta):
        dic=dict()
        [_,c]=A.shape
        C1f=sp.zeros(1,c+1)
        for i in Ar:
            C1f[0,i]=1
        M=CvMT(A,b,Bb,C1f);Fi=0
        for i in ['A','M','b','Ar','Bb','mnmx','Fi','C1f','C','NI']:
            dic[i]=eval(i)
        fls.svD(ruta,dic)
    grV(A,b,Ar,Bb,mnmx,C,NI,rt)

def spx2FE(rt2):#Simplex metodo 2 Fases especial Menu (min o max) usa metodo de Simplex de min o max, depenpendiendo de mnmx(0 o 1), ademas depende de las variables NC/NI pensado para ser dividido en varias sesiones y guardar su estado actual
    def grV(A,M,b,Ar,Bb,mnmx,Fi,C1f,C,NC,NI,fc,rt):
        dt=dict()
        if(Fi==0):
            for i in ['A','M','b','Ar','Bb','mnmx','Fi','C1f','C','NC','NI','fc']:
                dt[i]=eval(i)
        else:
            for i in ['A','M','b','Ar','Bb','mnmx','Fi','C','NC','NI','fc']:
                dt[i]=eval(i)
        fls.svD(rt,dt)
    i2f=False;rt1F=False
    br=np.zeros(1).astype(int);Bbc=[]
    if(fls.xtF(rt2)):
        dt=fls.lrD(rt2)
        C1f=np.arange(1)
        A=dt['A'];b=dt['b'];Ar=dt['Ar'];C=dt['C'];NI=dt['NI'];mnmx=dt['mnmx']; M=dt['M'];Bb=dt['Bb'];Fi=dt['Fi']
        if(Fi==0):
            C1f=dt['C1f']
            if(len(dt)==10):
                fc=1;NC=0
            else:
                fc=dt['fc'];NC=dt['NC']
            [M,Bb,Fi,NC]=spxEf(M,Ar,Bb,0,Fi,NC,fc*NI)# Fase 1
            if(Fi==-1):
                Fi=1;C=dt['C']
                Cb=C[0,Bb]
                M[-1,:]=np.dot(Cb,M[:-1,:])-C
                i2f=True
            if((Fi==1)&(NC==fc*NI)):
                rt1F=True
            if((Fi==0)|rt1F):
                fc+=1
            grV(A,M,b,Ar,Bb,mnmx,Fi,C1f,C,NC,NI,fc,rt2)
        if((Fi==1)&(not rt1F)):
            if not i2f:
                fc=dt['fc'];NC=dt['NC']
            [M,Bb,Fi,NC]=spxEf(M,Ar,Bb,mnmx,Fi,NC,fc*NI)#Fase 2
            fc+=1
            grV(A,M,b,Ar,Bb,mnmx,Fi,C1f,C,NC,NI,fc,rt2)
        if(Fi==-1):
            print(' Solucion alcanzada ')
            br=M[:-1,-1];Bbc=Bb.copy()
    else:
        print('\x1b[041m No existe el archivo \x1b[0m')
    return [br,Bbc]

def dsM2F():
    #Metodo 2 Fases minimizacion
    def tst1():
        [A,N0,f]=Ejx6()
        [A,b,d,C]=C2PF(A,N0,f)
        [A,b,Ar,Bb,C]=C2ej(A,b,d,C)
        iniP2F(A,b,Ar,Bb,0,C,-1,rt2)
        spx2FE(rt2)
        spx2FE(rt2)
    #............................
    #Metodo 2 Fases maximizacion
    #iniP2F(A,b,Ar,Bb,1,-C,-1,rt2)
    #spx2FE(rt2)
    #............................
    #Metodo 2 Fases minimizacion
    #[Ar,br,Bb]=smn2F2(A,b,Bb,Ar,C,0)
    #................................................................
    #Metodo 2 Fases maximizacion
    #[Ar,br,Bb]=smx2F2(A,b,Bb,Ar,-C,0)
    #............................
    #Metodo Dual 2 minimizacion
    def tst2():
        [A,N0,f]=Ejx6()
        [A,b,Bb,C]=C2Ej(A,N0,f)
        [_,_,Bb]=smnD2(A,b,Bb,C,-1)
    #............................
    #Metodo Dual 2 maximizacion
    #[Ar,br,Bb]=smxD2(A,b,Bb,-C,0)
    #.........TIMEIT...........................
    import timeit
    st=timeit.default_timer()
    tst2()
    print('Tiempo con esta OE es: %F' %(timeit.default_timer()-st))

#Solucion del problema
def sol(A,br,Bb):
    [f,c]=A.shape
    Xr=sp.zeros(c,1)
    for i in range(f):
        Xr[Bb[i],0]=br[i,0]
    return Xr

def sol2(X,Bb):
    irnc=list(np.where(np.array(X.subs(N,1).T)[0][Bb]!=0)[0])
    bir=list(np.array(Bb)[irnc])
    return bir

#Muestra si es correcto el resultado
def iscs(A,b,br,Bb):
    Xr=sol(A,br,Bb)
    return A*Xr==sp.Matrix(b)

#Para el cambio del primal al Dual considerar la tabla:
#Primal Restriccion (Ri<=bi,Ri>=bi,Ri=bi) --->  Dual variable (yi>=0,yi<=0,yi irrestricta)
#Primal Variable (xi>=0,xi irrestricta) --->  Dual Restriccion (DRi>=ci,DRi=ci)
#--------------------------------------------------------------------------------
#MAX Rp<=0, siempre x>=0 ===>  Rd>=0, siempre y>=0
#MIN Rp>=0, siempre x>=0 ===>  Rd<=0, siempre y>=0