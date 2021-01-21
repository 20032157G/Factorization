import sympy as sp
import numpy as np
import os#.path as opt
import pickle as pk
from zipfile import ZipFile as ZF
#import re
#ruta='D:\\Dcmts\\2020\\test.bd'
sls=['s','n','yes','no','si','no','afirmativo','negativo','S','N','YES','NO','Yes','No','Si','No','SI','NO','Afirmativo','Negativo','Affirmative','Negative','afirmative','negative','AFIRMATIVO','NEGATIVO']
hd=' >>> Formulas para Integracion Numerica 2D en una region triangular <<< '
ffr=list('0123456789-+=*sxy ')
cv=list(set(hd))+list('I-d')+ffr
#num=re.compile('[0-9]')
def n1(i):
    r=0
    if (i>0):
        r=1-i//i**2
    return r

def spn(n):#formula suma de los n primeros numeros
    return n*(n+1)//2

def feg(g):#formula numero de elementos de un grado
    return g+1

def feG(g):#Formula numero de elementos acumulada
    return spn(feg(g))

def fint(x):
    r=x
    lx=list(str(x))
    if(lx[0]=='0'):
        b=False
        i=0
        while(i<len(lx)):
            if(lx[i]!='0'):
                b=True
                break
            i+=1
        if(not b):
            r=0
        else:
            r=int(''.join(lx[i:]))
    return r

def vst(l):#validar string
    l2=[l[i][:-1]for i in range(len(l))]
    s=list(set(''.join(l2)))
    r=False
    if(len(s)>0):
        l=list(s)
        r=True
        c=0
        while(r&(c<len(l))):
            if not(l[c]in cv):
                r=False
            c+=1
    return r

def isnm(x): #si es un numero especifico
    sx=str(x) 
    r=False
    if(len(sx)>0):      
        nms=list('0123456789')
        smb=['.']
        lx=list(sx)
        r=True
        i=0
        while(i<len(lx)):
            if not(lx[i] in nms+smb):
                r=False
                break
            i+=1
        if(r):
            np=lx.count(smb)
            if(np>1):
                r=False
            elif(np==1):
                idp=lx.index(smb)
                if(idp!=1):#if((idp==0)|(idp==len(lx)-1)):
                    r=False
    return r

def isin(x): #reemplaza isinstance(i,int)
    sx=str(x) 
    r=False
    if(len(sx)>0):      
        nms=list('0123456789')+['-']
        lx=list(sx)
        r=True
        i=0
        while(i<len(lx)):
            if not(lx[i] in nms):
                r=False
                break
            i+=1
        if r:
            nn=lx.count('-')
            if(nn>0):
                if((nn>1)|(lx[0]!='-')):
                    r=False
    return r

def vlnd(i,j):#Validar indices
    ii=-1
    jj=-1
    if(isin(i)&isin(j)):
        if((int(i)>=0)&(int(j)>=0)):
            ii=int(i)
            jj=int(j)
    #mn=min(i,j);mx=max(i,j)
    #if(mn<0):
    #    r=False
    #elif(mn<1):
    #    r=mn%1==0
    #    if(r):
    #        if(mx<1):
    #            r=(mx%1==0)
    #        else:
    #            r=mx%1==1
    #else:
    #    r=(mn%1==1)&(mx%1==1)
    return [ii,jj]

def prgrsp(s):
    x=input(s)
    while(not(x in sls)):
        x=input(s)
    return sls.index(x)%2==0

def eps(e,v,asc):#encontrar posicion, asumiendo v ordenado por booleano asc
    n=len(v)
    r=-1
    if(n>0):
        i=0
        while(i<n):
            if((not asc)&(e>=v[i])|asc&(e<=v[i])):
                r=i
                break
            i+=1
    return r

def frm(i,j):
    #def f(cnd,r1,r2):
    #    return (1-cnd)*r2+cnd*r1
    r=''
    if((i>=0)&(j>=0)):
        M=max(i,j)
        if(M==0):
            r=''
        else:
            r=n1(i+1)*('x'+str(i)*n1(i))+n1(j+1)*('y'+str(j)*n1(j))#f(i//M,'x%i'%i,'x')+f(j//M,'y%i'%j,'y')
        r='I{}'.format(r)
    return r

def bsU(i,j,le):#Buscar ubicacion,-1:no hay grado mayor,-2:emcuentra lo mismo,>=0:indice
    r=-2
    l=len(le);ilo=[]
    if(l==0):
        r=0
    else:
        if((i>=0)&(j>=0)&((i>0)|(j>0))):
            m=np.array(le);m1=m[:,0];m2=m[:,1]
            if(sum(m1+m2==i+j)==l):
                M=np.array([max(m[i,:])for i in range(l)])
                u=np.argsort(m1)[::-1]
                v=u[np.argsort(M[u])]#indices de orden 2 criterios como sorted(le,key=lambda x:(sum(x),x[1]))
                if(sum([le[v[i]]==le[i]for i in range(l)])!=l):
                    ilo=list(v)
                    print('\x1b[041m No esta ordenada la lista ... \x1b[0m')
                mx=max(i,j)
                ii=eps(mx,M[v],True)#;print(ii)#primer indice para q M[]>=mx
                if(ii>=0):
                    if(mx==M[v[ii]]):
                        ib=v[list(np.where(M[v]==mx)[0])]
                        ii=eps(i,m1[ib],False)#;print(ii)#buscar situacion cuando m1[]>i
                        if(ii>=0):
                            if(i==m1[ib[ii]]):
                                r=-2
                            else:
                                r=ib[ii]
                        else:
                            if(ib[-1]<l-1):
                                r=ib[-1]+1
                            else:
                                r=-1
                    else:
                        r=ii
                else:
                    r=-1
            else:
                print('\x1b[041m Lista con problemas de orden de grados \x1b[0m (Integrales con grados fuera de contexto)')
    return [r,ilo]

def rdiI(s):#Leer Indices de integral Ix3y3
    i=-1;j=-1
    def ixy(li,l):
        try:
            r=l.index(li)
        except:
            r=-1
        return r
    def gn(l,ii,jj):
        try:
            r=int(''.join(l[ii:jj]))
        except:
            r=1
        return r
    if(len(s)>0):
        l=list(s)
        #ns=list(np.arange(10).astype(str))
        xy=[ixy('x',l),ixy('y',l)]
        ix=n1(xy[0]+2)
        iy=n1(xy[1]+2)
        i=ix*gn(l,xy[0]+1,(1-iy)*len(l)+iy*xy[1])
        j=iy*gn(l,max(2,xy[1]+1),len(l))
    return [i,j]

def rdI(ruta,i,j):#Leer Integral especifica
    r=''
    if((i>=0)&(j>=0)):
        with open(ruta,'r') as fl:
            L=fl.readlines()
        #[c0,lii]=srN(L,0,i,j,-1)
        [li,_]=srN(L,0,i,j,1)
        if(li[0]>0):
            r=L[li[0]].split('=')[1].strip()
        else:
            print('\x1b[041m Formula no registrada \x1b[0m')
    return r

def srg(l,g,esp):
    r=False
    ll=l.split()
    if(ll[0]=='grado'):
        if((not esp)|esp&(int(ll[1])==g)):
            r=True
    return r

def srG(L,g):
    r=-1
    c=0
    while(c<len(L)):
        if(srg(L[c],g,True)):
            r=c
            break
        c+=1
    return r

def srn(l,i,j,esp):
    r=False
    ll=l.split()
    ld=['-','=','>']
    if(ll[0]!='grado'):
        if not(ll[0][0] in ld):
            lb=rdiI(ll[0])
            if((esp==1)&(lb[0]==i)&(lb[1]==j)):
                r=True
            elif((esp==0)&(sum(lb)==i+j)):
                r=True
    else:
        if((esp==-1)&(int(ll[1])==i+j)):
            r=True#;print(ll[1],i+j)
    return r

def rp1t(L,c0):#retroceder por 1er tipo
    r=-1
    if((len(L)>0)&(c0>1)&(c0<len(L))):
        c=c0
        while((c>1)&(L[c][0]=='I')):
            c-=1
        r=c+1-c//c0
    return r

def srN(L,c0,i,j,esp):#search Numero (i,j) en lista empezando desde c0 especimicamente, depende de esp 
    r=[-1];r2=[];le=[]#esp: 1-lista con 1 item de (i,j), 0-lista con lineas de Integrales de grado (i+j), -1 lista con lineas "grado"
    c=rp1t(L,c0)
    while(c<len(L)):
        if(srn(L[c],i,j,esp)):
            r2+=[c]
            le+=[rdiI(L[c].split('=')[0])]
            if(esp==1):
                break
        else:
            if(len(r2)>0):
                break
        c+=1
    if(len(r2)>0):
        r=[r2,le]
    return r

def isFR(ruta,i,j,esp):#esta formula registrada
    b=False
    if((i>=0)&(j>=0)):
        try:
            with open(ruta,'r') as fl:
                for li in fl:
                    if((esp)&(srn(li,i,j,1))|(not esp)&(srg(li,i+j,True))):
                        b=True
                        break
        except:
            b=False
    return b

def frv(Fg):
    r=False
    if(len(str(Fg))>0):
        r=True
        l=list(set(str(Fg)))
        i=0
        while(i<len(l)):
            if not(l[i]in ffr):
                r=False
                break
            i+=1

    return r

def svF(ruta,Fg,i,j,rsb):
    if(frv(Fg)):
        spr='------------------------------------------------------------------------'
        spr2='grado {}'.format(i+j)
        fr='{} = {}'.format(frm(i,j),str(Fg))
        hd2='========================================================================'
        cnt=lr2(ruta)
        if(len(cnt)<2):#Caso archivo vacio
            with open(ruta,'w')as fl:
                fl.write(hd+'\n')
                fl.write(hd2+'\n')
                fl.write(spr2+'\n')
                fl.write(fr+'\n')
                fl.write(spr+'\n')
        else:#Caso archivo con contenido
            ii=srG(cnt,i+j)#;print(ii)
            if(ii>0):#Se encuentra el grado
                [lI,le]=srN(cnt,ii,i,j,0)
                [ii,ile]=bsU(i,j,le)
                if(len(ile)>0):
                    c=0
                    ax=[cnt[lI[i]]for i in range(len(ile))]
                    while(c<len(ile)):
                        cnt[lI[c]]=ax[ile[c]]
                        #lI=ile[lI[0]]
                        c+=1
                    ax.clear()
                if(ii>=0):
                    cnt.insert(lI[ii],fr+'\n')
                elif(ii==-1):
                    if(lI[-1]<len(cnt)-1):
                        cnt.insert(lI[-1]+1,fr+'\n')
                    else:
                        cnt.append(fr+'\n')
                elif(ii==-2):
                    if(rsb):
                        idx=np.where(np.array(le)[:,0]==i)[0][0]
                        if(len(ile)>0):
                            idx2=lI[ile[idx]]
                        else:
                            idx2=lI[idx]
                        cnt.remove(cnt[idx2])
                        cnt.insert(idx2,fr+'\n')
                        sbc='sobreescrita'
                    else:
                        sbc='registrada'
                    print('\x1b[041m Formula %s \x1b[0m'%sbc)
            else:#No se encuentra el gdo
                c=0
                l=[]
                while(c<len(cnt)):#ultima posicion o aquella q sea mayor inmediato al gdo
                    if srg(cnt[c],i+j,False):#(cnt[c].split()[0]=='grado'):
                        l=[c,int(cnt[c].split()[1])]
                        if(l[1]>i+j):
                            break
                    c+=1
                if(len(l)>0):
                    if(l[1]>i+j):#caso grado mayor
                        cnt.insert(l[0],spr+'\n')
                        cnt.insert(l[0],fr+'\n')
                        cnt.insert(l[0],spr2+'\n')
                    else:#Caso grado menor
                        cnt.append(spr2+'\n')
                        cnt.append(fr+'\n')
                        cnt.append(spr+'\n')
                else:
                    print('\x1b[041m %s \x1b[0m'%'El archivo ha sido alterado ...')
                    x=prgrsp('Desea borrar y empezar una nuevo s/n')
                    if(x):
                        cnt=[]
                        cnt.append(hd+'\n')
                        cnt.append(hd2+'\n')
                        cnt.append(spr2+'\n')
                        cnt.append(fr+'\n')
                        cnt.append(spr+'\n')
            with open(ruta,'w')as fl:
                fl.writelines(cnt)
    return

def isN(rt):
    cnt=[]
    try:
        with open(rt,'r') as fl:
            cnt=fl.readlines()
    except:
        print('\t\t...\x1b[031m no se puede leer \x1b[0m ...')
    return cnt

def isN2(rt):
    lns=[]
    if os.path.exists(rt):
        with open(rt,'r')as fl:
            lns=fl.readlines()
    return lns

def isRL(ruta,L):
    cnt=isN(ruta)
    enc=False
    if(len(cnt)>0):
        enc=False
        nmsc=set(L.split(','))
        i=0
        while(i<len(cnt)):
            nms=set(cnt[i][:-1].split(','))
            if(nms==nmsc):
                enc=True
                break
            i+=1
    return enc

def isRL2(lns,L):
    r=False
    if(len(lns)>0):
        i=0
        while(i<len(lns)):
            ln=[int(j) for j in lns[i][:-1].split(',')]
            if(ln==L):
                r=True
                break
            i+=1
    return r

def isRM(D,M):
    r=False
    j=0
    while(j<=D['i']):
        nmj='M'+str(j)
        Mj=D[nmj]
        if(M==Mj):
            r=True
            break
        j+=1
    return r

def svL(ruta,L):
    Le=list(np.array(L).astype(str)); Le=','.join(Le)
    cnt=isN(ruta)
    rg=False
    if(len(cnt)>0):
        rg=isRL(ruta,Le)
    if(not rg):
        cnt.append(Le+'\n')
        with open(ruta,'w')as fl:
            fl.writelines(cnt)
    return rg

def svL2(rt,L):
    lns=isN2(rt)
    r=isRL2(lns,L)
    if(not r):
        l=list(np.array(L).astype(str)); l=','.join(l)
        lns.append(l+'\n')
        with open(rt,'w')as fl:
            fl.writelines(lns)
    return r

def svL3(rt,L):
    lns=isN2(rt)
    r=L in lns
    if(not r):
        lns.append(L)
        with open(rt,'w')as f:
            f.writelines(lns)
    return r

def svM(rt,M,i):
    r=False
    if(not xtF(rt)):
        D=dict(); nM='M'+str(i)
        D[nM]=M; D['i']=i
    else:
        D=lrD(rt)
        r=isRM(D,M)
    if not r:
        nm='M'+str(i)
        D[nm]=M; D['i']=i
        svD(rt,D)
    return r

def brr(ruta,rpta):
    x=False
    if not rpta:
        x=prgrsp('\x1b[041m %s \x1b[0m'%' ATENCION: Are you sure to erase the record? s/n (s: el registro se borrara, n: se mantiene) ')
    if(rpta|x):
        with open(ruta,'w'):
            if(not rpta):
                print(' ))) Borrado (((\t\t\x1b[043m :( \x1b[0m')

def lr(ruta):#lee e imprime
    if(xtF(ruta)):
        with open(ruta,'r')as fl:
            for li in fl:
                print(li,end='')
    else:
        print('El Archivo no se encuentra : '+ruta)

def lr2(ruta):#lee y retorna
    try:
        l=[]
        with open(ruta,'r')as fl:
            l=fl.readlines()
        return l
    except:
        return ''

def lrf(ruta):
    L=lr2(ruta)
    if(len(L)>0):
        i=0
        while(i<len(L)):
            l=L[i][:-1]
            if(srg(l,0,False)):
                g=int(l.split()[1])
                [_,le]=srN(L,i,0,g,0)
                if(len(le)==feg(g)):
                    pt='\x1b[031m%s\x1b[0m'
                else:
                    pt='%s'
                print(pt%l)
            else:
                print(l)
            i+=1

def cnvF(F):
    return sp.sympify(F)

def xtF(rt):
    return os.path.exists(rt)

def brF(rt):#Borrar archivo
    if(os.path.exists(rt)):
        os.path.os.remove(rt)

def svD(rt,dt):#Grabar diccionario
    with open(rt,'wb')as fl:
        pk.dump(dt,fl,pk.HIGHEST_PROTOCOL)

def lrD(rt):#Leer diccionario
    cnt=''
    if os.path.exists(rt):
        with open(rt,'rb')as fl:
            cnt=pk.load(fl)
    return cnt

def pRt(i,j,nm,xt):
    cnf=str(i)+'_'+str(j)
    rt='.\\memproc\\'+nm+cnf+'.'+xt
    return [rt,cnf]

def prpV(i,j,tg,s1,s2):
    [rt,cnf]=pRt(i,j,tg,'dc')
    S1='';S2=''
    if(xtF(rt)):
        D=lrD(rt)
        S1=s1+cnf
        S2=s2+cnf
    return [D,S1,S2]

def prpV2(i,j,tg,s1,s2):
    [rt,cnf]=pRt(i,j,tg,'dc')
    S1=s1+cnf
    S2=s2+cnf
    return [rt,S1,S2]

def idG(i,j):#Esta definido Grupo?
    b=False
    [rt,_,l]=prpV2(i,j,'G','c','l')
    if xtF(rt):
        D=lrD(rt)
        if(l in D):
            b=True
    return b

def idG2(i,j,rt):#Esta definido Grupo?
    b=False
    if xtF(rt):
        D=lrD(rt)
        l='l'+str(i)+str(j)
        if(l in D):
            b=True
    return b

def lrG(i,j):#Leer Diccionario
    c=[];l=[]
    [D,cs,ls]=prpV(i,j,'G','c','l')
    if(len(D)>0):
        c=D[cs];l=D[ls]
    return [c,l]

def lrG2(i,j,rt):
    c=[];l=[]
    [rt,cs,ls]=prpV2(i,j,'G','c','l')
    if(xtF(rt)):
        D=lrD(rt)
        if(len(D)>0):
            c=D[cs];l=D[ls]
    return [c,l]

def grG(i,j,c,l):
    conf=str(i)+str(j)
    [rt,cs,ls]=prpV2(i,j,'G','c','l')
    D=dict()
    locals()[cs]=c
    locals()[ls]=l
    for i in [cs,ls]:
        D[i]=eval(i)
    svD(rt,D)

def grG2(i,j,c,l,rt):#Guardar Grupo en un archivo como diccionario agregando
    cs='c'+str(i)+str(j)
    ls='l'+str(i)+str(j)
    if(xtF(rt)):
        D=lrD(rt)
    else:
        D=dict()
    locals()[cs]=c
    locals()[ls]=l
    for i in [cs,ls]:
        D[i]=eval(i)
    svD(rt,D)

def idT(i,j):#Existe la tabla?
    b=False
    [rt,T,_]=prpV2(i,j,'T','T','F')
    if xtF(rt):
        D=lrD(rt)
        if(T in D):
            b=True
    return b

def idT2(i,j,rt):#Existe la tabla?
    b=False
    if xtF(rt):
        D=lrD(rt)
        T='T'+str(i)+str(j)
        if(T in D):
            b=True
    return b

def lrT(i,j):#Leer info de Tabla
    T=np.zeros(1).astype(int);f1=0;f2=0;f3=0;c=[]
    [rt,nr]=pRt(i,j,'T','dc')
    if(xtF(rt)):
        D=lrD(rt)
        t='T'+nr; f='F'+nr; c='C'+nr
        T=D[t];F=D[f];C=D[c]
        f1=F[0];f2=F[1];f3=F[2]
    return [T,f1,f2,f3,C]

def grT(i,j,T,f1,f2,f3,C):#guardar info de Tabla en una ruta como diccionario agregando si no esta vacio 
    [rt,nr]=pRt(i,j,'T','dc')
    t='T'+nr; f='F'+nr; c='C'+nr
    D=dict()
    locals()[t]=T
    locals()[f]=[f1,f2,f3]
    locals()[c]=C
    for i in [t,f,c]:
        D[i]=eval(i)
    svD(rt,D)

def gstF(rt1,rt2):#Si existen los dos archivo es V sino F y borrarlos
    r=False
    if(xtF(rt1)):
        if(xtF(rt2)):
            r=True
        else:
            brF(rt1)
            r=False
    else:
        if(xtF(rt2)):
            brF(rt2)
            r=False
    return r

def idI(i,j):
    [rt,s1,_]=prpV2(i,j,'I','I','i')
    b=False
    if(xtF(rt)):
        D=lrD(rt)
        if(s1 in D):
            b=True
    return b

def lrI(i,j):
    I=0
    [D,ic,_]=prpV(i,j,'I','I','I')
    if(len(D)>0):
        I=D[ic]
    return I

def grI(i,j,I):
    [rt,ic,_]=prpV2(i,j,'I','I','i')
    D=dict()
    locals()[ic]=I
    for i in [ic]:
        D[i]=eval(i)
    svD(rt,D)

def idF(i,j):
    [rt,f,g]=prpV2(i,j,'F','F','Fd')
    b=False
    if(xtF(rt)):
        D=lrD(rt)
        if((f in D)&(g in D)):
            b=True
    return b

def lrF(i,j):
    Fs=0;Fs2=0
    [D,f,g]=prpV(i,j,'F','F','Fd')
    if(len(D)>0):
        Fs=D[f];Fs2=D[g]
    return [Fs,Fs2]

def grF(i,j,Fs,Fs2):
    [rt,f,g]=prpV2(i,j,'F','F','Fd')
    D=dict()
    locals()[f]=Fs
    locals()[g]=Fs2
    for i in [f,g]:
        D[i]=eval(i)
        D[i]=eval(i)
    svD(rt,D)

def scF(rt):#Guardar copia de el archivo
    FP='\\'.join(rt.split('\\')[:-1])
    NF=rt.split('\\')[-1]
    L=lr2(rt)
    with open(FP+'\\c'+NF,'w')as fl:
        fl.writelines(L)

def bkp(rtd):
    rto='.\\'
    if(rtd!=rto):
        l=os.listdir(rto)
        with ZF(rtd+'backup.zip','w')as f:
            for i in l:
                if('.'in list(i)):
                    if(i.split('.')[1]=='tmp'):
                        f.write(rto+i)