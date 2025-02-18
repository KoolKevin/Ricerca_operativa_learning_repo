notazione:
- guardala ...
- matrici per rappresentare sistemi di equazioni lineari
- **interpretazione rossa del prodotto matriciale**

### Come si descrive un generale problema di ottimizzazione?
- vettore di variabili decisionali da ottimizzare
    - punto in R_n, appartenente al insieme delle soluzioni possibili
- funzione obiettivo: f: F -> R
- massimi e minimi non creano problemi

**classificazione**:
- (non lineare)
- convessa
- lineare


...


regione ammissibile anche non continua/ vuota

numero di righe uguale anche a  numero di vincoli 


definizione di intorno (versione generale crazy):
- noi utilizzeremo intorni euclidei (quelli che ti aspetti) e quindi la definizione generale la puoi ignorare

intorni esatti


## Programmazione convessa
**insiemi convessi**

- combinazione convessa un terzo punto ottenuto come una somma particolare di x e y
    - con lambda = 1/2 -> punto di mezzo tra x e y
    - più è grande/piccolo lambda -> più tendo verso x/y
    - combinazione convessa descrive tutti i punti del segmento che unisce x e y

- insiemi convessi
    - in qualunque modo scelga i due punti, l'intero segmento appartiene all'insieme

- proprietà insiemi convessi

- funzioni convesse su un insieme convesso
    - costo della combinazione convessa è <= della combinazione convessa dei costi

- funzione concava -> -c convessa

- notare il <= 
    - funzioni lineari sono sia concave che convesse

definizione di programmazione convessa: