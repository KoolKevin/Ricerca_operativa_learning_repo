### Notazione
- vettori colonna: _x_; per rappresentare un punto nello spazio n-dimensionale
- vettori riga: _x'_; trasposta di un vettore colonna
- matrici m*n A = [a_i,j] per rappresentare sistemi di equazioni lineari
    - con _i_ indice di riga, _j_ indice di colonna
    - A_j -> vettore colonna j-esimo della matrice
    - a_i' -> vettore riga i-esimo
- **interpretazione rossa da tenere a mente**, considero i coefficienti realativi ad una incognita per volta di tutte le equazioni del sistema 

## Problema di ottimizzazione generale
Come si descrive un generale problema di ottimizzazione?

Abbiamo:
- un vettore di *n* variabili decisionali da ottimizzare
    - punto in R_n, appartenente al insieme delle soluzioni possibili F
- un insiemi di soluzioni possibili: F sottoinsieme di *R_n* 
- una funzione obiettivo (costo/profitto) f: F -> R

Il problema di ottimizzazione si esprime come:
- min{f(x); con x appartente ad F} -> minimizzare la funzione obiettivo
- oppure anche trovare x* (**ottimo globale**) tale che f(x*) <= f(x) per ogni altro punto x appartenente a F    

**funzioni profitto**
A volte si vuole massimizzare la funzione obiettivo, nessun problema; massimizzare la funzione obiettivo è equivalente a minimizzare la sua opposta:
- max{f(x)} = - min{-f(x)} 
- la rappresentazione del problema va bene anche in questi casi (massimi e minimi non creano problemi)


### Classificazione dei problemi di ottimizzazione:
Abbiamo tre entità da considerare:
- la funzione obiettivo f(x)
- i vincoli sulle variabili decisionali
    - formati da equazioni(h_j(x) = 0)  e disequazioni (g_i(x) >= 0)

**Programmazione non lineare**
quando f(x), h(x) e g(x) sono funzioni generiche
- conosciame solo algoritmi non efficienti per soluzioni globali/euristiche che possono fallire anche nel trovare una soluzione valide

Noi tratteremo:

**Programmazione convessa**
quando f(x) è convessa, h(x) è lineare e g(x) è concava 
- we know algorithms which can find a local optimum for small- or medium-size problem instances, **but a local optimum is always a global optimum**

**Programmazione lineare**
tutto lineare
- con l'algoritmo del simplesso si trova facilmente l'ottimo globale anche per problemi di dimensione molto grande




**cosa che non centra ma utile da sapere**:
- m =  numero di righe della matrice dei coefficienti = a numero di vincoli 
- norma euclidea = || x || = sqrt(x1^2 + x2^2 + ...)


**intorni**
definizione di intorno (versione generale crazy):
- noi utilizzeremo intorni euclidei (quelli che ti aspetti) e quindi la definizione generale la puoi ignorare

**ottimi locali e ottimi globali**
dato (F, d) e una funzione intorno N, f è un ottimo locale se è un ottimo rispetto ad ogni punto dell'intorno N(f)
- un intorno si dice esatto quando un ottimo locale rispetto a quell'intorno è anche ottimo globale; ovvero è **l'intorno più piccolo possibile che considera l'ottimo globale**



## Programmazione convessa

### insiemi convessi
dati due punti x e y, le **combinazioni convesse** sono l'insieme di vettori z che risiedono nel segmento che congiunge i due punti
- con lambda = 1/2 -> punto di mezzo tra x e y
- più è grande/piccolo lambda -> più tendo verso x/y

**un insieme è convesso** se in qualunque modo io scelga due punti al suo interno, le loro combinazioni convesse appartengono sempre all'insieme
- in qualunque modo scelga i due punti, l'intero segmento appartiene all'insieme

**proprietà insiemi convessi**
- l'intersezione di insiemi convessi è a sua volta un insieme convesso
    - l'intersezione rimane convessa considerando una alla volta gli insiemi da cui proviene

### funzioni convesse
una funzione c da un insieme convesso ai reali, è convessa se c( combinazione convessa di x e y) <= combinazione convessa di c(x) e c(y)
- funzione è convessa su un insieme convesso <=> **costo della combinazione convessa è <= della combinazione convessa dei costi**
- graficamente, dati due punti appartenenti all'insieme convesso, la funzione è convessa <=> non è mai sopra (<=) il segmento che congiunge f(x) con f(y) 

- una funzione è concava se *-c()* è convessa

- notare il <=, **le funzioni lineari sono sempre sia concave che convesse**

### Definizione di programmazione convessa
Consideriamo il problema di minimizzare una funzione convessa su un insieme convesso:

TEOREMA
dato (F, c), con sia F che c convessi, ogni intorno è un intorno esatto (gli ottimi locali sono anche ottimi globali)