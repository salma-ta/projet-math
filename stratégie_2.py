
import random
import matplotlib.pyplot as plt
from main_squelette import SimulateurTraitement

def strategie_2(n_patients=1000, n_exploration=10, alpha=0.8):
    traitements = ['A', 'B', 'C', 'D', 'E']
    simulateur = SimulateurTraitement()

    N = {t: 0 for t in traitements}
    S = {t: 0 for t in traitements}
    total_succes = 0

    # --- Phase d'exploration initiale ---
    for t in traitements:
        for _ in range(n_exploration):
            resultat = simulateur.administrer_traitement(t)
            N[t] += 1
            if resultat:
                S[t] += 1
                total_succes += 1

    # --- Phase stratégie 2 ---
    for patient in range(len(traitements) * n_exploration + 1, n_patients + 1):
        estimations = {t: S[t] / N[t] for t in traitements if N[t] > 0}

        if random.random() < alpha:
            meilleur = max(estimations, key=estimations.get)
        else:
            meilleur = random.choice(traitements)

        resultat = simulateur.administrer_traitement(meilleur)
        N[meilleur] += 1
        if resultat:
            S[meilleur] += 1
            total_succes += 1

        if patient % 100 == 0:
            print(f"Patient {patient}: {total_succes} succès cumulés")

    # --- Résultat final ---
    print(f"\nRésultat final - Stratégie 2(alpha={alpha}):")
    print(f"{total_succes} succès sur {n_patients} patients")
    print(f"Taux de succès: {total_succes/n_patients*100:.2f}%")

    # --- Affichage du graphique (comme avant) ---
    traitements_tries = sorted(S.keys())
    valeurs = [S[t] for t in traitements_tries]

    plt.bar(traitements_tries, valeurs, color='lightgreen')
    plt.title(f"Nombre de succès par traitement\n(Stratégie 2, alpha={alpha})")
    plt.xlabel("Traitement")
    plt.ylabel("Nombre de succès")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    return total_succes

# Exécution
if __name__ == "__main__":
    strategie_2()
