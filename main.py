
"""
On recherche parmi les mots du nombre de caractère indiqué.

Les mots qui ont le plus de chance de nous apporter des informations sont ceux 
dont les lettres apparaissent le plus fréquement.

Dans le round n = 1, on cherche les mots dont les lettres maximisent la somme
des fréquences d'apparitions.

Dans les rounds n > 1, on cherche les mots dont les lettres maximisent la somme
des fréquences d'apparition, excluant celles qui ont déjà été testées

On peut utiliser la fonction mots_valides(indications) pour récupérer la liste
des mots vérifiant nos contraintes. S'il y en a trop, on peut relancer une 
rechercher "round n > 1".
"""

from copy import deepcopy

#longueur du mot
n = 7

#Je prépare une fonction qui refais np.unique
def single_one(liste):
    s = []
    for i in liste:
        if i not in s:
            s += [i]
    return s

#Je récupère la liste des mots de longneur n
fichier = open("liste.de.mots.francais.frgut.txt",'rb')
data = [i.rstrip("\r") for i in fichier.read().decode("utf-8").split("\n")]
fichier.close()
s = [i for i in data if len(i) == n]

#J'évalue la valeur des mots (ceux qui ont le plus de chances de m'apporter des lettres présentes)
frequence_app_lettres_frc = {"e":115024205,"a":67563628,"i":62672992,"s":61882785,"n":60728196,"r":57656209,"t":56267109,"o":47724400,"l":47171247,"u":42698875,"d":34914685,"c":30219574,"m":24894034,"p":23647179,"é":18451937,"g":11684140,"b":10817171,"v":10590858,"h":10583562,"f":10579192,"q":6140307,"y":4351953,"x":3588990,"j":3276064,"è":2969466,"à":2966029,"k":2747547,"w":1653435,"z":1433913,"ê":802211,"ç":544509,"ô":357197,"â":320837,"î":280201}
def evaluer_mot(mot,lettres_exclues): 
    return sum([frequence_app_lettres_frc[i] for i in single_one(list(mot)) if i in frequence_app_lettres_frc and i not in lettres_exclues])


### Round n = 1
scores_mots = [[evaluer_mot(i,[]),i] for i in s]
scores_mots.sort()
print("On a trouvé : "+str(len(scores_mots))+" mots")
print("Celui qui nous aidera le plus, c'est : "+str(scores_mots[-1]))

#### Round n > 1
lettres_deja_utilisees = list("tsarine")
scores_mots = [[evaluer_mot(i,lettres_deja_utilisees),i] for i in s]
scores_mots.sort()
print("On a trouvé : "+str(len(scores_mots))+" mots")
print("Celui qui nous aidera le plus, c'est : "+str(scores_mots[-1]))

### Fonction mots_valides(indications)
def mots_valides(indications):
    global s
    s2 = deepcopy(s)
    for j in indications["emplacements_connus"]:
        s2 = [i for i in s2 if i[indications["emplacements_connus"][j]] == j]
    for j in indications["emplacements_non_connus"]:
        s3 = []
        for i in s2:
            y_est = False
            for k in indications["emplacements_non_connus"][j]:
                if i[k] == j:
                    y_est = True
            if not y_est and j in i:
                s3 += [i]
        s2 = s3
    return s2

"""
Exemple : on sait que "a" est situé au rang 0 et on sait que "b" est mal placé au rang 1.

indications = {}
indications["emplacements_connus"] = {"a":0}
indications["emplacements_non_connus"] = {"b":[1]}
"""

indications = {}
indications["emplacements_connus"] = {"a":0}
indications["emplacements_non_connus"] = {"b":[1,2,3]}

stock = mots_valides(indications)

