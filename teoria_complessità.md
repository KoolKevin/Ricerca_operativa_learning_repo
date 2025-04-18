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

For most optimization problems no polynomial-time algorithm is known (ma non significa che non esista).
- It is widely **conjectured** that such algorithm cannot exist.
- congettura molto valida dato che se riuscissimo a trovare anche solo una soluzione polinomiale ad uno qualsiasi delle decine di migliaia di problemi di ottimizzazione con complessità esponenziale (la maggior parte), allora è dimostrato che automaticamente tutti potrebbero essere risolti polinominalmiente 
- invece, non se ne è ancora riuscito a trovare nessuno tra tutte queste migliaia in 70+ anni

**Complexity theory provides a rigorous treatment of these issues.**




...



Complexity theory, which has been developed for problems in RV (dato che sono più semplici da trattare), also holds for problems in OV.
- siccome i problemi RV hanno la stessa complessità dei problemi OV, una forma o un altra fa poca differenza e quindi quanto detto sopra non è limitativo


## Classi P e NP
- P = class of all problems in RV for which ∃ a Polinomial-time algorithm
    - (equivalently, problems that are solvable in polynomial time by a deterministic Turing machine).
- NP = class of all problems in RV such that **if the solution is “yes”** then **it can be certified in polynomial time**   -  
    - (equivalently, problems solvable in polynomial time by a non-deterministic Turing machine),
    - (equivalently, problems solvable through a branch-decision tree of polynomial height).

**NB**: If a problem is in NP, the existence of a polynomial-time algorithm **cannot be ruled out**.

i problemi di classe P sono quelli risolubili in tempo polinomiale
- risolivbili da una MdT deterministica

la classe NP **non sta per non-polinomiale**
- problemi in forma RV per cui **se la risposta è si** può essere certificata in tempo polinomiale  (da un algoritmo deterministico)
    - la risposta no la lasciamo stare più difficile (mi ricorda decidibilità)

**NB**: la maggioranza dei problemi di ottimizzazione combinatoria ricade in NP 




**MdT det vs non det**
- una MdT det. dopo ogni operazione ha una singola operazione che può eseguire
- non det. ha più istruzioni possibili dopo ogni istruzione eseguita, inoltre ha un oracolo che suggerisce l'istruzione che porta alla soluzione ottima
    - oracolo mi dice sempre la mossa giusta (caso migliore)



**Quand'è che un problema non appartiene neanche ad NP?**
- quando anche con l'oracolo, non ottengo la certificazione in tempo polinomiale
- crazy problema

**A noi interessano problemi della classe NP**
- per questi problemi non si può escludere una soluzione polinomiale, e quindi siamo motivati a cercarla
    - albero decisionale con altezza polinomiale
    - potrebbe esistere un algoritmo intelligente con cui possiamo simulare oracolo che ci salva dalla esponenzialità del problema

**Complessità superpolinomiale**:
- Per i problemi in NP, non è noto se esista un algoritmo deterministico polinomiale per trovare la soluzione 
    - (cioè, non sappiamo se P=NP, se ne trovo uno lo trovo per tutti... vedi dopo).
- Attualmente, gli algoritmi noti per molti problemi NP hanno complessità esponenziale.

**Relazione tra P e NP**:
- chiaramente P⊆NP
- Tutti i problemi risolvibili in tempo polinomiale deterministicamente possono anche essere certificati in tempo polinomiale (produco direttamente la risposta corretta).

La domanda aperta è se P=NP.
- Se fosse vero, significherebbe che i problemi in NP possono essere risolti efficientemente anche senza "indovinare" con un oracolo la soluzione.




**In sintesi** 
- NP non implica che gli unici algoritmi noti siano superpolinomiali, ma che al momento non conosciamo algoritmi deterministici polinomiali per i problemi in NP.
- La definizione si concentra sulla verificabilità polinomiale delle soluzioni, non sulla loro generazione.




### Trasformazioni polinomiali
Un problema A appartenente ad NP si dice trasformabile in tempo polinomiale in un altro problema B appartenente ad NP se esiste un algoritmo polinomiale che, per ogni istanza (input specifico del problema) di A è in grado di definire un'istanza di B che ha come risposta "si" se e solo se l'istanza di A di partenza aveva soluzione "si"
- non è detto che il mapping sia uno ad uno: possono esistere istanza di B che hanno risposta si a cui non corrispondono istanze di A. 

In pratica si sta dicendo che ogni istanza di A si può trasformare in una istanza di un più generale problema B in tempo polinomiale. Risolvendo il l'istanza di B si risolve anche listanza di A 
- A è una sorta di caso particolare del problema B

**NB**: Se esiste un algoritmo polinomiale per risolvere B allora automaticamente ne esiste uno anche per A (prima si trasforma A e poi si applica l'algoritmo di B)


### problemi NP-completi
Un problema A appartenente ad NP, si dice NP completo se:
- per ogni B appartenente ad NP
- B è trasformabile in tempo polinomiale in A

Insomma, A è NP completo se ogni altro problema NP si può ridurre a lui in tempo polinomiale.
- A è il problema NP più generale possibile
- **NB**: se esiste un algoritmo polinomiale per A allora ne esiste uno polinomiale per tutti i problemi in NP!
    
**è un problema potentissimo**
- posso trasformare qualunque altro problema della classe NP in tempo polinomiale
    - qualunque altro problema si riduce a lui
    - posso vedere qualsiasi problema NP come caso particolare di un dato problema NP completo
- se riuscissi a trovare un algoritmo polinomiale che risolve il problema NP-completo allora riuscirei a risolvere tutti i problemi NP in tempo polinomiale!!!
- questi problemi sono ancora più difficili di quelli NP normali in quanto se trovo una soluzione per un NP-completo la trovo per tutti gli NP, mentre se risolvo polinominialmente uno NP normale quelli NP-completi rimangono non affetti



**Incredibile**: si è scoperto che quasi tutti i problemi di ottimizzazione per cui non si possiede un algoritmo polinomiale sono np-completi

**Problemi aperti**: alcuni problemi non si sa se sono NP-completi oppure solo NP:
- appartengono ad NP
- ma non si è riuscito a dimostrare la NP completezza 


**esempi di problemi NP-completi**:
- KP01 (in forma RV)
- e quindi (sicco KP01 è un caso speciale, non c'è neanche bisogno di trasformare) anche i seguenti sono NP-completi
    - 0-1LP 
    - ILP
    - MILP

La programmazione lineare generale non è NP-completa (appartiene a P, vedi dopo)

**Ripetiamo**:
A polynomial-time algorithm for a single (any!) NP-complete problem would produce a polynomial-time algorithm for all NP problems, i.e., it would prove that P = NP. However, in the last 60 years nobody has been able to find such an algorithm, hence most mathematicians and computer scientists believe that its existence is unlikely.

On the other hand, formally proving that P ̸= N P is considered by many to be impossible with the current mathematical knowledge.

nota: La versione ottimizzazione di un problema NP-C viene detta NP-Hard (differenza più linguistica che altro



### Complessità della programmazione lineare
il simplesso ha complessità m*log(n) nella maggior parte delle istanza ma 2^n per caso peggiore e quindi non rende LP appartenente a P

Tuttavia, per la programmazione lineare è stato scoperto un algoritmo polinomiale e quindi è dimostrato che appartiene a P 
