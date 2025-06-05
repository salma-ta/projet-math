#import os
#import sys
import random

# Ajoute le dossier dist (qui est à côté du dossier actuel) au chemin
#dist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dist'))
#sys.path.insert(0, dist_path)

from main_squelette import SimulateurTraitement

def strategie_uniforme(n_patients=1000):
    simulateur = SimulateurTraitement()
    total_succes = 0
    traitements = ['A', 'B', 'C', 'D', 'E']
    
    for patient in range(1, n_patients + 1):
        choix = random.choice(traitements)
        resultat = simulateur.administrer_traitement(choix)
        
        if resultat:
            total_succes += 1
        
        if patient % 100 == 0:
            print(f"Patient {patient}: {total_succes} succès cumulés")
    
    print(f"\nRésultat final - Stratégie uniforme:")
    print(f"{total_succes} succès sur {n_patients} patients")
    print(f"Taux de succès: {total_succes/n_patients*100:.2f}%")
    return total_succes

if __name__ == "__main__":
    strategie_uniforme()