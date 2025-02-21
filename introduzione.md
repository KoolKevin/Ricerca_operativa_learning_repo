# Ricerca operativa
application of scientific methods to “decision making problems” which are encountered in any organization in which it is required to manage and coordinate activities and resources so as to obtain the best possible result
- a noi ci interessa risolvere **problemi di decisione** al fine di ottenere il migliore risultato possibile (**ottimizzazione**)
- ricerca operativa nome infelice, meglio **teoria delle decisioni**

ma se il sistema è influenzato dal dalle persone, è possibile prevedere il loro comportamento?
- si
- es. di teoria dei giochi


### metodo scientifico
ci siamo convinti che i problemi decisionali possono essere trattati scientificamente
- metodo scientifico
- modelli (regole?) e sistemi

Science:
- organization of knowledge in a form that allows one to predict the effect of actions.
- Objective: discover rules (**models**) that describe the behavior of a **system**


**metodo induttivo vs metodo deduttivo**
- metodo induttivo: use observations to find general laws and theories    
    - critica: tacchino induttivo
- metodo deduttivo: study the system -> devolop a model -> deduce a prediction -> correct? -> if not itera
    - cambia la prospettiva, non abbiamo più leggi assolute, piuttosto abbiamo dei modelli che possono essere stressati tramite predizioni dedotte dallo studio del sistema.
    - se il risultato vero non coincide con quello del modello, allora il modello è sbagliato


**sistema**: entità composta da tante parti che interagiscono tra di loro
- come possiamo predirre il comportamento di un sistema?

**modelli**: semplificazione della realtà inventata per lo studio di un sistema (schemi che descrivono sistemi)
- modelli fisici
- modelli matematici: descrizione sotto forma di formule matematiche/logiche
    - modelli matematici analitici: sistemi di equazioni con una soluzione espressa da una formula
        - difficilmente applicabili per problemi decisionali
    - **modelli matematici numerici**: modelli di programmazione lineare, simulazione (e grafi)
        - quelli di interesse per il corso
        - la soluzione si esprime tramite algoritmi e computer che li computano

i modelli si classificano ulteriormente in
- modelli statici:    sistemi senza dipendenza dal tempo (programmazione lineare, grafi)
- modelli dinamici:   sistemi con dipendenza del tempo (simulazione)



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

Perché "programmazione"? Il termine "programmazione" in questo contesto deriva dal significato originale della parola, che si riferisce alla **pianificazione** strategica piuttosto che alla scrittura di programmi informatici.

Negli anni '40, quando la programmazione lineare è stata sviluppata (soprattutto grazie a George Dantzig con il metodo del simplesso), il termine "programmare" significava pianificare in modo ottimale l'uso delle risorse disponibili per raggiungere un obiettivo. Questo era particolarmente utile in ambito militare ed economico, dove si cercava di ottimizzare la distribuzione delle risorse.

3) programmazione lineare intera:
    - tengo fermi i candidati, considero tutte le permutazioni, scelgo quella che minimizza il costo
        - costo computazionale spropositato -> permutazioni
    - problemi con una struttura combinatoria non si risolvono tramite enumerazione(detta anche brute-force)
    - ogni riga/colonna ha tutti zeri ed un uno (ogni compito può essere assegnato ad un solo impiegato e viceversa) 
    - di nuovo vincoli e funzione obiettivo sono lineari, però le variabili sono intere
    - non sembra una differenza drammatica rispetto alla programmazione lineare normale ma in realtà lo è -> **MOLTO PIù DIFFICILE**

4) problemi di scheduling 
    - ILP -> integer linear programming

5) problemi su grafi | circuito ottimo
    - vogliamo visitare tanti nodi col viaggio più breve possibile
    - migliaia di problemi di ottimizzazione possono essere modellati tramite grafi
        - grafi come strumento di modellazione