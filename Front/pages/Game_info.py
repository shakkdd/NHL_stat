import streamlit as st
import requests
import os
from datetime import date
from dotenv import load_dotenv

st.title("Game Info")

load_dotenv()

API_URL = os.getenv("API_URL", "").rstrip("/")

def get_game_info(game_id, params):
    response = requests.get(f"{API_URL}/Game_info/{game_id}", params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def get_game_id():
    response = requests.get(f"{API_URL}/Game/id")
    response.raise_for_status()
    return response.json()
    


with st.form("game_info_filter"):
    st.subheader("Filtres")
    game_id = st.selectbox("Enter Game ID :", options=get_game_id())
    
    st.session_state.setdefault("last_game_info_limit", 10)
    st.session_state.setdefault("applied_game_info_params", {"page": 0})
    
    limit = st.selectbox("Nombre de play", [10, 20, 50])
    limit_changed = limit != st.session_state.last_game_info_limit
    offset = st.number_input("page", min_value=0, value=0, step=1)
    submitted = st.form_submit_button("Filtrer")

if submitted or limit_changed:
    if submitted:
        params = {
            "limit": limit,
            "page": offset*limit
        }
        st.session_state.applied_game_info_params = params
        st.session_state.last_game_info_limit = limit
    else:
        params = st.session_state.applied_game_info_params

    try:
        game_info_data = get_game_info(game_id, params)
        if game_info_data:
            st.dataframe(game_info_data, column_order=["against_team_id", "for_team_id", "period_type", "period", "period_time","event", "secondary_type", "x", "y", "description", "goals_home", "goals_away", "st_x", "st_y"])
        else:
            st.warning("No data found for the given Game ID.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching game info: {e}")