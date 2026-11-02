# 1. Avoir une liste de persos et monstre enregistrer dans la db
# initier la db

# Afficher un menu
    # Afficher entête 
    # option 1 = jouer
    # option 2 = Voir les 3 meilleurs scores
    # option 3 = Quitter
    # recuperer choix valide 
    # Lancer l'option associer au choix 

# get_valid_choice(min, max) :

    # demander d'entrer un choix
    # Si l'entrer est un chiffre
        # Tant que le choix n'est pas dans l'intervalle min < choix <= max
            # demander d'entrer un choix
        # retourner le choix
    #sinon 
        # afficher "Vueillez entrer un chiffre"

# Jeu : 
    # team = []
    # team_alive = []
    # Créé une equipe de 3 persos
    # Lancer une vague

# créer_equipe :
    # definir la taille de l'equipe
    # Afficher la liste persos depuis la db
    # tant que l'equipe n'est pas complete
        # recuperer un choix valide dans la liste de persos
        # l'ajouter a l'equipe 
        # le supprimer de la liste persos
    # retourner l'equipe

# Vague :
    # Tant que l'equipe est en vie :
        # Choisir un monstre aléatoirement parmis la liste de monstres
        # Afficher le nom du monstre et ses infos
        # Tant que le monstre est en vie :
            # Les persos vivant attaquent le monstre
            # Vérifier que le monstre est encore en vie
            # Vérifier que le perso est encore en vie


    # Retourner le score


# Verifier_pv_monstre :
    # Si les pv du monstre sont positif
        # Le monstre attaque un perso vivant aléatoire
        # retourner pv du perso
    # Sinon 
        # Ajouter 1 au score 
        # retourner le score

# Verifier_pv_perso :
    # Si les pv du perso sont positif
        # Retourner True
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