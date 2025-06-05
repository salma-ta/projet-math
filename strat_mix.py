#import os
#import sys
import random

# Ajoute le dossier dist au chemin
#dist_dir = os.path.join(os.path.dirname(__file__), "dist")
#sys.path.insert(0, dist_dir)

from main_squelette import SimulateurTraitement

def strategie_mixte(n_patients=1000, n_exploration=10, alpha=0.8):
    traitements = ['A', 'B', 'C', 'D', 'E']
    simulateur = SimulateurTraitement()

    N = {t: 0 for t in traitements}
    S = {t: 0 for t in traitements}
    total_succes = 0

    # Exploration initiale
    for t in traitements:
        for _ in range(n_exploration):
            resultat = simulateur.administrer_traitement(t)
            N[t] += 1
            if resultat:
                S[t] += 1
                total_succes += 1

    # Phase stratégie mixte
    for patient in range(len(traitements)*n_exploration + 1, n_patients + 1):
        estimations = {t: S[t] / N[t] for t in traitements if N[t] > 0}

        if random.random() < alpha:
            # Choix du meilleur traitement
            meilleur = max(estimations, key=estimations.get)
        else:
            # Choix aléatoire
            meilleur = random.choice(traitements)

        resultat = simulateur.administrer_traitement(meilleur)
        N[meilleur] += 1
        if resultat:
            S[meilleur] += 1
            total_succes += 1

        if patient % 100 == 0:
            print(f"Patient {patient}: {total_succes} succès cumulés")

    print(f"\nRésultat final - Stratégie mixte (alpha={alpha}):")
    print(f"{total_succes} succès sur {n_patients} patients")
    print(f"Taux de succès: {total_succes/n_patients*100:.2f}%")

    return total_succes

# Exécution
if __name__ == "__main__":
    strategie_mixte()
