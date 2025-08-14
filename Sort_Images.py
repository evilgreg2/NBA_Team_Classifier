import os
import pandas as pd
import json
from anyascii import anyascii



input_directory = "Unsorted_Data/NBA Players"
players_csv_name = "nba_2020_per_game.csv"
players_csv = pd.read_csv(players_csv_name)
def get_all_team_names():

    teams = list(sorted(set(players_csv['Tm'])))
    return teams

def get_players_for_team(team):
    team_players = players_csv.loc [players_csv['Tm'] == team]
    team_player_names = list(sorted(set(team_players['Player'])))
    team_player_names = list(map(anyascii, team_player_names))
    player_names_lowercase = []
    for name in team_player_names:
        player_names_lowercase.append(name.lower())
    return player_names_lowercase

def get_all_team_rosters():
    roster = {}
    for team in get_all_team_names():
        roster[team] = get_players_for_team(team)
    return roster
def save_roster_to_file(file_name = "roster.json"):
    roster = get_all_team_rosters()
    with open(file_name, 'w') as outfile:
        json.dump(roster, outfile, indent=4)

def create_team_folders(output_directory):
    team_folders = {}
    for team in get_all_team_names():
        team_folder = os.path.join(output_directory, team)
        os.makedirs(team_folder, exist_ok=True)
        team_folders[team] = team_folder
    return team_folders

def sort_player_images(input_directory, team_folders, roster):
    folder_name = os.path.split(input_directory)[1]
    names = folder_name.split(", ")
    player_name = names[1] + " " + names[0]
    player_name = player_name.lower()
    teams = []
    for team_name, team_players in roster.items():
        if player_name in team_players:
            teams.append(team_name)
    print(player_name, teams)


def sort_all_player_images(input_directory = "Unsorted_Data/NBA Players"):
    team_folders = create_team_folders("NBA_Teams")
    rosters = get_all_team_rosters()
    player_directory_names = os.listdir(input_directory)
    for player_directory in player_directory_names:
        player_directory = os.path.join(input_directory, player_directory)
        if os.path.isdir(player_directory):
            sort_player_images(player_directory, team_folders, rosters)

if __name__ == "__main__":
    save_roster_to_file()
    sort_all_player_images()
