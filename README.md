# Factorization
The [repository](https://github.com/20032157G/Factorization.git) of this project contains:
- fctrz.py
- coefs.py
- smplx.py
- prnt.py
- fls.py
- IntCuad.py          
The main is `fctrz`, the program try to get a formula for an `2D` integral on a triangle of something like x^m*y^n by simplex optimization methods, obviously for bigger indexes m and n the process will be tedius and dificult for the machine inclusive.
for example : 
* fct(2,2,True,0) => m=n=2, Ope=True (operate as be possible), rgst=0 (this case means do not record the result, -1: is overwrite, 1: it's do record if the result is achieved but only in the case it isn't recorded before)
* fct2(2,2,True,0) => It is almost the same, the difference is that in one try by Dual minimization the other by Two phases minimization methods.

To show table results, after execute and have registered, type: _fls.lrf(rtSmD)_ or _fls.lrf(rtSmF)_ in case of table simplex dual method or simplex Two phases method.
