import random

def calculer_score(main):
    score = 0
    as_comptes = 0

    for carte in main:
        if carte == 2:
            score += 2
        elif carte == 3:
            score += 3
        elif carte == 4:
            score += 4
        elif carte == 5:
            score += 5
        elif carte == 6:
            score += 6
        elif carte == 7:
            score += 7
        elif carte == 8:
            score += 8
        elif carte == 9:
            score += 9
        elif carte == 10:
            score += 10
        elif carte == 'J':
            score += 10
        elif carte == 'Q':  # Ou 'D' si tu préfères
            score += 10
        elif carte == 'K':  # Ou 'R' si tu préfères
            score += 10
        elif carte == 'A':
            score += 11
            as_comptes += 1  # Bien aligné ici !

    while score > 21 and as_comptes > 0:
        score -= 10
        as_comptes -= 1

    return score
def paquet():
    valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    paquet = valeurs*4
    random.shuffle(paquet)
    return paquet
def tirage_carte(paquet, main):
    carte = paquet.pop()
    main.append(carte)
    return carte
def tour_joueur(paquet, main_joueur):
    while True:
        score = calculer_score(main_joueur)
        print("\nVos cartes :", main_joueur, "| Score :", score)
        
        if score > 21:
            print("Vous avez depasse 21 ! Vous avez perdu.")
            break
            
        choix = input("(t)pout tirer (s)pour arreter")
        
        if choix == 't':
            tirage_carte(paquet, main_joueur)
        elif choix == 's':
            print("Vous vous arretez avec un score de :", score)
            break
        else:
            print("Choix invalide ! Tapez 't' ou 's'.")
def tour_banque(paquet, main_banque):
    print("tour banque")
    score = calculer_score(main_banque)
    print("Main de la banque :", main_banque, "| Score :", score)
    while score <= 16:
        print("La banque tire une carte...")
        tirage_carte(paquet, main_banque)
        score = calculer_score(main_banque)
        print("Main de la banque :", main_banque, "| Score :", score)

    if score > 21:
        print("La banque a depasse 21 !")
    else:
        print("La banque s'arrete.")

    return score
def gagnant(main_joueur, main_banque):
    score_j = calculer_score(main_joueur)
    score_b = calculer_score(main_banque)

    print("\nResutat")
    print("Joueur :", score_j, "| Banque :", score_b)

    if score_j > 21:
        print("Vous avez depasse 21. La banque gagne.")
    elif score_b > 21:
        print("La banque a depasse 21 ! Vous gagnez !")
    elif score_j > score_b:
        print("Vous gagnez !")
    elif score_b > score_j:
        print("La banque gagne.")
    else:
        print("nul")
if __name__ == "__main__":
    paquet = paquet()
    main_joueur = []
    main_banque = []
    tirage_carte(paquet, main_joueur)
    tirage_carte(paquet, main_joueur)
    tirage_carte(paquet, main_banque)
    tirage_carte(paquet, main_banque)
    print("Start")
    print("Carte visible de la banque :", main_banque[0])
    tour_joueur(paquet, main_joueur)
    if calculer_score(main_joueur) <= 21:
        tour_banque(paquet, main_banque)
    gagnant(main_joueur, main_banque)