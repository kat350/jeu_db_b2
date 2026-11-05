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
    team = create_team()
    wave = start_battle(team)
    save_data(wave, username)

def get_user_name():
    input_username = False
    while input_username == False:
        username = input("Vueillez entrer un pseudo")
        input_username = is_valid_input(username)
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
        print(f"{hero['name']}, ATK: {hero['ATK']}, DEF: {hero['DEF']}, PV: {hero['PV']}")
        i += 1
    return available_heroes

def start_battle(team):
    wave = 0
    while team is True:
        win = start_round(team)
        if win:
            wave += 1
    return wave

def start_round(team):
    team_alive = team_alive(team)
    monster = get_random_monster()
    display_info_monster(monster)
    while monster['PV'] > 0 and len(team_alive()) > 0 :
        combat_turn(monster)
    if len(team_alive()) >  0 :
        return True

def get_random_monster() :
    monsters = import_monsters()
    monster = random.choice(list(monsters.items()))
    return monster

def display_info_monster(monster) :
    print(f"{monster['name']} apparait ! ATK: {monster['ATK']}, DEF: {monster['DEF']}, PV: {monster['PV']}")



# print_monster_name(monster) :
    # 

def combat_turn(monster) :
    heros_alive = team_alive()
    team_attack(heros_alive, monster)
    monster_alive = monster_is_alive(monster)
    if monster_alive is True :
        monster_attack(heros_alive)


def monster_is_alive(monster) :  
    if monster['PV']  > 0 :
        return True
    else :
        return False

def hero_is_alive(team) :
    for hero in team :
        if hero['PV'] > 0 :
            return True
        else:
            print(f"{hero['name']} est mort")
            return False

def team_attack(team_alive, monster) : 
    for hero in team_alive:
        attack(hero, monster)

def monster_attack(monster, team) :
    random_hero = get_random_hero(team)
    attack(monster, random_hero)

def attack(attacker, opponent) :
    degat = attacker['ATK'] - opponent['DEF']
    opponent['PV'] -= degat

def team_alive(team) :
    team_alive = []
    for hero in team :
        if hero['PV'] <= 0 :
            continue
        else :
            team_alive.append(hero)
        return team_alive
    
def get_random_hero(team) :
    random_hero = random.choice(list(team.items()))
    return random_hero

def display_top_three() : 
    learderboard = get_leaderboard()
    top_three =  [learderboard[0], learderboard[1], learderboard[2]]
    print(top_three)

def get_leaderboard():
    leaderboard = db['leaderboard']
    leaderboard = sort_leaderboard(leaderboard)
    return leaderboard

def sort_leaderboard(leaderboard) :
    sorted_leaderboard = leaderboard.sort(reverse=True)
    return sorted_leaderboard

# close_game
    # sys.exit()

# Enregistrer les données
    # Enregistrer player
    # inserer dans la db

# New_player(pseudo, vague)
    # player = {"name" = pseudo, "score" = vague}

