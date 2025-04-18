### Definizioni:
- **Instance of a problem P** 
    - specific **input** for a numeric case of the problem; (Problem P = (infinite) set of all its instances.)
- **Complexity of an algorithm**
    - measure of the **time** it takes to solve the worst case instance of P; 
- **complexity of a problem P**
    - complexity of the best algorithm for P. 
- **Time**:
    - number of elementary steps, or number of milliseconds on a specific computer, or ... 
    - **Time as a function of the instance size**. 
- **Size of an instance**
    - number of **bits** needed to encode the input 
    - frequently (but not always!) equivalent to the number of values in the input.

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
- risolivbili da una MdT deterministica

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

...

albero decisionale con altezza polinomiale

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



...

Knapsack 0-1 è un problema NP-completo, e quindi ... ILP, MILP e roba sono NP-C


La versione ottimizzazione di un problema NP-C viene detta NP-Hard (differenza più linguistica che altro)


...



### Complessità della programmazione lineare

m*log(n) e 2^n


PL è polinomiale 








## Programmazione dinamica

problema: caso particolare di knapsack 0-1 in cui il profitto di ogni oggetto è pari al suo peso

...

algoritmo DP per knapsack 01
- complessità polinomiale n*c???
- ma branch and bound richiede per 2^n
- ma in realtà non è polinomiale
- ricorda: la grandezza di un'istanza è il numero di bit necessari a codificare un input

**Algoritmi pseudo polinomiali**

**NB**: interessante notare che la complessità dipende dalla **dimensione** delle entità in gioco
- due problemi con la stessa dimensione dell'input in ingresso ma uno con capacità 10 e l'altro 10^6 hanno tempi drammaticamente diversi
- questo non vale per branch and bound che ci mette sempre 2^n




intuizione: ma allora posso trasformare i problemi NP in subset-sum che è np-completo e pseudopolinomiale e risolvere questi problemi in con questa complessità? NO! -> ulteriore differenziazione

### Problemi Fortemente NP-completi
sono quelli che non ammettono pseudopolinominalità (non conviene programmazione dinamica)

restrizioni:
...

se considero c <= n -> cn = n^2!




**conclusioni su DP**:
- tecnica generale che produce algoritmi efficienti per problemi che hanno numeri piccoli
- per i problemi fortemente np-c gli algoritmi dp sono esponenziali, per i problemi NON fortemente np-c sono pseudo-polinomiali
...
- approcci di DP non sempre conveniente a causa della molta memoria richiesta e molti accessi alla memoria
