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

**OSS**:
dove stanno le soluzioni ammissibili NON base (ottenuto durante il transitorio di theta) sul politopo? **sullo spigolo tra due vertici (BFS)**
- se la soluzione è degenere c'è il rischio che io rimanaga fermo su un vertice (vedi sotto) 

**casi particolari**
1. **x_0 degenere**
    - theta_max = 0 (non posso spostare la manopola)
    - posso essere sfortunato o fortunato in base a se y_ij è minore o maggiore di zero
        - se sono sfortunato (y_ij > 0): **cambio comunque base**, perchè entra una colonna e ne esce un altra, ma la soluzione non è cambiata siccome la colonna è entrata con theta = 0 
            - ci siamo spostati su una nuova base ma la soluzione non cambia, abbiamo fatto fatica inutile (d'altronde la BFS era degenere)
        - se sono fortunato (y_ij < 0): **theta max è definito dalle altre componenti** 

2. tutti gli y_ij <= 0
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
    - utilizza la funzione obiettivo per definire le variazioni di costo nel fare entrare una determinata una colonna. Estendi il tableau di conseguenza 

...

**Corollario**:
se ci sono due pivot la nuova BFS è degenere dato che con lo stesso theta_max annullo due componenti.
- caso infelice, partiamo da una base non degenere ed arriviamo ad una base degenere, che come abbiamo visto ci può far fare fatica inutile se cambiamo base in maniera che non cambia la BFS








## Tableau
Strumento fondamentale per applicare l'algoritmo

è una rappresentazione di A*x = b
- matrice m*(n+1) la colonna aggiuntiva è b che viene posta come colonna 0

...


elementary row operations lasciano inalterato il sistema
- operazioni gratis che danno un'altra forma al tableau



**voglio che in corrispondenza della base ci sia una matrice identità!** 
- In questo modo non devo far calcoli di inversione per calcolare x0
- crazy, se riesco a fare questa cosa, nella colonna 0 **il vettore dei termini noti mi diventa anche il BFS della base attuale**
    - B^-1*b = x0 -> I\*b = x0 -> b = x0 
- **nelle altre colonne ho i coefficienti y_ij**
    - prodotto tra matrice identità è la colonna Aj di cui voglio trovare i coefficienti 
- rende anche comodo trovare i rapporti y_i0/y_ij! mi basta fare i rapporti sulla stessa riga
    - osserva la comodità della notazione la colonna 0 del tableau è proprio quella della soluzione e la colonna j è proprio quella che voglio far entrare




### Operazioni di pivoting
se cambio base ottengo un nuovo tableau scombinato (non ho la matrice identità nella base) ...

**Metodologia per il cambiamento di base nel tableau**:
1. scelgo una colonna *j* a caso (per adesso) da fare entrare
2. calcolo theta_max ed ottengo la riga del pivot (l = i: min{y_i0/y_ij})
3. divido la riga del pivot per il valore del pivot
    - ottengo la **pivoting row**
4. per tutte le altre righe sottraggo la pivoting row moltiplicata per il valore che c'è adesso sulla colonna che è entrata (y_ij con i!=L) 
    - considero sempre la riga del pivot dato che non agisce mai sulla base (se non sulla colonna che esce)

**NB**: ricorda che esce la colonna di base con indice pari alla riga del pivot data la relazione con theta max

**NB**: non abbiamo ancora un metodo per definire una base iniziale






### come si sceglie la colonna da fare entrare in base?
bisogno non far peggiorare il valore della soluzione 
- dobbiamo considerare la funzione di costo (fino ad ora lasciata da parte)
- per adesso scegliamo una colonna a caso con costo negativo

Facciamo entrare un'unità per volta (theta =1) una colonna fuori base *x_j* (= yij con i da 1 a m) 
- il costo ottenuto si può riscrivere in funzione del costo della BFS iniziale (z0) e delle componenti della nuova soluzione non base x_j 
- chiamiamo **c_j  costo relativo della colonna j** la variazione di costo che si ottiene facendo entrare un'unità di x_j

**NB**: Only columns A_j for which c_j < 0 are profitable! 
- fanno diminuire la funzione di costo
- la funzione di costo dimuinuisce tanto quanto sono le unità di x_j che riesco a fare entrare
    - la nuova soluzione fa diminuire il costo di **theta_max*c_j** 



**Estensione del tableau per tenere conto dei costi relativi**:
1. estendiamo il tableau aggiungendo nella riga 0 l'equazione del costo
2. vogliamo impostare a zero tutti i costi relativi in corrispondenza alle colonne della base
    - fare entrare una colonna della base in base non cambia il costo relativo, c'è gia 
3. operazioni elementari di riga: Subtract each row i, multiplied by cβ(i) , to row 0
    - in questa maniera ottieniamo anche i costi relativi in corrispondenza delle colonne fuori base
    - ed il costo della soluzione corrente, negata


**CRITERIO DI OTTIMALITÀ**:
se tutti i costi relativi delle colonne fuori base sono > 0 -> la soluzione è ottima


We still need:
- a policy to decide which column must enter the base
- a method to obtain an initial BFS

















### Quanto possono essere preoccupanti le soluzioni degeneri?
...

**possono produrre cicli infiniti!** (in base a quali pivoting rules si adottano) 
- Se si incontrano basi degeneri non è detto che l'algoritmo arrivi alla soluzione ottimale, potrebbe entrare in loop!

**bisogna scegliere attentamente le colonne da fare entrare in base.**
- Una mi può portare ad una soluzione degenere, l'altra no



### Regole di pivoting
due decisioni:
1) which column (among those with cj < 0) must enter the base;
2) what to do in case of tie among rows (più pivot).


```
non esiste nessun metodo matematico che ci dice con certezza quale colonna far entrare per far convergere il prima possibile l'algoritmo!  
```

Tuttavia, nel caso medio, una buona idea è scegliere quella con il costo minore (Regola di Dantzig)
- non è solo una buona idea è di gran lunga la scelta migliore che si conosce fino ad oggi
- curiosità: si potrebbe pensare di scegliere la colonna che produce la diminuzione locale migliore possibile... però computazionalmente molto oneroso 
- **regola di bland**: garantisce la convergenza dell'algoritmo but convergence is much slower ⇒ only used to escape loops.
    - the column Aj with minimum index j (among those with cj < 0) enters the base; 
        - interessante non guardiamo il costo relativo
    - in case of tie, the column Aj with minimum index j leaves the base.

L'algoritmo, normalmente userà la regola di Dantzig. Nei casi in cui ci si sta accorgendo di essere in un loop -> switch alla regola di Bland











### Metodo delle due fasi
Rimane da capire come ottenere una BFS di partenza con la matrice identità come base
- difficile a causa delle assunzioni 1 e 2
    - la matrice A deve avere m colonne linearmente indipendenti
    - regione ammissibile non vuota
- forse non esiste una base
- anche se esiste magari la regione ammissibile è vuota

Dobbiamo accorgercene! Cosa fare?

(voglio che il vettore dei termini noti abbia tutti i componenti positivi)


Aggiungo al sistema **_m_** variabili artificiali, ogni riga del sistema passa da x1 + x2 = 3 -> x1 + x2 + xa = 3
- chiaramente non è un operazione elementare di riga, le soluzioni del sistema cambiano

**NB**: sistema "dopato" potrebbe anche andarmi bene se la base non fosse nelle variabili artificiali ma in quelle vere.
- questo perchè le variabili fuori base, e quindi anche quelle artificiali, valgono zero
- come faccio? -> operazioni di pivoting! 

Minimizzo con la stessa strategia vista fino ad adesso **una funzione obiettivo artificiale** che come costo ha la somma di tutte le variabili artificili della soluzione:
- con questa funzione obiettivo cerco soluzioni del mio sistema originale (variabili artificiali hanno somma zero)


Ho tre casi:
1. La funzione obiettivo artificiale minimizzata vale zero e nessuna delle variabili artificiali è in base
    - (caso ottimo) abbiamo ottenuto una BFS per il problema originale
    - passare alla fase 2
2. La funzione obiettivo artificiale minimizzata rimane maggiore di zero
    - è impossibile soddisfare i vincoli del problema senza variabili artificiali
    - non esiste alcuna soluzione ammissibile
    - **assuzione 2 violata**
3. La funzione obiettivo artificiale minimizzata vale zero ma delle variabili artificiali sono in base
    - puzza di degenerazione (le variabili artificiali hanno valore zero)
    - bisogna lavorare

può accadere che la soluzione ottima ha comunque funzione obiettivo maggiore di zero
- Assunzione 2 violata

può anche accadere che il costo sia zero ma che alcune variabili artificiali rimangano comunque in base (situazione degenere)
- corrisponde alla violazione dell'assunzione 1



**fase 2**
uguale a quanto visto prima
- considero per il pivoting solo le colonne riguardanti le variabili autentiche

le variabili artificiale sembrerebbe che possano essere scartate via (semplicistico); in realtà vedremo che saranno utili

introduciamo solamente le variabili artificiali necessarie nella fase 2

i termini noti devono essere positivi? si in questa metodologia a 2 fasi





**Se si verifica il terzo caso: posso eseguire un pivoting speciale anche se l'elemento è negativo dato che ... perchè? chiedi meglio**



non finisce qua! Dobbiamo accorgerci anche della violazione dell'assunzione 1

- potrebbe capitare che non sia possibile trovare un pivot valido per portare fuori la variabile artificiale fuori base
    - questo è il caso che viola l'assunzione 1