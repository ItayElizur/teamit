import ast
from collections import OrderedDict
from typing import List

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State, ALL, MATCH

from teamit.player import Player
from teamit.sport_type import SportType

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

players: List[Player] = []
selected_players = []

app.layout = html.Div([
    html.Div('TeamIt', style={'padding': '40px', 'text-align': 'center', 'background': '#1abc9c',
                              'font-family': 'verdana', 'color': 'white', 'font-size': '40px',
                              'border-bottom': '6px solid green'}),
    html.Div(children=[
        html.Div(children=[
            dbc.Input(id='new-player-name', type='text', placeholder='Enter player name'),
            dcc.Slider(id='soccer-rank', min=1, max=10, step=1, value=5, marks={str(i): str(i) for i in range(1, 11)}),
            dbc.Button(children='Add Player', id='add-player', block=True, className='btn btn-primary'),
            html.Div(id='player-buttons', children=[
                dbc.Button(children=f'{player}', id=f'{i}', active=False, block=True, outline=True,
                           color='primary', className='mr-1')
                 for i, player in enumerate(players)]),
            html.Hr(style={'border': '5px solid green'}),
            # dbc.Button(children='Select all players', id='select-all', block=True, className='btn btn-primary'),
            dbc.Input(id='teams-number', type='number', min=2, step=1, max=6, value=2),
            dbc.Button(children='Create Teams', id='create-teams', block=True, className='btn btn-primary',
                       style={'bottom': '10px'}),
        ], className='col-3', style={'display': 'inline-block', 'border-right': '6px solid green', 'height': '500px'}),
        html.Div(id='teams', children=[], className='col-9', style={'display': 'inline-block'}),
    ], className='row'),
])


@app.callback(Output({'type': 'player-button', 'index': MATCH}, 'active'),
              Input({'type': 'player-button', 'index': MATCH}, 'n_clicks'),
              State({'type': 'player-button', 'index': MATCH}, 'active'))
def clicked(n_clicks, state):
    if not n_clicks or n_clicks == 0 or not dash.callback_context.triggered[0]['value']:
        return state
    state = not state
    player_idx = ast.literal_eval(dash.callback_context.triggered[0]['prop_id'].split('.')[0])['index']
    if state:
        selected_players.append(player_idx)
    else:
        selected_players.remove(player_idx)
    return state


# @app.callback(Output({'type': 'player-button', 'index': ALL}, 'n_clicks'),
#               Input('select-all', 'n_clicks'),
#               State({'type': 'player-button', 'index': ALL}, 'n_clicks'))
# def select_all(n_clicks, clicks):
#     if not n_clicks or n_clicks == 0 or not dash.callback_context.triggered[0]['value']:
#         return clicks
#     # selected_players = list(range(len(players)))
#     return [click + 1 for click in clicks]

@app.callback([Output('player-buttons', 'children'), Output('new-player-name', 'value'), Output('soccer-rank', 'value')],
              Input('add-player', 'n_clicks'),
              [State('new-player-name', 'value'), State('soccer-rank', 'value'), State('player-buttons', 'children')])
def add_player(n_clicks, name, rank, player_buttons):
    if not n_clicks or n_clicks == 0:
        return player_buttons, name, rank
    players.append(Player(name, {SportType.SOCCER: rank}))
    player_buttons.append(
        dbc.Button(children=f'{name}', id={'type': 'player-button', 'index': len(player_buttons)},
                   active=False, outline=True, n_clicks=0, color='primary', className='mr-1'))
    return player_buttons, None, 5


@app.callback(Output('teams', 'children'),
              Input('create-teams', 'n_clicks'),
              State('teams-number', 'value'))
def create_teams(n_clicks, teams_num):
    if not n_clicks or n_clicks == 0:
        return []
    children = []
    width = 12 // teams_num
    team_size = len(selected_players) // teams_num
    for num in range(teams_num):
        teamates = [players[selected_player].name for selected_player in selected_players[team_size*num:team_size*(num+1)]]
        children.append(
            html.Div(id=f'team-{num}', children=teamates, className=f'col-{width}', style={'display': 'inline-block'}))
    return children


if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
