una rappresentazione diversa di un qualcosa che ci da delle informazioni non evidenti dalla rappresentazione iniziale. 
- Servirà per PL intera!

**NB**: Il problema duale ha lo stesso valore della soluzione del problema primale

**NB**: duality corresponds to an **involution**, a function that is its own inverse (i.e., such that f(f(x)) = x). Note indeed that, if we apply to the dual the same transformation that produced it, its dual coincides with the original problem.





### Interpretazione algebrica dell'algoritmo del simplesso
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

**conclusione**: è dimostrabile che la base B da cui siamo partite corrisponde ad una BFS ottimale <->  pi' = c'_b*B^-1 è una soluzione ottima al problema duale














...

es. 


la tabella è da imparare a memoria perchè aiuta

x <=> 0 -> variabile libera