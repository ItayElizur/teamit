import os
import pandas as pd
import matplotlib.pyplot as plt
import math

CSV_FOLDERPATH = r'C:\Users\garre\Desktop\datathon\data'

n_matches_to_analyze = 2_000
matches = pd.read_csv(CSV_FOLDERPATH + os.sep + "match_clean.csv", nrows=n_matches_to_analyze)
matches = matches.iloc[:n_matches_to_analyze, 1:]

# add symmetry of matches.
# matches_mirror = matches.rename(columns={player_column: player_column.replace("away", "home") if "away" in player_column
#     else player_column.replace("home", "away") for player_column in matches.columns if "_player_" in player_column})
# matches = pd.concat(matches, matches_mirror)

matches = matches[sorted(matches.columns)]
matches["homeaway_goal_delta"] = matches.apply(lambda row: row["home_team_goal"] - row["away_team_goal"], axis=1)
matches["winning_team"] = matches.apply(lambda row: "home" if row["homeaway_goal_delta"] >= 1 else "tie" if row["homeaway_goal_delta"] == 0 else "away", axis=1)

HOME_PLAYERS_COLUMNS = ["{}_player_{}".format("home", player_role) for player_role in range(1, 12)]
AWAY_PLAYERS_COLUMNS = ["{}_player_{}".format("away", player_role) for player_role in range(1, 12)]
def columns_of_players_from_team(team):
    return HOME_PLAYERS_COLUMNS if team == "home" else AWAY_PLAYERS_COLUMNS if team == "away" else RuntimeError

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.rating = 50
        self.number_of_games_played = 0

    def update_rating(self, match):
        # log2(1 + delta goals)
        winning_team = match["winning_team"]
        if winning_team == "tie":
            pass
        else:
            homeaway_goal_delta = match["homeaway_goal_delta"]
            winning_players_ids = set(match[columns_of_players_from_team(winning_team)])
            player_was_in_winning_team = self.player_id in winning_players_ids
            reward_for_winning_in_game = math.log2(1 + abs(homeaway_goal_delta))
            if self.number_of_games_played == 0:
                self.rating = 100 if player_was_in_winning_team else 0
            else:
                self.rating = (self.rating * self.number_of_games_played) +
                    (reward_for_winning_in_game * (1 if )
                self.rating /= self.number_of_games_played + 1
        self.number_of_games_played += 1

class Team:
    def __init__(self, players):
        self.players = players

    def get_rating(self):
        players_scores
        return sum([player.rating for player in self.players])

all_players = {}
def analyse_match(match):
    players_id_in_match = match[[col for col in matches.columns if "_player_" in col]]
    for player_id in players_id_in_match:
        if player_id not in all_players:
            all_players[player_id] = Player(player_id)
        all_players[player_id].update_rating(match)

matches.apply(analyse_match, axis=1)

matches_to_mlable = matches[["winning_team"]]

def calc_home_team_advantage_for_match(match):
    home_players = match[[col for col in matches.columns if "home_player" in col]]
    away_players = match[[col for col in matches.columns if "away_player" in col]]
    home_players = [all_players[player_id] for player_id in home_players]
    away_players = [all_players[player_id] for player_id in away_players]
    home_team = Team(home_players)
    away_team = Team(away_players)
    return home_team.get_rating() - away_team.get_rating()

matches_to_mlable["home_team_advantage"] = matches.apply(calc_home_team_advantage_for_match, axis=1)
matches_to_mlable.plot.scatter("home_team_advantage", "winning_team")
plt.show()




print("helllooo")