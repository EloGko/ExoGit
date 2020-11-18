def initialiseGrille(grille):
    for i in range(0,9):
        grille[i] = " "
    return

def afficheGrille(grille):
    for i in range(0,3):
        print(grille[3*i],grille[3*i+1],grille[3*i+2],"\n")
    return
