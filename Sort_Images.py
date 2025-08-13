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
    return team_player_names

def get_all_team_rosters():
    roster = {}
    for team in get_all_team_names():
        roster[team] = get_players_for_team(team)
    return roster
def save_roster_to_file(file_name = "roster.json"):
    roster = get_all_team_rosters()
    with open(file_name, 'w') as outfile:
        json.dump(roster, outfile, indent=4)
if __name__ == "__main__":
    save_roster_to_file()

