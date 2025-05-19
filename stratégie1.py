import random
from simulateur.dist import simulateur
from simulateur import SimulateurTraitement
traitements=['A','B','C','D','E']
patients=1000
comptes={t:0 for t in traitements}
succes={t:0 for t in traitements}
succes_total=0

for i in range(patients):
    t=random.choice(traitements)
    comptes[t]=comptes[t]+1
    if  simulateur.administrer_traitement(t)=='Succès' :
        succes[t]=succes[t]+1
        succes_total+=1
print(f"nombre total de succés:{succes_total}")

