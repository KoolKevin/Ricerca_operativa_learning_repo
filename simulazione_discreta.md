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
- e quindi che il tempo tra arrival medio sia 1/lambda




## Simulazione numerica a eventi discreti
sono sistemi complessim in cui non è possibile
- scrivere un modello matematico in formula chiusa
- utilizzare algoritmi come il simplesso e branch & bound

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

La simulazione ha una coda del tempo in cui vengono inseriti gli eventi con il loro timestamp nel posto giusto. La simulazione si sposta nel tempo facendo dequeue di un evento alla volta



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