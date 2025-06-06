import os
import random
import matplotlib.pyplot as plt
from collections import defaultdict
from main_squelette import SimulateurTraitement

def strategie_uniforme(n_patients=1000):
    simulateur = SimulateurTraitement()
    total_succes = 0
    traitements = ['A', 'B', 'C', 'D', 'E']
    succes_par_traitement = defaultdict(int)

    print("\n--- STRATÉGIE UNIFORME - DÉTAIL PAR PATIENT ---")
    
    for patient in range(1, n_patients + 1):
        traitement = random.choice(traitements)
        resultat = simulateur.administrer_traitement(traitement)
        etat = "succès" if resultat else "échec"
        print(f"Patient {patient}: traitement {traitement} → {etat}")
        
        if resultat:
            total_succes += 1
            succes_par_traitement[traitement] += 1

    print(f"\nRésultat final - Stratégie uniforme :")
    print(f"{total_succes} succès sur {n_patients} patients")
    print(f"Taux de succès : {total_succes / n_patients * 100:.2f} %")

    # Affichage du graphique
    traitements_tries = sorted(succes_par_traitement.keys())
    valeurs = [succes_par_traitement[t] for t in traitements_tries]

    plt.bar(traitements_tries, valeurs, color='skyblue')
    plt.title("Nombre de succès par traitement (stratégie uniforme)")
    plt.xlabel("Traitement")
    plt.ylabel("Nombre de succès")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    return total_succes

# Exécution
if __name__ == "__main__":
    strategie_uniforme()
