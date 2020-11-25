#FONCTIONS :
def initialiseGrille(grille):
    for i in range(0,9):
        grille[i] = " "
    return

def afficheGrille(grille):
    for i in range(0,3):
        print(grille[3*i],grille[3*i+1],grille[3*i+2],"\n")
    return

def ajouteSymbole(grille, joueur):
    choixIncorrect = "vrai"
    while choixIncorrect = "vrai" :
        i = input("Sur quelle ligne voulez-vous jouez ?")
        j = input("Sur quelle colonne voulez-vous jouez ?")
        if grille[3*i+j] != " ":
            grille[3*i+j] = joueur
            choixIncorrect = "faux"
    return

def testeVictoireVerticale(grille):
    compteur = 0
    while compteur < 3:
        if grille[compteur] != " " and grille[compteur] == grille[compteur+3] and grille[compteur] == grille[compteur+6]:
            return "vrai"
    return "faux"

def testeVictoireHorizontale(grille):
    compteur = 0
    while compteur < 3:
        if grille[compteur] != " " and grille[compteur*3] == grille[compteur*3+1] and grille[compteur*3] == grille[compteur*3+2]:
            return "vrai"
    return "faux"
    
def testeVictoireDiagonale(grille):
    if grille[compteur] != " " and grille[4] == grille[0] and grille[4] == grille [8]:
        return "vrai"
    if grille[compteur] != " " and grille[4] == grille[2] and grille[4] == grille [6]:
        return "vrai"
    return "faux"

def testeJeuNul(gagnantTrouvé, tour):
    if tour == 9 and gagnantTrouvé = "faux":
        return "vrai"
    return "faux"

#CODE PRINCIPAL :
initialiseGrille(grille)
afficheGrille(grille)
ajouteSymbole(grille, joueur)
