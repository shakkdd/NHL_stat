import streamlit as st
import requests
import os
import pandas as pd
from uuid import UUID
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "").rstrip("/")

st.title("Player stat :")

def get_list_stat(params):
    player_id = params["player_id"]
    query_params = {
        key: params[key]
        for key in ("team_id", "limit", "page")
        if params.get(key) not in (None, "")
    }
    response = requests.get(f"{API_URL}/Player_stat/{player_id}", params=query_params)
    response.raise_for_status()
    return response.json()

def get_global_stat(params):
    player_id = params["player_id"]
    query_params = {}
    if params.get("team_id") not in (None, ""):
        query_params["team_id"] = params["team_id"]
    response = requests.get(f"{API_URL}/Player_stat/{player_id}/global_stat", params=query_params)
    response.raise_for_status()
    return response.json()

def get_player_team(player_id):
    response = requests.get(f"{API_URL}/Player_stat/{player_id}/Teams")
    response.raise_for_status()
    return response.json()

def convert_sec_to_hours(second):
    total_seconds = second    
        
    hours = total_seconds // 3600  
    remaining_seconds = total_seconds % 3600     
    minutes = remaining_seconds // 60   
    seconds = remaining_seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

st.session_state.setdefault("last_player_limit", 10)
st.session_state.setdefault("applied_player_stats_params", {"page": 0})

player_stats = pd.DataFrame()
player_stat_global = None

player_id = st.text_input("enter player id").strip()
player_id_is_valid = False
team_lookup_succeeded = False
team_ids = []

if player_id:
    try:
        UUID(player_id)
        player_id_is_valid = True
    except ValueError:
        st.info("Saisissez un UUID de joueur valide pour charger ses équipes.")

if player_id_is_valid:
    try:
        team_ids = get_player_team(player_id)
        team_lookup_succeeded = True
    except requests.RequestException as error:
        st.error(f"Impossible de récupérer les équipes du joueur : {error}")

with st.form("Player_stat"):
    team_options = ["Toutes les équipes", *team_ids]
    selected_team_id = st.selectbox(
        "enter player's team id",
        options=team_options,
        key=f"team_id_{player_id or 'empty'}",
        disabled=not team_lookup_succeeded or not team_ids,
    )
    
    col1, col2 = st.columns(2)
    with col1:
        limit = st.selectbox("Nombre de joueur", [10, 20, 50])
    limit_changed = limit != st.session_state.last_player_limit
    with col2:
        offset = st.number_input("page", min_value=0, value=0, step=1)
                
    submitted = st.form_submit_button(
        "Filtrer",
        disabled=not player_id_is_valid or not team_lookup_succeeded,
    )
    
if submitted:
    params = {"player_id": player_id}
    if selected_team_id != "Toutes les équipes":
        params["team_id"] = selected_team_id
    st.session_state.applied_player_stats_params = params
      
    params = {
        **params,
        "limit": int(limit),
        "page": int(offset * limit),
    }
    st.session_state.last_player_limit = limit
    
    try:
        player_stats = pd.DataFrame(get_list_stat(params))
    except requests.RequestException as error:
        st.error(f"impossible de récuperer les stats du joueur : {error}")
        
    try:
        player_stat_global = get_global_stat(params)
    except requests.RequestException as error:
        st.error(f"impossible de récuperer les stats global du joueur : {error}")
    
        
if player_stat_global:

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Goals", player_stat_global["total_goals"])
    with col2:
        st.metric("Assists", player_stat_global["total_assists"])
        st.metric("time on ice", convert_sec_to_hours(player_stat_global["total_time_on_ice"]))
    with col3:
        st.metric("Score", player_stat_global["total_plus_minus"])
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Short handed", convert_sec_to_hours(player_stat_global["total_short_handed_time_on_ice"]))
    with col2:
        st.metric("Even", convert_sec_to_hours(player_stat_global["total_even_time_on_ice"]))
    with col3:
        st.metric("Power play", convert_sec_to_hours(player_stat_global["total_power_play_time_on_ice"]))
        
    col1, col2, col3 = st.columns(3)
    with col1 :
        st.metric("Penalty in minute", player_stat_global["total_penalty_minutes"])
    with col2:
        st.metric("Face off taken", player_stat_global["total_face_off_taken"])
    with col3:
        st.metric("face off win", player_stat_global["total_face_off_wins"])
       
else:
    st.write("pas encore de joueur sélectionner")

if not player_stats.empty:
    st.dataframe(player_stats, hide_index=True, column_order=["game_id", "team_id", "time_on_ice", "goals", "assists", "shots", "power_play_goals", "power_play_assists", "penalty_minutes", "face_off_wins", "face_off_taken", "short_handed_goals", "short_handed_assists", "plus_minus", "even_time_on_ice", "short_handed_time_on_ice", "power_play_time_on_ice"])
else:
    st.write("Aucune statistique à afficher.")