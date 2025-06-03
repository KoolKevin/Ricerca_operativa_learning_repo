ricorda:
- variabile casuale: una variabile che può assumere valori reali associati agli esiti di un esperimento
    - è una funzione che associa ad un evento casuale un numero reale (valore casuale)
    - eg. 1 se testa, 0 se croce
- Un valore casuale è un numero reale specifico che ottieni quando la variabile casuale viene "realizzata" (cioè quando l’esperimento si verifica).
    - è il risultato osservato di una variabile casuale (output della funzione).



### Generating pseudo-random numbers from a probability distribution

**Metodo della trasformazione inversa**
Data: 
- Una funzione di densità di probabilità f(x)
- Un valore r casuale uniforme in [0, 1] 

Obiettivo: Generare un valore x con distribuzione f(x) qualunque

Come si fa:
- Si calcola la funzione di distribuzione cumulativa (CDF): 𝐹 (𝑥) = ∫[−∞, 𝑥] 𝑓(𝜉)𝑑𝜉
- Si prende l’inverso della CDF: 𝑥 = 𝐹^−1(𝑟)

Conclusione: Se prendi 𝑟∼𝑈(0, 1) e calcoli 𝑥 = 𝐹^−1(𝑟), allora 𝑥 ha densità di probabilità 𝑓(𝑥)


Il metodo della trasformazione inversa è estremamente utile perché permette di **generare numeri casuali secondo una qualsiasi distribuzione di probabilità, a partire da generatori di numeri casuali uniformi** (che sono standard nei computer).
 
1. I computer generano facilmente numeri pseudo-casuali uniformi in [0, 1] 
    - Tuttavia, nella pratica (simulazioni, modelli probabilistici, algoritmi stocastici), ci serve spesso generare numeri secondo distribuzioni diverse (esponenziale, normale, gamma, ecc.)
2. Permette di simulare qualsiasi distribuzione (**se la CDF è invertibile**)
    - Se conosci la funzione di distribuzione cumulativa 𝐹(𝑥), e puoi calcolare (se possibile) 𝐹^−1(𝑟), allora puoi simulare quella distribuzione facilmente.
3. Limiti del metodo: Devi conoscere l'inversa della funzione di distribuzione cumulativa F^−1
    - Per molte distribuzioni complesse, non esiste una formula chiusa per l'inversa (ad es. la distribuzione normale)



**Conclusione**: possiamo costruirci un generatore con una distribuzione che più ci piace con un generatore uniforme tra [0, 1]
- nel contesto della simulazione siamo particolarmente interessati alla distribuzione di una variabile casuale di Poisson

Una distribuzione di Poisson con parametro lambda ci dice la probabilità che ci siano k arrivals in un'unità di tempo
- il valore atteso è di lambda arrivals
    - in media abbiamo lambda arrivals per unità di tempo
- e quindi che il tempo tra arrival medio sia 1/lambda




## Simulazione numerica a eventi discreti
sono sistemi complessi in cui non è possibile
- scrivere un modello matematico in formula chiusa
- o utilizzare algoritmi come il simplesso e branch & bound

```perchè?```

la simulazione viene spesso accoppiata con l'ottimizzazione
- si simula una parte del sistema e si ottimizza un'altra

Perchè si utilizza la simulazione?
- per avere la possibilità di progettare/modificare un sistema in un ambiente controllato
- spese contenute
- eventi catastrofici nella simulaizione non hanno conseguenze reali
- per ottimizzare la configurazione del sistema tramite iterazione di esperimenti (molteplici simulazioni)

La simulazione a eventi discreti considera il sistema come una sequenza (discreta) di **eventi** casuale che **modifica lo stato del sistema**


come si fanno a conoscere i parametri probabilistici? (e.g. lambda)
- qualcuno ha fatto uno studio statistico sul sistema vero
- studi già noti



### tempo nelle simulazioni
nelle simulazioni abbiamo un solo **evento esterno** (avvio la simulazione) tutti gli altri sono **eventi interni**
- siccome gli eventi sono definiti da un PRNG la simulazione sa già quando il prossimo evento arriverà
- di conseguenza, dopo aver finito di gestire l'evento, può modificare direttamente le lancette dell'orologio senza aspettare 

La simulazione ha una **coda del tempo** in cui vengono inseriti gli eventi con il loro timestamp nel posto giusto. La simulazione si sposta nel tempo facendo dequeue di un evento alla volta



### diagramma degli inneschi
determina la sequenza di eventi che vanno ad innescarsi

ogni blocco è un evento
- con una sequenza di istruzioni di gestione dell'evento associata

**molto comune**
ogni arrivo, come prima cosa, innesca un'altro arrivo

**Nota**: eventi con ritardo zero possono spesso essere accorpati/eliminati in quanto il loro arrivo corrisponde all'inizio/fine di un'altro evento
- gli eventi modificano lo stato del sistema... questi spesso non lo fanno



... nel sistema possono essere state generate più auto rispetto a quelle specificate in NTOT. in generale la condizione di terminazione non determina il numero di entità ...



**Nota**: alcuni eventi vengono schedulati con riferimento a entità specifiche. Ad esempio l'evento di fine degenze normale/grave viene schedulato per uno specifico paziente


eventi endogeni sono quelli schedulati dalla simulazione, contrapposti agli eventi esogeni che sono aggiunti dall'utente (e.g. start della simulazione)

operazioni simultanee possono essere accorpate


tondino con S sta per start
- inizia la gestione dell'evento appena pescato dalla coda del tempo con la relativa subroutine
tondino con R sta per return
- ritorna al simulatore e pesca il prossimo evento dalla coda dei tempi



paradigma alternativo rispetto a quello della coda del tempo
- che è agnostica rispetto all'entità che genera l'evento

è il paradigma a interazione di processi in cui gli eventi sono associati ad un processo che ne definisce una sequenza propria










## scendiamo al secondo livello
Le variabili sono puntatori vengono riassegnati a diverse entità durante la simulazione in seguito al processamento di eventi
- **NB**: bisogna memorizzare gli indirizzi delle vecchie entità che subiscono un assegnamento distruttivo, altrimenti vengono perse
- questi indirizzi bisogna comunicarle al prossimo evento in quanto è l'unica entità che consente di accedere ad informazioni durante la simulazione (il sistema fa solo un ciclo: prelievo da coda del tempo - execute)




### Simulation statements | temporary entities
- **Creazione/distruzione di entità temporanee (dinamiche)**
    - temporary entities are **created** when they enter the system, **destroyed** when they leave it
    - *CREATE [A, AN, THE] entitiy [CALLED p]* 
        1. reserves a new block of memory for a new entity of class en;
        2. defines a **local variable** p containing the corresponding **pointer**;
            - if “CALLED p” is missing, the variable has name entity (preferred for single entities).
        - Example:
            - CREATE A CAR CALLED A1
            - CREATE A CAR (equivalent to CREATE A CAR CALLED CAR)
    - *DESTROY THE entity [CALLED p]* 
        - releases the reserved block of memory pointed by p (by entity, if “CALLED p” omitted)
- **lettura/scrittura di attributi**
    - attribute(p)
    - aggiunge/recupera l'attributo chiamato *attribute* dal puntatore p
    - Example: 
        - CREATE A CAR
        - TYPE(CAR) = X
            - CAR ha un attributo di tipo TYPE con valore X

### Simulation statements | permanent entities
- **System**
    - The System can have **permanent attributes**
    - permanent attributes are **global variables**.
        - Example: NMAX, NLG, NLN.
    - The System can **own sets with no index**
        - Example: QUEUE.
    - The system is automatically created, and is never destroyed.

- **Permanent entities**
    - Permanent entities can have **permanent attributes** (global variables)
        - Form like arrays (index = specific permanent entity).
        - Example: STATUS(J) = status (idle, busy) of **disc J**.
    - Permanent entities are created by a single statement:
        - *CREATE EVERY entity*;
    - must be preceded by the definition of **N.entity** (= **number of entities of class entity**).
        - Example: 
        - *READ N.DISC*
        - *CREATE EVERY DISC*


### Simulation statements | sets
- Sets have **members and owners**
    - members are usually temporary entities
    - owners are usually permanent entities
- sets with no index are owned by the system
    - hai già visto la QUEUE sopra
- sets with index are owned by permanent entities.
    - questi sono come degli attributi permanenti di entità permanenti
    - l'indice serve solo a distinguere a quale entità permanente appartiene il set a cui ci si vuole riferire
    - example: (code dei vari dischi DISC_QUEUE(i) = coda dell'i-esimo disco)
- Sorting policies:
    - FIFO;
    - LIFO;
    - Ranked
        - precedence given by the increasing or decreasing value of an **attribute of the member entities**.
- *FILE THE p IN THE s*
    - inserts the entity pointed by p in set s
- *REMOVE THE FIRST q FROM THE s*
    - removes the first entity from set s
    - stores its pointer in a local variable named q
- *REMOVE THE p FROM THE s*
    - removes the entity pointed by p from set s
- *IF THE s IS EMPTY I / IF THE s IS NOT EMPTY I*
    - executes I if s is/is not empty.




### Simulation statements | events and event notices
- Exogenous events are scheduled through input data (no need to reserve memory)
    - lasciamoli stare

- each scheduled Endogenous event needs a block of memory (time , entity pointer(s), ...);
- **Event Notice**: each event has an associated special **temporary entity having its name**;
    - gli eventi notice in pratica definiscono i dati variabili di una specifica istanza di un evento (car, tempo di schedulazione)
    - gli eventi vengono schedulati
    - un evento schedulato contiene un event-notice (con lo stesso nome) in cui salvo i dati che mi servono per gestire una specifica istanza di evento 
- event notices must be created before scheduling the event, and destroyed after the event is executed
    - when an event is executed, the system stores the pointer to the event notice in a local variable having the event name.
- **event notices can have attributes, typically used to store pointers to the entities that the event is interested in**
    - modificando gli attributi di un event notice si implementano, ad esempio, gli eventi di inizio servizio di macchine diverse (attributo car diverso dell'event notice)
    - devo creare l'event notice sia per aggiungerlo alla coda del tempo come evento da eseguire, sia per salvarci dentro le informazioni (sotto forma di attributi) su cui dovrà operare l'evento


CREATE AN ev [CALLED p] 
- reserves a new block of consecutive words for a **new event notice** of class ev;
    - uguale alla creazione di entità temporanee in quanto gli event notice sono una loro specializzazione
- defines a local variable p containing the corresponding pointer; 
    - if “CALLED p” is missing, the variable has name ev.
    
SCHEDULE THIS ev [CALLED p] AT t 
- schedules the event of pointer p (or ev) at t.
- Note: t = absolute time. Implemented as, e.g., SCHEDULE THIS E.SRV AT TIME.V + T
    - TIME.V = istante attuale

CANCEL THE ev [CALLED p]
- cancels the event of class ev having pointer p (or ev), **without** destroying the event notice.


### How do events exchange information?
There are only three possibilities:
1. Permanent attributes 
    - Example: TTC is reset to 0 in START, updated in E.SRV, and used in END;
2. Attributes of event notices
    - Example: CR(E.SRV) is defined in ARRIVAL and used in E.SRV;
 3. Attributes of temporary entities inserted and extracted from sets
    - Example: CAR is inserted in QUEUE in ARRIVAL, and removed from it in E.SRV, where TIC(CAR) is used"




**Grafica**
- esagono rappresenta il nome di una funzione
- il mezzo esagono rappresenta una chiamata di funzione
- parallelogramma per stampe




### Esempio finale ospedale
distruggo l'event notice direttamente quando non c'è una coda e quindi non c'è nessun altro che può riutilizzare l'event notice






### Esercizio esame
lunedì 9, facciamo solo esercitazione

- in una prima fase scriviamo:
    - dati
    - entità
    - insiemi 
        - code con la loro logica di ordinamento
    
- poi scriviamo un minimo di attributi

- e poi diagramma degli inneschi



quando ho un test, tutte le volte che modifico la variabile del test devo ricontrollare quest'ultimo
- vedi end nell'esempio della stazione di servizio