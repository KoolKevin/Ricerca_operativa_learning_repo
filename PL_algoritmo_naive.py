from itertools import combinations

# S = {1, 2, 3}
# Combinazioni di due elementi su un insieme S di tre elementi = [{1, 2}, {1, 3}, {2, 3}]

def trova_combinazioni_colonne(matrice):
    n_righe   = len(matrice)  
    n_colonne = len(matrice[0])

    for i in range(n_righe):
        for j in range(i+1, n_colonne):
            print(i, j)


matrice = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]



# Trova e stampa tutte le combinazioni di colonne
trova_combinazioni_colonne(matrice)