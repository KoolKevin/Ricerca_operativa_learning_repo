### Definizioni:

dimensione di un'istanza: il numero di **BIT** ... 
- normalmente però numero di valori
- a quanto pare importante questa distinzioni


...


For most optimization problems no polynomial-time algorithm is known.
- It is widely **conjectured** that such algorithm cannot exist.
- congettura molto valida dato che se riuscissimo a trovare anche solo una soluzione polinomiale ad uno qualsiasi delle decine di migliaia di problemi di ottimizzazione esponenziali (la maggior parte), allora è dimostrato che automaticamente tutti potrebbero essere risolti polinominalmiente 
- invece, non se ne è ancora riuscito a trovare nessuno tra tutte queste migliaia in 70+ anni

**Complexity theory provides a rigorous treatment of these issues.**




...



Complexity theory, which has been developed for problems in RV (dato che sono più semplici da trattare), also holds for problems in OV.
- siccome i problemi RV hanno la stessa complessità dei problemi OV, una forma o un altra fa poca differenza e quindi quanto detto sopra non è limitativo


## Classi P e NP
i problemi di classe P sono quelli risolubili in tempo polinomiale

la classe NP **non sta per non-polinomiale**
- problemi in forma RV per cui **se la risposta è si** può essere certificata in tempo polinomiale (da una MdT non det.) 
    - la risposta no la lasciamo stare più difficile (ricorda decidibilità)


MdT deterministica vs non det
- una MdT det. dopo ogni operazione ha una singola operazione che può eseguire
- non det. ha più istruzioni possibili dopo ogni istruzione eseguita, inoltre ha un oracolo che suggerisce l'istruzione che porta alla soluzione ottima
    - oracolo mi dice sempre la mossa giusta (caso migliore)

Quand'è che un problema non appartiene neanche ad NP?
- quando anche con l'oracolo, non ottengo la certificazione in tempo polinomiale

A noi interessano problemi della classe NP
- per questi problemi non si può escludere una soluzione polinomiale, e quindi siamo motivati a cercarla
- se siamo intelligenti possiamo ottenere un pseudo-oracolo che ci salva dalla esponenzialità del problema



### Trasformazioni polinomiali




### problemi NP-completi
...

**è un problema potentissimo**
- posso trasformare qualunque altro problema della classe NP in tempo polinomiale
    - qualunque altro problema si riduce a lui
    - posso vedere qualsiasi problema NP come caso particolare di un dato problema NP completo
- se riuscissi a trovare un algoritmo polinomiale che risolve il problema NP-completo allora riuscirei a risolvere tutti i problemi NP in tempo polinomiale!!!
- questi problemi sono ancora più difficili di quelli NP normali in quanto se trovo una soluzione per un NP-completo la trovo per tutti gli NP, mentre se risolvo polinominialmente uno NP normale quelli NP-completi rimangono non affetti



...



incredibile: si è scoperto che quasi tutti i problemi per cui non si possiede un algoritmo polinomiale sono np-completi

