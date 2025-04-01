rilassamento continuo del problema
- se il problema è di minimo -> **il valore della soluzione è sicuramente non peggiore**
- ho un vincolo in meno



Ci sono due tecniche per risolvere ILP

### Metodo dei piani di taglio
**def | parte intera di y**: l'intero q : q <= y 


**def | parte frazionaria**: ...


taglio di Gomory: per ogni riga del tableau 
- se voglio inserire nel tableau i nuovi vincoli dei tagli di gomory mi è più comodo moltiplicare per -1 ed aggiungere una variabile di slack
- tutti le feasible integer solution rimangono ammissibili in quanto ho utilizzato delle relazioni già presenti nel tableau (semplicemente abbiamo aggiunto vincoli di interezza)


Dopo aver aggiunto un taglio Abbiamo una soluzione primal unfeasible e dual feasible, **possiamo quindi applicare il simplesso duale**!
- oppure ripartire da zero (ma chiaramente non conviene in quanto "basta che ci spostiamo poco")

anche nella riga zero non vogliamo valori frazionari siccome una combinazione lineare (coefficienti interi) con variabili intere non può produrre un valore frazionario

per disegnare i tagli si fanno delle sostituzioni
- i tagli relativi a relazioni non valide sono inutili nel senso che non eliminano niente

### Metodo branch and bound
molto simile a prima

bisogna scegliere una variabile frazionaria e imporre due condizioni mutamente esclusive (se si verifica una non si verifica l'altra) ed esaustive (non eliminano possibili soluzioni intera)
- in maniera tale da non considerare la parte in mezzo a due soluzioni intere
- da una parte complico il problema dato che invece di un ILP ne devo risolvere due
- dall'altra anche l'unione dei due politopi è più piccola di quella del problema iniziale (devo cercare di meno)


interessante notare come nell'albero lo studio dei lower bound mi aiuta a trovare la soluzione intera potando rami dell'albero (parte di bounding)