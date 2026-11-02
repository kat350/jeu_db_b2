# 1. Avoir une liste de persos et monstre enregistrer dans la db
# Importer la db

# Afficher un menu
    # Afficher entête 
    # option 1 = jouer
    # option 2 = Voir les 3 meilleurs scores
    # option 3 = Quitter
    # demander un choix
    # Vérifier que le choix est valide 
    # Lancer l'option associer au choix 

# Jeu : 
    # Afficher la liste persos depuis la db
    # Créé une equipe de 3 persos
    # Lancer une vague

# Vague :
    # Tant que l'equipe est en vie :
        # Choisir un monstre aléatoirement parmis la liste de monstres
        # Afficher le nom du monstre et ses infos
        # Tant que le monstre est en vie :
            # Les 3 persos attaques le monstre
            # Vérifier que le monstre est encore en vie
            # Vérifier que le perso est encore en vie


    # Retourner le score


# Verifier_pv_monstre :
    # Si les pv du monstre sont positif
        # Le monstre attaque un perso aléatoire de l'equipe
        # retourner pv du perso
    # Sinon 
        # Ajouter 1 au score 
        # retourner le score

# Verifier_pv_perso :
    # Si les pv du perso sont positif
        # Retourner True
    # Sinon 
        # Afficher "le perso est mort"
        # Supprimer le perso de l'equipe 

# Persos_attaque :
    # Pour tous les persos parmis l'equipe
        # degat = atk du perso - defense du monstre
        # Pv du monstre -= degat
# monstre_attaque :
    # choisir aléatoirement le perso a attaquer
    # degat = atk du monstre - defense du perso
    # pv du perso -= degat