import random
import sys
import os

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu"]

def import_heros() :
    heros = db["persos"]
    return heros

def import_monsters():
    monsters = db["monstres"]
    return monsters

def main():
    display_menu()
    choice = get_choice(1,3)
    run_option(choice)

def clear_console() :
     os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_console()
    display_header()
    display_option()

def display_header():
    game_name = ""
    print(f"Bienvenue sur {game_name}")

def display_option():
    print("Option 1 : Jouer/nOption 2 : Classement des 3 meilleurs joueurs/nOption 3 : Quitter/n")

def get_choice(min, max):
    choix = False
    while choix == False :
        choice = input("Que voulez vous faire ?")
        choix = is_valid_choice(choice, min, max)
    return choice

def is_valid_choice(choice, min, max):
    if choice.isdigit():
        if choice < min or choice > max:
            return False
        return True
    else:
        print("Vueillez entrer un chiffre")
        return False

def run_option(choice):
    if choice == 1:
        play()
    if choice == 2:
        display_top_three()
    if choice == 3:
        close_game()

def play():
    username = get_user_name()
    create_team()
    wave = start_battle()
    save_data(wave, username)

def get_user_name():
    input_username = False
    while input_username == False:
        username = input("Vueillez entrer un pseudo")
        input_username = is_valide_input(username)
    return username

def is_valid_input(username):
    if username.isdigit():
        print("Vueillez entrer des lettres")
        return False
    if len(username) < 3 or len(username) > 10:
        print("Votre nom doit comporter au minimum 3 lettres et au maximum 10")
        return False
    else:
        return True

def create_team():
    team = []
    team_size = 3
    available_heroes = display_list_heros()
    while len(team) < team_size:
        print(available_heroes)
        print(f"Votre team est {team}")
        choice = get_choice(1, len(available_heroes)) 
        character = available_heroes[choice - 1]
        team.append(character)
        available_heroes.pop(choice-1)  
    return team

def display_list_heros():
    available_heroes = import_heros()
    i = 1
    for hero in available_heroes:
        print(f"{i} : ")
        print(f"{hero['name']}, ATK: {hero['ATK']}, DEF: {hero['DEF']}, PV: ")
    return available_heroes

# Afficher liste persos :
    # persos_dispos = heros
    # i = 1
    # Pour chaque perso dans persos
        # afficher i
        # afficher nom, atk, def, pv du perso
        # i+= 1
    # retourner persos_dispos

# combat(team) :
    # vague = 0
    # Tant que team_alive est vraie :
        # lancer round()
        # si equipe en vie
            # ajouter 1 a vague
    # retourner vague


# round :
    # Choisir un monstre aléatoirement parmis la liste de monstres 
    # Afficher le nom du monstre et ses infos 
    # Tant que le monstre est en vie et equipe en vie  :
        # tour de combat
    
    # si equipe est en vie
    # return true

# get_random_monster
    # monster = choisir aleatoirement un monstre dans monstres
    # retourner monster

# display_info_monster:
    # Afficher nom, atk, def, pv du monstre

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
        # attaque(hero, monstre)

# monstre_attaque :
    # choisir aléatoirement le perso a attaquer
    # attaque(monstre, perso_aleatoire)

# attaque(attaquant, opposant) :
    # degat = atk attaquant - def opposant 
    # pv opposant -= degat

# team_alive() :
    # team_alive = []
    # Pour chaque perso dans team
    # Si pv perso <= 0
        # continuer
    # Sinon :
        # ajouter a team_alive

# Display_top_three
    # recuperer le classement trier par score 
    # afficher les trois premiers de la liste

# get_leaderboard
    # recuperer le classement dans la db
    # trier le classement par score 

# sort_leaderboard(leaderboard)
    # leaderboard = leaderboard.sort()
    # return leaderboar 

# close_game
    # sys.exit()

# Enregistrer les données
    # Enregistrer player
    # inserer dans la db

# New_player(pseudo, vague)
    # player = {"name" = pseudo, "score" = vague}