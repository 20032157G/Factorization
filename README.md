# Factorization
The [repository](https://github.com/20032157G/Factorization.git) of this project contains:
- fctrz.py
- coefs.py
- smplx.py
- prnt.py
- fls.py
- IntCuad.py          
The main is `fctrz`, the program try to get a formula for an integral on a triangle of something like x^m.y^n by simplex optimization methods.
for example : 
* fct(2,2,True,0) => m=n=2, Ope=True (operate as be possible), rgst=0 (this case means do not record the result, -1: is overwrite, 1: is record is result is achieved)     
* fct2(2,2,True,0) => It is almost the same, the difference is that in one try by Dual minimization the other by Two fases minimization.
