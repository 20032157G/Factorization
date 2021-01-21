import sympy as sp
import numpy as np
import os.path as opt
import coefs
import smpx
import prnt
import IntCuad
import fls

rtSmD='.\\Resultados\\smsbd.txt' #Archivo de lista de Formulas encontradas por el Metodo Simplex Dual
rtSmF='.\\Resultados\\smsbdf.txt' #Archivo de lista de Formulas encontradas por el Metodo Simplex de 2 Fases
#ruta2='.\\memproc\\vr.bd' #Archivo de diccionario de variables del metodo simplex
rtStP='.\\memproc\\estadoVp.dc' #Archivo de diccionario de variables de programa menu 
rtStS='.\\memproc\\estadoV.dc'
rtBb='.\\memproc\\cmbBs.bd'

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

def iniPD(gx,gy,Fs,Fs2,cmbi,st,rt):
    def grV(gx,gy,Fs,Fs2,cmbi,st,ruta):
        dic=dict()
        for i in ['gx','gy','Fs','Fs2','cmbi','st']:
            dic[i]=eval(i)
        fls.svD(ruta,dic)
    grV(gx,gy,Fs,Fs2,cmbi,st,rt)

def dcsc(s,n):
    if(n>40):
        x=fls.prgrsp(s)
        if(x):
            NI=2000
        else:
            NI=-1
    else:
        NI=-1
    return NI

def fct(i,j,ope,rgst):#i,j orden, ope: en lo posible no operes si es Falso, V de todos modos opera, rgst: (0 o 1) registrar, en caso =1 no sobreescribe, cheat -1 sobrescribe si ope es V
    [ni,nj]=fls.vlnd(i,j)
    Fg=0
    if((ni+nj>=0)&(ni>=0)&(nj>=0)&(rgst in range(-1,2))&(ope in{True,False})):
        flx=fls.isFR(rtSmD,ni,nj,True)
        if((not flx)|(ope&flx)):
            tb=False;inc=False;cnc=False;fact=True
            if(i+j<4):
                tb=True
                Fg=IntCuad.mtbl(i,j)
            else:
                cntr=fls.gstF(rtStS,rtStP)#Ambos existen entonces es V, sino F
                if(cntr):
                    dicc3=fls.lrD(rtStP);dicc2=fls.lrD(rtStS)
                    di=dicc3['gx'];dj=dicc3['gy'];NC=dicc2['NC'];fact=dicc2['fact'];del dicc3,dicc2
                    if((ni!=di)|(nj!=dj)):
                        fct=''
                        if(not fact):
                            fct='Se sugiere borrarlo pues es No Factible'
                        x=fls.prgrsp('\x1b[041m Se encontro un archivo con contenido con %i iteraciones, desea BORRARLO o continuar con aquel de grados: (%i, %i) en otro momento ? s/n\x1b[0m\n%s\t Borrarlo (s) / Conservarlo (n)\t'%(NC,di,dj,fct))
                        del di,dj
                        if(x):
                            fls.brF(rtStS);fls.brF(rtStP)
                            cntr=False
                            fact=True
                        else:
                            cnc=True
                if(not cntr):
                    st=1
                    x,y,N=sp.symbols('x,y,N')
                    print('\x1b[042m %s \x1b[0m'%' ::: INICIO DEL PROGRAMA ::: ')
                    # Hallando la integral sin factor Area
                    sp.pprint(sp.Integral(x**ni*y**nj,x,y))
                    print('\x1b[33m%i)\x1b[0m Hallando la integral ...'%st)
                    fml=IntCuad.intet3(ni,nj)
                    fml=IntCuad.frm2(fml,ni,nj)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Comparando con un factor particular sx^i.sy^j
                    print('\x1b[033m%i)\x1b[0m Comparando el resultado y primera agrupacion ...'%st)
                    fml2=var(ni,nj)
                    [c,l]=coefs.agr(fml,fml2)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Comparacion y ultima agrupacion ...
                    print('\x1b[033m%i)\x1b[0m Ultimo proceso de agrupacion ...'%st)
                    [c,l]=coefs.agrx(c,l)
                    [c,l,f1,f2,f3]=coefs.grps(c,l)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Descubriendo todas las posibles Formulas respecto a los grupos
                    print('\x1b[033m%i)\x1b[0m Proceso de factorizacion por "partes" y revelando todas las posibles formulas ...'%st)
                    Fs=coefs.sms([],ni,nj,0)
                    Fs2=coefs.sms([],ni,nj,1)
                    Fr=coefs.frms(c,l,Fs2)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Verificacion y Tabulacion
                    print('\x1b[033m%i)\x1b[0m Verificando valores y Generando tabla ...'%st)
                    [Fl,Cl]=coefs.rarT(Fr,f1,f2,f3)
                    Fs=[Fs[i]for i in Cl]
                    Fs2=[Fs2[i]for i in Cl]
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Problema de minimizacion
                    print('\x1b[032m%i)\x1b[0m Construyendo Problema de Minimizacion ...'%st)
                    [fl,cl]=Fr.shape
                    N0=sp.zeros(fl,1)#;fl-=1
                    N0[:,0]=N*np.array(c)[Fl];N0=np.array(N0)
                    T=Fr[Fl[:-1],:][:,Cl[:-f1-1]]#;smpx.pM2(T)
                    [A,b,Bb,C]=smpx.C2Ej(T,N0,f1)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Resolviendo el problema
                    print('\x1b[032m%i)\x1b[0m Resolviendo el problema del paso anterior ...'%st)
                    NI=dcsc('\x1b[036m Tiene %i columnas, desea dividirlo en partes s/n \x1b[0m'%(len(Fs)-f1-1),len(Fs))
                    smpx.iniPD(A,b,0,Bb,C,NI,rtStS)
                    iniPD(ni,nj,Fs,Fs2,cl-f1-1,st,rtStP)
                    [br,Bb]=smpx.spxDEM(rtStS,rtBb)
                    del fml,fml2,fl,cl,f1,f2,f3,c,l,Fl,Cl,Fr,N0,C,b,T
                else:
                    dicc2=fls.lrD(rtStS);fact=dicc2['fact']
                    if((not cnc)&fact):
                        dicc3=fls.lrD(rtStP)
                        di=dicc3['gx']
                        dj=dicc3['gy']
                        NC=dicc2['NC']
                        del dicc3,dicc2
                        print('033[H\033[J')#clearscrean
                        [br,Bb]=smpx.spxDEM(rtStS,rtBb)
                dicc2=fls.lrD(rtStS)
                pd=dicc2['pd']
                if((not cnc)&(pd==-1)):
                    N=sp.symbols('N')
                    dicc3=fls.lrD(rtStP);cmbi=dicc3['cmbi'];Fs=dicc3['Fs'];Fs2=dicc3['Fs2'];st=dicc3['st']
                    A=dicc2['A'];del dicc3,dicc2;fls.brF(rtStS)
                    X=smpx.sol(A,br,Bb)
                    iX=smpx.sol2(X,Bb)
                    ix=np.array(iX);ix[ix>cmbi]-=1#;print(iX==ix);print(ix[ix>cl-f1-1])
                    dns=[sp.fraction(1/X[i].subs(N,1))[0]for i in iX]
                    lcm=np.lcm.reduce(dns)
                    for ii in iX:
                        X[ii,0]=X[ii,0].subs(N,lcm)
                    del dns,lcm
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Construyendo Formula gnrl
                    print('\x1b[032m%i)\x1b[0m Construyendo posible formula general ...'%st)
                    Fg=0;FG=0#;print(len(Fs),len(Fs2),end='\t');print(ix,iX)
                    for ii in range(len(iX)):
                        Fg+=Fs[ix[ii]]*X[iX[ii]]
                        FG+=Fs2[ix[ii]]*X[iX[ii]]
                    del Fs,Fs2,cmbi
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Comprobando
                    print('\x1b[031m%i)\x1b[0m Verificando resultados obtenidos ...'%st)
                    FG=sp.expand(FG)#;print(FG)
                    Ir=IntCuad.intet3(ni,nj)
                    inc=IntCuad.correcto2(Ir,FG,ni,nj)
            if((tb|inc)&(not cnc)):
                if(inc):
                    print('\x1b[042m >>> Formula desarrollada con exito despues de %i pasos <<< \x1b[0m'%st)
                rp2=''
                if((rgst==-1)&flx): #Caso unico sobreescribir
                    fls.svF(rtSmD,str(Fg),ni,nj,True)
                    rp2='sobreescrita'
                elif((rgst in [-1,1])&(not flx)): #Caso registra y no sobreescribe
                    fls.svF(rtSmD,str(Fg),ni,nj,False)
                    rp2='registrada'
                elif(rgst!=0): #Caso unico, integral registrada y opcion solo registra (no sobreescribe)
                    print('\x1b[033m Formula en el registro \x1b[0m')
                else: #Caso restante es cuando, dentro del universo, rgst=0 y es opera no+
                    print(' No se registro, pues los parametros fueron: \x1b[031m fct(%i,%i,%s,%i)\x1b[033m y 4to parametro rgst=0 es no registrar \x1b[0m'%(ni,nj,ope,rgst))
                if((rgst!=0)&((not flx)|(rgst!=1))):
                    rp=' >>> \x1b[042m Formula %s con exito \x1b[0m <<<'
                    if fls.isFR(rtSmD,ni,nj,True):
                        print(rp%rp2)
                print('\x1b[044m ::: FIN ::: \x1b[0m')
            else:
                if(fact&(not cnc)):
                    dicc2=fls.lrD(rtStS);pd=dicc2['pd'];del dicc2
                    if(pd==-1):
                        print('\x1b[041m ___ FORMULA ERRONEA ___ \x1b[0m')
                    else:
                        print('\x1b[037m Operacion incompleta, ejecutar fct(%i,%i,False,%i) \x1b[0m'%(ni,nj,1))
        else:
            #print('\x1b[031m No hay proceso para realizar respecto a los parametros ingresados \x1b[0m ')
            Fg=sp.sympify(fls.rdI(rtSmD,ni,nj));print('\x1b[033m Formula en el registro \x1b[0m')
    return Fg

def fct2(i,j,ope,rgst):#i,j orden, ope: en lo posible no operes si es Falso, V de todos modos opera, rgst: (0 o 1) registrar, en caso =1 no sobreescribe, cheat -1 sobrescribe si ope es V
    [ni,nj]=fls.vlnd(i,j)
    Fg=0
    if((ni+nj>=0)&(ni>=0)&(nj>=0)&(rgst in range(-1,2))&(ope in{True,False})):
        flx=fls.isFR(rtSmF,ni,nj,True)
        if((not flx)|(ope&flx)):
            tb=False;inc=False;cnc=False
            if(i+j<4):
                tb=True
                Fg=IntCuad.mtbl(i,j)
            else:
                cntr=fls.gstF(rtStS,rtStP)#Ambos existen entonces es V, sino F
                if(cntr):
                    dicc3=fls.lrD(rtStP);dicc2=fls.lrD(rtStS)
                    di=dicc3['gx'];dj=dicc3['gy'];NC=dicc2['NC'];del dicc3,dicc2
                    if((ni!=di)|(nj!=dj)):
                        x=fls.prgrsp('\x1b[041m Se encontro un archivo con contenido con %i iteraciones, desea BORRARLO o continuar con aquel de grados: (%i, %i) en otro momento ? s/n\x1b[0m\n%s\t Borrarlo (s) / Conservarlo (n)\t'%(NC,di,dj,fct))
                        del di,dj
                        if(x):
                            fls.brF(rtStS);fls.brF(rtStP)
                            cntr=False
                        else:
                            cnc=True
                if(not cntr):
                    st=1
                    x,y,N=sp.symbols('x,y,N')
                    print('\x1b[042m %s \x1b[0m'%' ::: INICIO DEL PROGRAMA ::: ')
                    # Hallando la integral sin factor Area
                    sp.pprint(sp.Integral(x**ni*y**nj,x,y))
                    print('\x1b[33m%i)\x1b[0m Hallando la integral ...'%st)
                    fml=IntCuad.intet3(ni,nj)
                    fml=IntCuad.frm2(fml,ni,nj)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Comparando con un factor particular sx^i.sy^j
                    print('\x1b[033m%i)\x1b[0m Comparando el resultado y primera agrupacion ...'%st)
                    fml2=var(ni,nj)
                    [c,l]=coefs.agr(fml,fml2)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Comparacion y ultima agrupacion ...
                    print('\x1b[033m%i)\x1b[0m Ultimo proceso de agrupacion ...'%st)
                    [c,l]=coefs.agrx(c,l)
                    [c,l,f1,f2,f3]=coefs.grps(c,l)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Descubriendo todas las posibles Formulas respecto a los grupos
                    print('\x1b[033m%i)\x1b[0m Proceso de factorizacion por "partes" y revelando todas las posibles formulas ...'%st)
                    Fs=coefs.sms([],ni,nj,0)
                    Fs2=coefs.sms([],ni,nj,1)
                    Fr=coefs.frms(c,l,Fs2)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Verificacion y Tabulacion
                    print('\x1b[033m%i)\x1b[0m Verificando valores y Generando tabla ...'%st)
                    [Fl,Cl]=coefs.rarT(Fr,f1,f2,f3)
                    Fs=[Fs[i]for i in Cl]
                    Fs2=[Fs2[i]for i in Cl]
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Problema de minimizacion
                    print('\x1b[032m%i)\x1b[0m Construyendo Problema de Minimizacion ...'%st)
                    [fl,cl]=Fr.shape
                    N0=sp.zeros(fl,1)#;fl-=1
                    N0[:,0]=N*np.array(c)[Fl];N0=np.array(N0)
                    T=Fr[Fl[:-1],:][:,Cl[:-f1-1]]
                    [A,b,d,C]=smpx.C2PF(T,N0,f1)
                    [A,b,Ar,Bb,C]=smpx.C2ej(A,b,d,C)
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Resolviendo el problema
                    print('\x1b[032m%i)\x1b[0m Resolviendo el problema del paso anterior ...'%st)
                    NI=dcsc('\x1b[036m Tiene %i columnas, desea dividirlo en partes s/n \x1b[0m'%(len(Fs)-f1-1),len(Fs))
                    smpx.iniP2F(A,b,Ar,Bb,0,C,NI,rtStS)
                    iniPD(ni,nj,Fs,Fs2,cl-f1-1,st,rtStP)
                    [br,Bb]=smpx.spx2FE(rtStS)
                    del fml,fml2,fl,cl,f1,f2,f3,c,l,Fl,Cl,Fr,N0,C,b,T
                else:
                    if(not cnc):
                        dicc3=fls.lrD(rtStP);dicc2=fls.lrD(rtStS)
                        di=dicc3['gx']
                        dj=dicc3['gy']
                        NC=dicc2['NC']
                        del dicc3,dicc2
                        print('033[H\033[J')#clearscrean
                        [br,Bb]=smpx.spx2FE(rtStS)
                dicc2=fls.lrD(rtStS)
                if((not cnc)&(len(Bb)>0)):
                    N=sp.symbols('N')
                    dicc3=fls.lrD(rtStP);cmbi=dicc3['cmbi'];Fs=dicc3['Fs'];Fs2=dicc3['Fs2'];st=dicc3['st']
                    A=dicc2['A'];del dicc3,dicc2;fls.brF(rtStP)
                    X=smpx.sol(A,br,Bb)
                    iX=smpx.sol2(X,Bb)
                    dns=[sp.fraction(1/X[i].subs(N,1))[0]for i in iX]
                    lcm=np.lcm.reduce(dns)
                    for ii in iX:
                        X[ii,0]=X[ii,0].subs(N,lcm)
                    rst=False
                    if(cmbi in iX):
                        rst=True
                        iX.remove(cmbi)
                    ix=np.array(iX);ix[ix>cmbi]-=1
                    del dns,lcm
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Construyendo Formula gnrl
                    print('\x1b[032m%i)\x1b[0m Construyendo posible formula general ...'%st)
                    Fg=0;FG=0#;print(len(Fs),len(Fs2),end='\t');print(ix,iX)
                    for ii in range(len(iX)):
                        Fg+=Fs[ix[ii]]*X[iX[ii]]
                        FG+=Fs2[ix[ii]]*X[iX[ii]]
                    if rst:
                        Fg-=Fs[-1]*X[cmbi]
                        FG-=Fs2[-1]*X[cmbi]
                    del Fs,Fs2,cmbi,rst
                    print('>>>>>>>>>>>> Fin del paso %i'%st);st+=1
                    # Comprobando
                    print('\x1b[031m%i)\x1b[0m Verificando resultados obtenidos ...'%st)
                    FG=sp.expand(FG)#;print(FG)
                    Ir=IntCuad.intet3(ni,nj)
                    inc=IntCuad.correcto2(Ir,FG,ni,nj)
            if((tb|inc)&(not cnc)):
                if(inc):
                    print('\x1b[042m >>> Formula desarrollada con exito despues de %i pasos <<< \x1b[0m'%st)
                rp2=''
                if((rgst==-1)&flx): #Caso unico sobreescribir
                    fls.svF(rtSmF,str(Fg),ni,nj,True)
                    rp2='sobreescrita'
                elif((rgst in [-1,1])&(not flx)): #Caso registra y no sobreescribe
                    fls.svF(rtSmF,str(Fg),ni,nj,False)
                    rp2='registrada'
                elif(rgst!=0): #Caso unico, integral registrada y opcion solo registra (no sobreescribe)
                    print('\x1b[033m Formula en el registro \x1b[0m')
                else: #Caso restante es cuando, dentro del universo, rgst=0 y es opera no+
                    print(' No se registro, pues los parametros fueron: \x1b[031m fct(%i,%i,%s,%i)\x1b[033m y 4to parametro rgst=0 es no registrar \x1b[0m'%(ni,nj,ope,rgst))
                if((rgst!=0)&((not flx)|(rgst!=1))):
                    rp=' >>> \x1b[042m Formula %s con exito \x1b[0m <<<'
                    if fls.isFR(rtSmF,ni,nj,True):
                        print(rp%rp2)
                print('\x1b[044m ::: FIN ::: \x1b[0m')
            else:
                if(not cnc):
                    dicc2=fls.lrD(rtStS);Fi=dicc2['Fi'];del dicc2
                    if(Fi==-1):
                        print('\x1b[041m ___ FORMULA ERRONEA ___ \x1b[0m')
                    else:
                        print('\x1b[037m Operacion incompleta, ejecutar fct(%i,%i,False,%i) \x1b[0m'%(ni,nj,1))
        else:
            #print('\x1b[031m No hay proceso para realizar respecto a los parametros ingresados \x1b[0m ')
            Fg=sp.sympify(fls.rdI(rtSmF,ni,nj));print('\x1b[033m Formula en el registro \x1b[0m')
    return Fg

def fctt(i,j):
    Fg=0
    if(not fls.isFR(rtSmD,i,j,True)):
        st=1;pd=1;tb=False;slc=False
        if(i+j<4):
            tb=True
            Fg=IntCuad.mtbl(i,j)
        else:
            N=sp.symbols('N')
            print(prnt.clt('%i) Iniciando el programa ...'%st,37));st+=1
            [rtsts,_]=fls.pRt(i,j,'SesionS','dc');[rtstp,_]=fls.pRt(i,j,'SesionP','dc');[rtdb,_]=fls.pRt(i,j,'CmB','bd')
            if((not fls.xtF(rtsts))|(not fls.xtF(rtstp))|(not fls.xtF(rtdb))):
                if(fls.idF(i,j)):
                    [Fs,Fs2]=fls.lrF(i,j)
                else:
                    Fs=coefs.sms([],i,j,0)
                    Fs2=coefs.sms([],i,j,1); Fs2=[sp.expand(i)for i in Fs2]
                    fls.grF(i,j,Fs,Fs2)
                if(fls.idT(i,j)):
                    [T,f1,f2,f3,c]=fls.lrT(i,j)
                else:
                    [c,l]=coefs.sgG(i,j)
                    [c,l]=coefs.agrx(c,l)
                    [c,l,f1,f2,f3]=coefs.grps(c,l)
                    T=coefs.frms2(c,l,Fs2)
                    fls.grT(i,j,T,f1,f2,f3,c)
                [F,C]=coefs.rarT(T,f1,f2,f3)
                Fs=[Fs[i]for i in C]
                Fs2=[Fs2[i]for i in C]
                
                print(prnt.clt('%i) Construyendo el P.O. '%st,37));st+=1
                [fl,cl]=T.shape
                N0=sp.zeros(fl,1)
                N0[:,0]=N*np.array(c)[F];N0=np.array(N0)
                T=T[F[:-1],:][:,C[:-f1-1]]
                del F,C,fl,f2,f3
                [A,b,Bb,C]=smpx.C2Ej(T,N0,f1)
                print(prnt.clt('%i) Resolviendo el P.0. '%st,37));st+=1
                NI=4000
                
                smpx.iniPD(A,b,0,Bb,C,NI,rtsts); D=fls.lrD(rtsts); fls.svD('.\\memproc\\iniPS.dc',D)
                iniPD(i,j,Fs,Fs2,cl-f1-1,st,rtstp)
                [br,Bb]=smpx.spxDEM(rtsts,rtdb); l=[]
                del c,l,cl,f1,T,N0,A,b,C,NI
            else:
                [br,Bb]=smpx.spxDEM(rtsts,rtdb)
            ds=fls.lrD(rtsts);pd=ds['pd']
            if(pd==-1):
                if(not tb):
                    fls.brF(rtdb)
                print(prnt.clt('%i) Fin del P.O. '%st,37));st+=1
                dp=fls.lrD(rtstp);cmbi=dp['cmbi'];Fs=dp['Fs'];Fs2=dp['Fs2'];st=dp['st']
                A=ds['A'];del dp,ds;fls.brF(rtsts)
                X=smpx.sol(A,br,Bb)
                iX=smpx.sol2(X,Bb)
                ix=np.array(iX);ix[ix>cmbi]-=1
                dns=[sp.fraction(1/X[i].subs(N,1))[0]for i in iX]
                lcm=np.lcm.reduce(dns)
                for ii in iX:
                    X[ii,0]=X[ii,0].subs(N,lcm)
                del dns,lcm

                print(prnt.clt('%i) Formula gnral ...'%st,37));st+=1
                Fg=0;FG=0
                for ii in range(len(iX)):
                    Fg+=Fs[ix[ii]]*X[iX[ii]]
                    FG+=Fs2[ix[ii]]*X[iX[ii]]
                del Fs,Fs2,cmbi

                FG=sp.expand(FG)
                if(fls.idI(i,j)):
                    Ir=fls.lrI(i,j)
                    slc=IntCuad.correcto4(Ir,FG)
                else:
                    Ir=IntCuad.intet3(i,j)
                    slc=IntCuad.correcto2(Ir,FG,i,j)
        if(tb|((pd==-1)&slc)):
            if(not tb):
                print(prnt.clt('%i) Solucion correcta, procediento a registrarla ... '%st,42))
            fls.svF(rtSmD,str(Fg),i,j,False)
            if(fls.isFR(rtSmD,i,j,True)):
                print(prnt.clt('_-_ Registrada _-_',42))
    else:
        Fg=fls.rdI(rtSmD,i,j)
    return Fg