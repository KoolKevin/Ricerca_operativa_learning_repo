### BFS Adiacenti
Quando le basi corrispondenti a due BFS sono diverse per un solo vettore colonna

**Algoritmo del simplesso**:
start with a BFS, and iteratively replace the current BFS with an adjacent BFS having no greater cost, until an optimal BFS is found.
- ad ogni iterazione toglie una colonna dalla base corrente e ne fa entrare un'altra, in maniera tale che la base ottenuta non sia peggiore!
- il valore della soluzione o resta uguale o diminuisce
- come si fa a capire che la base corrente è quella ottima? (vedremo)


### Spostarsi da BFS a BFS
supponiamo x_0 non degenere

- posso ottenere la m+1-esima colonna come combinazione lineare di quelle in base
- nuova relazione che produce *b* con *m+1* colonne con theta che fa da manopola
- ci sarà un theta massimo che mi annulla la prima componente e **mi fa ritornare ad un BFS con m componenti**
- alzo theta **fino a che non trovo una nuova base!** (ricorda che BFS diversi implicano Basi diverse)
    - se alzo troppo e la componente diventa negativo sto uscendo dal politopo, la soluzione non è più ammissibile

- dove stanno le soluzioni ammissibili NON base sul politopo? sullo spigolo tra i due vertici!

**casi particolari**
1. x_0 degenere
    - partiamo con la manopola non mossa ma con il valore già a zero
    - posso essere sfortunato o fortunato in base a se y_ij è minore o maggiore di zero
    - **se sono sfortunato cambio comunque base**, perchè cambio colonna, ma la soluzione non è cambiata  (d'altronde la BFS era degenere)
        - ci siamo spostati su una nuova base ma la soluzione non cambia, abbiamo fatto fatica inutile

2. tutti gli y_ij < 0
    - lo spigolo del politopo va all'infinito
    - l'assunzione 3 è violata 
    - l'algoritmo se ne accorge! Se cambiamo una base e ci ritroviamo in questa situazione il problema è risolto (-inf)


**cosa ci rimane da fare**
- ho tolto una colonna e ne ho fatta entrare un altra, sono linearmente indipendenti? 
    - forse non abbiamo trovato un'altra base
    - in realta è dimostrabile che lo sono
- modo comodo per trovare i valori y_ij
    - con tableau e base trasformata in matrice identità
- come faccio a capire come andare verso un vertice migliore? Devo capire quale colonna far entrare


...

corollario se ci sono due pivot, la nuova BFS è degener
- caso infelice, partiamo da una base non degenere ed arriviamo ad una base degenere






### Tableau
Strumento fondamentale per applicare l'algoritmo

è una rappresentazione di A*x = b
- matrice m*(n+1) la colonna aggiuntiva è b

...


elementary row operations lasciano inalterato il sistema
- operazioni gratis che danno un'altra forma al tableau

**voglio che in corrispondenza della base ci sia una matrice identità!** In modo da non dover far calcoli di inversione
- crazy, se riesco a fare questa cosa nella colonna 0 ho il BFS della base attuale, e nelle altre colonne ho i coefficienti y_ij
- rende anche comodo trovare i rapporti y_i0/y_ij

se cambio base ottengo un nuovo tableau scombinato... che fatica

operazioni:
- divido la riga del pivot per il pivot
- per tutte le altre righe sottraggo la nuova riga del pivot moltiplicata per il valore che c'è adesso sulla colonna(?) 
    - considero sempre la riga del pivot dato che non agisce mai sulla base (se non sulla colonna che esce)

a quanto pare esce la colonna di base con indice pari alla riga del pivot (capisci perchè)
- a quanto pare centra la relazione con theta max


**NB**: non abbiamo ancora un metodo per definire una base iniziale



### come si sceglie la colonna da fare entrare in base?
bisogno non far peggiorare il valore della soluzione -> dobbiamo considerare la funzione di costo (fino ad ora lasciata da parte)
- per adesso scegliamo uno a caso con costo negativo

tutti zero in corrispondenza della base



### Quanto possono essere preoccupanti le soluzioni degeneri?
...

**possono produrre cicli infiniti!**

Se si incontrano basi degeneri non è detto che l'algoritmo arrivi alla soluzione ottimale!

bisogna scegliere attentamente le colonne da fare entrare in base. Una mi può portare ad una soluzione degenere, l'altra no



### Regole di pivoting
due decisioni:

```
non esiste nessun metodo matematico che ci dice con certezza quale colonna far entrare per far convergere il prima possibile l'algoritmo!  
```

Tuttavia, nel caso medio, una buona idea è scegliere quella con il costo minore (Regola di Dantzig)
- infatti è di gran lunga la scelta migliore
- curiosità: si potrebbe pensare di scegliere la colonna che produce la diminuzione locale migliore possibile... però ad ogni passo devo guardare m elementi 
- regola di bland: garantisce la convergenza dell'algoritmo

l'algoritmo, normalmente userà la regola di Dantzig. Nei casi in cui ci si sta accorgendo di essere in un loop -> switch alla regola di Bland





Rimane come capire una BFS di partenza con la matrice identità come base
- difficile a causa delle assunzioni 1 e 2
- forse non esiste una base
- anche se esiste magari la regione ammissibile è vuota

Dobbiamo accorgercene!

### Metodo delle due fasi
...

Aggiungo al sistema m variabili artificiali, ogni riga del sistema passa da x1 + x2 = 3 -> x1 + x2 + xa = 3
- chiaramente non è un operazione elementare di riga, le soluzioni del sistema cambiano

**NB**: sistema "dopato" potrebbe anche andarmi bene se la base non fosse nelle variabili artificiali ma in quelle vere.
- questo perchè le variabili fuori base, e quindi anche quelle artificiali, valgono zero
- come faccio? operazioni di pivoting! 

uso una funzione obiettivo artificiale con cui cerco soluzioni del mio sistema originale (variabili artificiali hanno somma zero)

...


può accadere che la soluzione ottima ha comunque funzione obiettivo maggiore di zero
- Assunzione 2 violata

può anche accadere che il costo sia zero ma che alcune variabili artificiali rimangano comunque in base (situazione degenere)
- corrisponde alla violazione dell'assunzione 1

... struttura tipica dei costi relativi (di quanto varia il costo se faccio entrare la variabili in base (varia quanto il coefficiente))

**fase 2**
le variabili artificiale sembrerebbe che possano essere scartate via (semplicistico)

introduciamo solamente le variabili artificiali necessarie nella fase 2


i termini noti devono essere positivi?? **controlla**

...


nel terzo esempio posso eseguire un pivotin anche se l'elemento è negativo dato che 