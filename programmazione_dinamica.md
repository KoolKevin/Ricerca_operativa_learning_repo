## Programmazione dinamica

**problema subset sum**:
caso particolare di knapsack 0-1 in cui il profitto di ogni oggetto è pari al suo peso

...



**DP per KP01**:
In subset-sum abbiamo che salviamo solamente i valori distinti delle somme nonostante lo stesso valore possa essere prodotto da più sottoinsiemi. Nella versione KP01, dobbiamo considerare anche i pesi e quindi nell'insieme delle soluzioni possibili **inseriamo coppie (dette anche stati)**; chiaramente, se il peso è lo stesso bisogna scegliere la somma con profitto maggiore.

...

Consideriamo la complessità di questo algoritmo:
- n iterazioni (una per variabile)
- ad ogni iterazione, nel caso peggiore scorriamo c+1 elementi di pesi diversi
- **complessità polinomiale n*c??? Ma KP01 non era NP-completo???**
    - (branch and bound richiede 2^n)
- ma in realtà non è polinomiale

ricorda:
- la grandezza di un'istanza è il numero di bit necessari a codificare un input
- distinguiamo quindi tra **dimensione numerica**
    - è il valore numerico dell'input, non della sua rappresentazione
- **dimensione** dell'input
    - È il numero di bit necessari per rappresentare l'istanza del problema.
    - Per KP01, servono circa ⌈log2 c⌉ bit per codificare c.
    - **se c è il valore più grande nell'input**, la dimensione dell'input è proporzionale a log_c (2n*log_c)

... chiedi a Martello ...



### Algoritmi pseudo polinomiali
def: ...


**NB**: interessante notare che la complessità dipende dalla **dimensione** delle entità in gioco
- due problemi con la stessa dimensione dell'input in ingresso ma uno con capacità 10 e l'altro 10^6 hanno tempi drammaticamente diversi
- questo non vale per branch and bound che ci mette sempre 2^n

intuizione: ma allora posso trasformare i problemi NP in subset-sum che è np-completo e pseudopolinomiale, e risolvere questi problemi NP con questa complessità pseudopolinomiale? NO! -> ulteriore differenziazione

### Problemi Fortemente NP-completi
... 

sono quelli che non ammettono pseudopolinominalità (non conviene programmazione dinamica)

**Theorem**
No strongly NP-complete problem can admit a pseudo-polynomial algorithm, unless P = NP.


restrizioni:
...

**nota**: se considero istanza piccole del problema: c <= n -> cn = n^2!









**conclusioni su DP**:
- tecnica generale che produce algoritmi efficienti per problemi che hanno numeri piccoli (esponenziale per problemi fortemente NP-completi)
- per i problemi fortemente np-c gli algoritmi dp sono esponenziali, per i problemi NON fortemente np-c sono pseudo-polinomiali
...
- approcci di DP non sempre conveniente a causa della molta memoria richiesta e molti accessi alla memoria