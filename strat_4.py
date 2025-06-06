import random
import matplotlib.pyplot as plt
from main_squelette import SimulateurTraitement

def strategie_bayesienne(n_patients=1000, n_exploration=10):
    traitements = ['A', 'B', 'C', 'D', 'E']
    simulateur = SimulateurTraitement()

    # Paramètres Beta pour chaque traitement (a=alpha, b=beta)
    alpha_params = {t: 1 for t in traitements}  # succès + 1
    beta_params = {t: 1 for t in traitements}   # échecs + 1

    total_succes = 0

    # Phase d'exploration initiale : tester chaque traitement n_exploration fois
    for t in traitements:
        for _ in range(n_exploration):
            resultat = simulateur.administrer_traitement(t)
            if resultat:
                alpha_params[t] += 1
                total_succes += 1
            else:
                beta_params[t] += 1

    # Phase Thompson Sampling
    for patient in range(len(traitements)*n_exploration + 1, n_patients + 1):
        # Tirage aléatoire depuis Beta(alpha, beta) pour chaque traitement
        echantillons = {t: random.betavariate(alpha_params[t], beta_params[t]) for t in traitements}
        # Choix du traitement avec la meilleure estimation
        meilleur = max(echantillons, key=echantillons.get)

        resultat = simulateur.administrer_traitement(meilleur)
        if resultat:
            alpha_params[meilleur] += 1
            total_succes += 1
        else:
            beta_params[meilleur] += 1

        if patient % 100 == 0:
            print(f"Patient {patient}: {total_succes} succès cumulés")

    # Nombre de succès par traitement = alpha_params - 1 (car a init = 1)
    succes_par_traitement = {t: alpha_params[t] - 1 for t in traitements}

    print(f"\nRésultat final - Stratégie bayésienne (Thompson Sampling):")
    print(f"{total_succes} succès sur {n_patients} patients")
    print(f"Taux de succès: {total_succes/n_patients*100:.2f}%")
    print("Succès par traitement :", succes_par_traitement)
    print("Nombre de tests par traitement :", {t: alpha_params[t] + beta_params[t] - 2 for t in traitements})

    # Affichage du graphique
    traitements_tries = sorted(succes_par_traitement.keys())
    valeurs = [succes_par_traitement[t] for t in traitements_tries]

    plt.bar(traitements_tries, valeurs, color='skyblue')
    plt.title("Nombre de succès par traitement (Stratégie bayésienne)")
    plt.xlabel("Traitement")
    plt.ylabel("Nombre de succès")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    return total_succes

if __name__ == "__main__":
    strategie_bayesienne()
