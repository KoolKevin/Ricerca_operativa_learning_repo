...


nei problemi di programmazione dinamica abbiamo anche un principio di dominanza forte
- utilizzandolo facciamo prima i conto
- ... ma bisogna stare un attimo più attenti a controllare quali sono le coppie dominate







variabili: quintali di composto X e Y 
- x1 e x2
- c_1 = 1; c_2 = 2
- max z = 1*x1 + 2*x2
- x1 + x2 <= 6
- x2 <= x1+1
- x1 >= 1
- x1, x2 >= 0

**forma standard**


max z == min -z 


- min -z = -1*x1 -2*x2
-  x1 + x2 + s1           = 6
- -x1 + x2 +    + s2      = 1
-  x1                - s3 = 1
-  x1, x2, s1, s2, s3 >= 0



