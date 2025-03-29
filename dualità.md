una rappresentazione diversa di un qualcosa che ci da delle informazioni non evidenti dalla rappresentazione iniziale. 
- Servirà per PL intera!

**NB**: Il problema duale ha lo stesso valore della soluzione del problema primale

**NB**: duality corresponds to an **involution**, a function that is its own inverse (i.e., such that f(f(x)) = x). Note indeed that, if we apply to the dual the same transformation that produced it, its dual coincides with the original problem.





### Interpretazione algebrica dell'algoritmo del simplesso
Differenza tra: 
- base B        == m colonne linearmente indipendenti della matrice A
- e tableau Y   == la matrice A a cui sono state applicate le operazioni elementari di riga per avere I in corrispondenza della base 

Il tableau si ottiene non solo tramite operazioni elementari di riga ma anche come: Y = B^-1 * A
- le colonne di A corrispondenti alla base si trasformano nella matrice identità

Il vettore dei costo (NON relativi) si ottiene come: z' = c'_beta * B^-1 * A (con ' ad indicare vettore riga)
- costi relativi ...
- criterio di ottimalità ...


**La dualità di un PL emerge dal criterio di ottimalità**:
- per la BFS ottima, il termine c'_b*B^-1 è l'unica incognita (dipende da quel'è la base ottima)
- il resto è un dato del problema
- possiamo allora chiamare c'_b*B^-1 -> **pi'**

abbiamo che pi' per definizione è una soluzione ammissibile al seguente nuovo problema che già puzza di duale:
- pi'*A <= c'  (notare l'uso di vettori riga al posto di vettori colonna)

Se ci inventiamo anche una nuova funzione obiettivo: max pi'*b (scambiamo i termini noti con i costi), ottienamo **il problema duale!**
```
    max pi'*b
    pi'*A <= c'
    con pi' <=> 0 -> variabile libera
```

- costi al posto dei termini noti
- max al posto di min
- termini noti al posto dei costi
- righe e colonne scambiate nella matrice dei vincoli
- un po' di altra roba

**conclusione**: è dimostrabile che la base B da cui siamo partite corrisponde ad una BFS ottimale <->  pi' = c'_b*B^-1 è una soluzione ottima al problema duale


...

es. 


la tabella è da imparare a memoria perchè aiuta

x <=> 0 -> variabile libera


nel problema duale i vincoli sono dati dalle colonne della matrice (e non più dalle righe)

- le relazioni sono tra vincolo primale e variabile duale (e viceversa)
- un vincolo forte primale mi da una condizione debole sulla variabile (e viceversa)



...


per risolvere un problema PL noi abbiamo solo il simplesso come tecnica e quindi il problema duale va trasformato in forma standard





## Dualità forte e dualità debole
che relazione c'è tra problema duale e primale?

**Theorem**
**HP**: If an LP has a finite optimal solution, then
1. its dual has a finite optimal solution; (dualità debole)
    - si può dimostrare vedendo che: **cost in the primal ≥ cost in the dual!**
    - **the dual cannot have an unbounded solution.**
2. the two solutions have the same value
    - questo si vede con un passaggio

La figura spacca: ![alt text](immagini/relazione_soluzione_primale_duale.png)

Relazione slide 11 molto importante:
- le soluzione ammissibili del primale sono >= rispetto alla soluzioni del duale
- le soluzioni del primale non sono ammissibili per il duale anche se gli farebbero gola e viceversa
- intuitivamente: solamente l'ottimo soddisfa sia i vincoli del duale che del primale


**Conclusione**: se il primale ha una BFS ottima allora ce l'ha anche il duale e i loro valori combaciano.
- **Rimangono i casi fuori dall'ipotesi!**


### Relazioni primale-duale:
abbiamo una matrice 3x3 che definisce le possibili coppie di relazioni primale duale
- caso standard è quello visto sopra in cui entrambi hanno un ottimo finito che ha valore coincidente
- non possono essere illimitati entrambi e non può essere che uno ha ottimo finito e l'altro è illimitato  (uno schiaccia l'altro)
    - **cost in the primal ≥ cost in the dual!**
    - oppure basta pensare che il duale del duale è il primale! Se uno ha ottimo finito, anche l'altro ce lo deve avere
- è possibile che i problemi siano **entrambi impossibili**
- è possibile che **uno sia illimitato e l'altro impossibile** (di nuovo, uno schiaccia l'altro)


### Come si interpreta il problema duale?
- al posto del allevatore considero un venditore
- al posto di n cibi considero m pillole con i nutrienti
- al posto di minimizzare la spesa, massimizzo il profitto
- ...

**foto sul telefono**




### Lemma di Farkas
...

se il duale si stacca da zero allora deve per forza deve andare a +inf (altri valori finiti dovrebbero essere uguali nel primale)


### Complementary slackness/condizioni di ortogonalità
fino ad ora sappiamo solo che primale e duale hanno lo stesso valore della soluzione. Ma come faccio a trovare la soluzione del duale (che da quel valore)?
lo strumento ce lo da il seguente teorema

- prodotto tra variabile duale e scarto primale deve valore zero
- viceversa

questo teorema mi da uno strumento potente dato che che se ... (uno dei due termini deve fare zero il che mi porta a delle conclusioni nella soluzione ottima)


**conclusione**: Le condizioni di ortogonoalità ci forniscono la soluzione di un problema data la soluzione del suo duale



### Tableau e informazioni sulla dualità
...

- cj = cj - pi*Aj ma gli Aj sono quelli di una matrice identità
- se moltiplico i due tableua per l'inversa della base ottima ...

...

**conclusione**: il confronto tra il tableau iniziale e il tableua nella sua forma che trova la soluzione ottima mi permette di recuperare la soluzione ottima del problema duale!
- è per questo che non possiamo scartare le variabili artificiali, mi servono per il duale







## Algoritmo del simplesso duale
chiave per risolvere i problemi di PL intera

idea: partiamo da una soluzione duale che è più che ottima per il primale ma che non soddisfa i suoi vincoli. Poi cerchiamo di spostarla nella direzione dell'ammissibilità

Capisci come si scelgono i pivot
- l'unica differenza è che prendiamo dei pivot negativi














## Analisi di sensitività
fino ad ora abbiamo visto la dualità come uno strumento teorico che ci servirà per la PL intera. Vediamo ora come la teoria della dualità ci porta a risolvere anche dei problemi molto pratici!

concetto di **intervallo di confidenza** di un dato in input
- se il dato varia all'interno del suo intervallo **la base** rimane ottima
- **NB**: la base non cambia, la BFS e il suo valore si. Questo però non è un problema in quanto è facilmente ricalcolabile


Andiamo a vedere cosa succede se cambio una valore di _b_ o un costo _c_.
- ho due equazioni nel tableau
- sa cambio b si modifica la soluzione x, ma il criterio di ottimalità rimane soddisfatto! e viceversa!


OSS: se facendo un analisi di sensitività finisco nel caso negativo non è detto che non mi convenga far variare un dato di input, semplicemente devo ricalcolare la soluzione ottima.

### Prezzi ombra
prezzi ombra e funzione obiettivo del problema duale (che mi darà lo stesso valore della funzione obiettivo del primale)




**Algoritmo primale duale da saltare!!!**