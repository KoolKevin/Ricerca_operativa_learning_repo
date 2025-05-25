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
- Un valore r casuale uniforme in [0 , 1] 

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