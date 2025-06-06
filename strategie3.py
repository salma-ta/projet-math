import numpy as np
import sys
import os


# Chargement du simulateur depuis le dossier dist/
from main_squelette import SimulateurTraitement

# Paramètres
N = 1000
K = 5
delta = 0.05

# Conversion indice -> lettre
traitements = ['A', 'B', 'C', 'D', 'E']

# Initialisation du simulateur
simulateur = SimulateurTraitement()

successes = np.zeros(K)
counts = np.zeros(K)

# Premier tour : un traitement chacun
for k in range(K):
    label = traitements[k]
    result = simulateur.administrer_traitement(label)
    successes[k] += result
    counts[k] += 1

results = []
selected_treatments = [] 

# Boucle principale
for n in range(K, N):
    p_hat = successes / counts
    epsilons = np.sqrt(np.log(2 * n**2 / delta) / (2 * counts))
    S = p_hat + epsilons
    k = np.argmax(S)
    selected_treatments.append(k) 
    

    result = simulateur.administrer_traitement(traitements[k])
    successes[k] += result
    counts[k] += 1
    results.append(result)

# Affichage des résultats
total_successes = int(sum(successes))
print("Succès totaux :", total_successes)


# Affichage formaté du tableau final
print("\nTraitement | Estimation p̂ |  Marge ε  | p̂ + ε (borne sup)")
print("--------------------------------------------------------------")
for k in range(K):
    print(f"    {traitements[k]}      |   {p_hat[k]:.3f}      |  {epsilons[k]:.3f}   |     {S[k]:.3f}")

meilleur_k = np.argmax(S)
print(f"\n Meilleur traitement choisi selon la stratégie : {traitements[meilleur_k]}")

