### BFS Adiacenti
Quando le basi corrispondenti a due BFS sono diverse per un solo vettore colonna

**Algoritmo del simplesso**:
start with a BFS, and iteratively replace the current BFS with an adjacent BFS having no greater cost, until an optimal BFS is found.
- ad ogni iterazione toglie una colonna dalla base corrente e ne fa entrare un'altra, in maniera tale che la base ottenuta non sia peggiore!
- il valore della soluzione o resta uguale o diminuisce
- come si fa a capire che la base corrente è quella ottima? (vedremo)


### Spostarsi da BFS a BFS
- posso ottenere la m+1-esima colonna come combinazione lineare di quelle in base
- nuova relazione che produce *b* con *m+1* colonne con theta che fa da manopola
- ci sarà un theta massimo che mi annulla la prima componente e **mi fa ritornare ad un BFS con m componenti**
- alzo theta **fino a che non trovo una nuova base!** (ricorda che BFS diversi implicano Basi diverse)
    - se alzo troppo e la componente diventa negativo sto uscendo dal politopo, la soluzione non è più ammissibile