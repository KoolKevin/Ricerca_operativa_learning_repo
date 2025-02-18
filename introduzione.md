la ricerca operativa ha varie definizioni

a noi ci interessa risolvere problemi di decisione al fine di ottenere il migliore risultato possibile (problemi di ottimizzazione)

ma se il sistema è influenzato dal dalle persone, è possibile prevedere il loro comportamento?
- es. di teoria dei giochi

ci siamo convinti che i problemi decisionali possono essere trattai scientificamente
- metodo scientifico
- modelli (regole?) e sistemi


**metodo induttivo vs meduto deduttivo**
- tacchino induttivo
- cambia la prospettiva, non abbiamo più leggi assolute, piuttosto abbiamo dei modelli che possono essere stressati tramite delle deduzioni di preduzioni. Se il risultato vero non coincide con quello del modello, allora il modello è sbagliato


sistema: entità composta da tante parti che interagiscono tra di loro
- modelli descrivono sistemi

modelli matematici analitici difficilmente applicabili per problemi decisionali
- non ci sono soluzioni in formula chiusa

**modelli numerici**: programmazione lineare, grafi e simulazioni

modelli statici vs dinamici: sistemi senza/con dipendenza del tempo


### Origine storica della ricerca operativa
ricerca operativa nome infelice, meglio teoria delle decisioni

...




## di che problemi ci occuperemo nel corso? 
1) simulazione:
    - i parametri del sistema non sono stabili -> no soluzione analitica!!!
    - si risolve un problema tramite simulazione!
    - notare i passaggi e le retroazioni

2) programmazione lineare (15 ore):
    - funzione obiettivo da massimizzare/minimizzare
    - vincoli su questa funzione
    - modello di programmazione lineare è un modello in cui: sia funzione obiettivo, che vincoli, sono espressi da funzioni lineari
    - algoritmo del simplesso
        - il più importante algoritmo nell'area dell'ottimizzazione (computazionalmente efficiente)

Perché "programmazione"?
Il termine "programmazione" in questo contesto deriva dal significato originale della parola, che si riferisce alla **pianificazione** strategica piuttosto che alla scrittura di programmi informatici.

Negli anni '40, quando la programmazione lineare è stata sviluppata (soprattutto grazie a George Dantzig con il metodo del simplesso), il termine "programmare" significava pianificare in modo ottimale l'uso delle risorse disponibili per raggiungere un obiettivo. Questo era particolarmente utile in ambito militare ed economico, dove si cercava di ottimizzare la distribuzione delle risorse.

3) programmazione lineare intera:
    - tengo fermi i candidati, considero tutte le permutazioni, scelgo quella che minimizza il costo
        - costo computazionale spropositato -> permutazioni
    - problemi con una struttura combinatoria non si risolvono tramite enumerazione(detta anche brute-force)
    - ogni riga/colonna ha tutti zeri ed un uno (ogni compito può essere assegnato ad un solo impiegato e viceversa) 
    - di nuovo vincoli e funzione obiettivo sono lineari, però le variabili sono intere
    - non sembra una differenza drammatica rispetto alla programmazione lineare normale ma in realtà lo è (problema dell'assegnazione). MOLTO PIù DIFFICILE

4) problemi di scheduling 
    - ILP -> integer linear programming

5) problemi su grafi | circuito ottimo
    - vogliamo visitare tanti nodi col viaggio più breve possibile
    - migliaia di problemi di ottimizzazione possono essere modellati tramite grafi
        - grafi come strumento di modellazione