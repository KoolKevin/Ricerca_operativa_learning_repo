**NB**: saper risolvere graficamente un problema di programmazione lineare serve anche durante il compito
- con due incognite, azzerane una e considera dove finisce l'altra

...

**NB**: le rette parallele **si spostano nella direzione del gradiente** (capisci bene cosa significa)
- la soluzione ottima di solita si posiziona in un vertice delle spazio ammissibile (perchè) 
- mi interessano solo i vertici? No le soluzioni ottime possono anche risiedere su uno spigolo (ma allora risiedono anche su due vertici)

...

## Forme di programmazione lineare
- sempre coefficienti interi in input (non limitante)
- le x invece (output) possono essere frazionarie






# capisci che cosa rappresentano i e j, m e n
- m numero righe
- n numero colonne

- m numero vincoli
- n numero variabili

...







Rispetto alla forma generale: Problema in forma canonica/standard è un caso notevole
- forma canonica per esempi grafici (ha poche variabili)
- forma standard per algoritmi (algoritmo del simplesso)

Ma algoritmo del simplesso è limitato?

- m >= n non è un caso che fa perdere generalità
    - sistemi con m > n non hanno soluzioni e quindi non ha senso considerarli
    - sistemi con m = n hanno una sola soluzione
    - sistemi con m < n hanno infinite soluzioni (n-m gradi di libertà)

- le 3 forme (generale, canonica, standard) sono poi equivalenti
    - x_j+ e x_j- sono sempre positivi e sostituiscono x_j nel modello (x_j scompare)

**Conclusione**: L'algoritmo del simplesso quindi funziona senza perdità di generalità con problemi in forma standard con m < n


Il problema si risolve invertendo la matrice A -> x = A^-1*b
- la matrice deve essere invertibile!



### Indipendenza lineare

3 caratterizzazioni che verificano l'assenza di indipendenza lineare
- la matrice non è invertibile (singolare, avrei bisogno del determinante a denominatore)



# FONDAMENTALE | Soluzione Base
in pratica rendo quadrato il sistema imponenendo zero come valore di tutte le variabili fuori base


**NB**: L'assunzione delle colonne linearmente indipendenti è un debito! L'algoritmo a cui arriveremo dovrà anche dirmi se l'assunzione non è verificata

**Soluzione base ammissibile**

altre due assunzioni (e relativi debiti)







## Politopi convessi
(sinonimo di poliedro)

un iperpiano divide lo spazio in due sotto-spazi

politopo intersezioni di un numero finito di semi spazi (sta tagliando via con delle machettato le spazio attorno al politopo)
- i vincoli di un problema di programmazione lineare (particolarmente visibile in forma canonica) definiscono uno spazio ammissibile che è un politopo

**terminologia sui politopi**:
l'iperpiano che mi definisce una faccia deve appoggiarsi al politopo su uno spigolo/vertice



combinazione convessa di p punti: 
- generalizzazione
- non più solo i punti appartenenti al segmento che congiunge due punti
- consiste in un tutti i punti che appartengono all'area/volume/spazio in generalre p-1 dimensionale definito dai p punti

**PROP**: Ogni punto di un politopo è una combinazione convessa dei suoi vertici!

**PROP 2**:

Property The constraints of an LP define a polytope.




### Politopi e programmazione lineare:

congiungiamo le due strade (algebriche e geometriche)

Theorem Given the polytope P defined by the constraints of an LP, a necessary and sufficient condition for a point to be a vertex is that the corresponding vector x be a BFS.

- le soluzioni base ammissibili sono vertici del politopo e i vertici del politopo sono soluzioni base ammissibili

ricorda che, intuitivamente, la soluzione ottima si trova guardando i vertici 


per ogni politopo esiste un vertice ottimo
- non abbiamo dimostrato che il punto è un vertice, però il suo valore è ottimo
    - funzione obiettivo parallela ad uno spigolo
    - da qui deriva il corollario

**Abbiamo ottenuto un algoritmo per risolvere tutti i problemi di programmazione lineare!**
- esaminiamo tutti i vertici del politopo
- binomio di newton (m su n) combinazioni di m colonne sulla matrice A (ognuna che calcola l'inversa di una matrice)


**Considerazioni sulle basi**:
- basi degeneri
- basi e BFS distini, BFS distini e basi non necessariamente distinte

Cio che frega è che ci possono essere più zeri di n-m

un'algoritmo pensa di star cambiando vertice cambiando base, ma in realtà può rimanere nello stesso punto e star facendo fatica inutilmente