import html
import os
from pathlib import Path
from uuid import UUID, uuid4

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "").rstrip("/")

st.title("Player stat :")
st.set_page_config(layout="wide")

def get_player_team(player_id):
    response = requests.get(f"{API_URL}/Player_stat/{player_id}/Teams")
    response.raise_for_status()
    return response.json()

player_id = st.text_input("enter player id").strip()
player_id_is_valid = False
team_lookup_succeeded = False
teams = []

if player_id:
    try:
        UUID(player_id)
        player_id_is_valid = True
    except ValueError:
        st.info("Saisissez un UUID de joueur valide pour charger ses équipes.")

if player_id_is_valid:
    try:
        teams = get_player_team(player_id)
        team_lookup_succeeded = True
    except requests.RequestException as error:
        st.error(f"Impossible de récupérer les équipes du joueur : {error}")

with st.form("Player_stat"):
    team_options = ["Toutes les équipes", *teams]
    selected_team = st.selectbox(
        "Équipe",
        options=team_options,
        format_func=lambda team: team if isinstance(team, str) else team["abbreviation"],
        key=f"team_id_{player_id or 'empty'}",
        disabled=not team_lookup_succeeded or not teams,
    )
    
    col1, col2 = st.columns(2)
    with col1:
        limit = st.selectbox("Nombre de match", [10, 20, 50])
    with col2:
        offset = st.number_input("page", min_value=0, value=0, step=1)
                
    submitted = st.form_submit_button(
        "Filtrer",
        disabled=not player_id_is_valid or not team_lookup_succeeded,
    )
    
if submitted:
    template_path = Path(__file__).resolve().parents[1] / "static" / "Player_stat.html"
    player_stat_html = template_path.read_text(encoding="utf-8")
    player_stat_html = player_stat_html.replace("__API_URL__", html.escape(API_URL, quote=True))
    player_stat_html = player_stat_html.replace("__PLAYER_ID__", html.escape(player_id, quote=True))
    team_id = "" if isinstance(selected_team, str) else str(selected_team["team_id"])
    player_stat_html = player_stat_html.replace("__TEAM_ID__", html.escape(team_id, quote=True))
    player_stat_html = player_stat_html.replace("__LIMIT__", str(int(limit)))
    player_stat_html = player_stat_html.replace("__PAGE__", str(int(offset * limit)))
    player_stat_html = player_stat_html.replace("__APP_ID__", f"player-stat-app-{uuid4().hex}")

    st.html(player_stat_html, width="content", unsafe_allow_javascript=True)