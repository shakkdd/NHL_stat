import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "").rstrip("/")

st.title("Games")
st.set_page_config(layout="wide")

def get_game(params):
    response = requests.get(f"{API_URL}/Game", params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def get_outcome():
    response = requests.get(f"{API_URL}/Game/result")
    response.raise_for_status()
    return response.json()

def get_place():
    response = requests.get(f"{API_URL}/Game/place")
    response.raise_for_status()
    return response.json()

def get_season():
    response = requests.get(f"{API_URL}/Game/season")
    response.raise_for_status()
    return response.json()

def get_teams():
    response = requests.get(f"{API_URL}/Teams", timeout=10)
    response.raise_for_status()
    return response.json()

try:
    teams = get_teams()
except requests.RequestException as error:
    st.error(f"Impossible de récupérer les équipes : {error}")
    st.stop()

st.session_state.setdefault("last_game_limit", 10)
st.session_state.setdefault("applied_game_params", {"page": 0})

with st.form("game_filters"):
    st.subheader("Filtres")
    season = st.multiselect("season", options=get_season())
    
    option_game = {
        "P" : "Play-off",
        "R" : "Regular season" 
    }
    game_type = st.pills("Type de match",options=option_game.keys(), format_func=lambda option: option_game[option] , selection_mode="single")
    
    col1, col2 = st.columns(2)
    with col1:
        team_1 = st.selectbox(
            "Équipe 1",
            options=teams,
            format_func=lambda team: team["abbreviation"],
            index=None,
        )
        
        outcome = st.multiselect("outcome", options=get_outcome())
        
        limit = st.selectbox("Nombre de matchs", [10, 20, 50])
    with col2:
        team_2 = st.selectbox(
            "Équipe 2",
            options=teams,
            format_func=lambda team: team["abbreviation"],
            index=None,
        )
        
        venue = st.selectbox("salle", options= get_place(), index=None)
        
        offset = st.number_input("page", min_value=0, value=0, step=1)
 
    limit_changed = limit != st.session_state.last_game_limit
    submitted = st.form_submit_button("Filtrer")

if submitted or limit_changed:
    if submitted:
        params = {
            "page": int(offset * limit),
        }
        optional_params = {
            "season": season,
            "type": game_type,
            "team_1": team_1["abbreviation"] if team_1 else None,
            "team_2": team_2["abbreviation"] if team_2 else None,
            "outcome": outcome,
            "venu": venue,
        }
        params.update({key: value for key, value in optional_params.items() if value})
        st.session_state.applied_game_params = params
    else:
        params = st.session_state.applied_game_params.copy()

    params = {
        **params,
        "limit": int(limit),
    }
    st.session_state.last_game_limit = limit

    try:
        games = get_game(params)
    except requests.RequestException as error:
        st.error(f"Impossible de récupérer les matchs : {error}")
    else:
        if games:
            st.dataframe(
                games,
                column_order=[
                    "season",
                    "type",
                    "date_time",
                    "away_team_abbreviation",
                    "home_team_abbreviation",
                    "away_goals",
                    "home_goals",
                    "outcome",
                    "venue",
                ],
            )
        else:
            st.info("Aucun match trouvé avec ces filtres.")