
# initier la db
# heros = liste persos dans la db
# monstres = liste monstres dans la db


# main :
    # afficher le menu
    # recuperer choix 
    # Lancer l'option associer au choix  


# Afficher un menu
    # clear
    # Afficher entête 
    # option 1 = jouer
    # option 2 = Voir les 3 meilleurs scores
    # option 3 = Quitter

# get_choice(min, max):
    # choix = false
    # Tant que choix est faux
        # demander choix
        # verifier le choix
    # return choice

# get_valid_choice(choice, min, max) :
    # Si le choix est un chiffre
        # si le choix n'est pas dans l'intervalle min < choix <= max :
            # retourner false
        # retourner True
    #sinon 
        # afficher "Vueillez entrer un chiffre"
        # return false

# Lancer otpion :
    # si option 1 
        # lancer jeu
    # si option 2
        # Montrer score TODO:
    # si option 3 
        # fermer jeu TODO:

# Jeu : 
    # Créé une equipe de 3 heros
    # Lancer une vague

# créer_equipe :
    # team = []
    # definir la taille de l'equipe
    # tant que l'equipe n'est pas complete
        # Afficher liste persos
        # recuperer un choix dans la liste de persos
        # caractère = perso de l'index choix-1
        # ajouter le caractère à la team
        # le supprimer le caractère de la liste persos_actuels
    # retourner team

# Afficher liste persos :
    # persos_actuels = heros
    # i = 1
    # Pour chaque perso dans persos
        # afficher i
        # afficher nom, atk, def, pv du perso
        # i+= 1
    # retourner persos_actuels

# Vague(team) :
    # team = team_alive
    # Tant que l'equipe est en vie :
        # Choisir un monstre aléatoirement parmis la liste de monstres TODO
        # Afficher le nom du monstre et ses infos TODO
        # Tant que le monstre est en vie :
            # Les persos vivant attaquent le monstre
            # Vérifier que le monstre est encore en vie
            # Monstre attaque (seulement si il est mort !)
            # Vérifier que le perso est encore en vie
    # Retourner le score


# Verifier_pv_monstre :
    # Si les pv du monstre sont positif
        # Retourner pv du monstre
    # Sinon 
        # Ajouter 1 au score 
        # retourner le score
        # break ?

# Verifier_pv_perso :
    # Si les pv du perso sont positif
        # Retourner pv perso
    # Sinon 
        # Afficher "le perso est mort"
        # Supprimer le perso de team_alive

# Persos_attaque :
    # Pour tous les persos parmis team_alive
        # degat = atk du perso - defense du monstre
        # Pv du monstre -= degat

# monstre_attaque :
    # choisir aléatoirement le perso a attaquer
    # degat = atk du monstre - defense du perso
    # pv du perso -= degat