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
        if grille[compteur] != " " and grille[compteur] == grille[compteur+3] and grille[compteur+6]:
            return "vrai"
    return "faux"