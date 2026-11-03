# importer random
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
    # afficher option

# Afficcher option
    # option 1 = jouer
    # option 2 = classement
    # option 3 = Quitter

# get_choice(min, max):
    # choix = false
    # Tant que choix est faux
        # demander choice
        # choix = is_valid_choice(choice)
    # return choix

# is_valid_choice(choice, min, max) :
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
    # get_user_name() TODO
    # Créé une equipe de 3 heros
    # Lancer un combat

# créer_equipe :
    # team = []
    # definir la taille de l'equipe
    # tant que l'equipe n'est pas complete
        # Afficher liste persos_actuels
        # recuperer un choix valide
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

# combat(team) :
    # team = team_alive
    # vague = 0
    # Tant que l'equipe est en vie :
        # lancer round()
        # si equipe en vie
            # ajouter 1 a vague


# round :
    # Choisir un monstre aléatoirement parmis la liste de monstres 
    # Afficher le nom du monstre et ses infos TODO
    # Tant que le monstre est en vie et equipe en vie  :
        # tour de combat
    
    # si equipe est en vie
    # return true

# get_random_monster
    # monster = choisir aleatoirement un monstre dans monstres
    # retourner monster

# print_monster_name(monster) :
    # 


# tour de combat :
    # recuperer les persos vivant
    # Les persos vivant attaquent le monstre 
    # Vérifier que le monstre est encore en vie
    # Si monstre en vie
        # Monstre attaque 

# Verifier_pv_monstre :
    # Si les pv du monstre sont positif
        # Retourner pv du monstre
    # Sinon 
        # retourner que le monstre est mort


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