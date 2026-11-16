import html
import os
from pathlib import Path
from uuid import uuid4

import streamlit as st
import requests
from dotenv import load_dotenv

st.title("Game Info")

load_dotenv()

API_URL = os.getenv("API_URL", "").rstrip("/")

def get_game_id():
    response = requests.get(f"{API_URL}/Game/id")
    response.raise_for_status()
    return response.json()
    
with st.form("game_info_filter"):
    st.subheader("Filtres")
    game_id = st.selectbox("Enter Game ID :", options=get_game_id())
    submitted = st.form_submit_button("Filtrer")

if submitted:
    template_path = Path(__file__).resolve().parents[1] / "static" / "Game_info.html"
    game_info_html = template_path.read_text(encoding="utf-8")
    game_info_html = game_info_html.replace("__API_URL__", html.escape(API_URL, quote=True))
    game_info_html = game_info_html.replace("__GAME_ID__", html.escape(str(game_id), quote=True))
    game_info_html = game_info_html.replace("__APP_ID__", f"game-info-app-{uuid4().hex}")

    st.html(game_info_html, width="content", unsafe_allow_javascript=True)