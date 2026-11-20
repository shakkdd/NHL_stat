import streamlit as st
import requests
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "").rstrip("/")


st.title("Players")
st.set_page_config(layout="wide")

st.session_state.setdefault("last_player_limit", 10)
st.session_state.setdefault("applied_player_params", {"page": 0})

def get_player(params):
    response = requests.get(f"{API_URL}/player", params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def get_position():
    response = requests.get(f"{API_URL}/player/position")
    response.raise_for_status()
    return response.json()


with st.form("player_filter"):
    st.subheader("Filtres")
    
    option_shoot = {
        "L" : "Gaucher",
        "R" : "Droitier"
    }
    
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("first name", placeholder="john")
        nationality = st.text_input("nationality", placeholder="USA")
        heigth = st.slider("taille (cm)",min_value=100, max_value=230, value=(100, 230))
        weight = st.slider("Poids", min_value=140,max_value=265, value=(130, 270))
        limit = st.selectbox("Nombre de joueur", [10, 20, 50])
    with col2:
        last_name = st.text_input("last name", placeholder="Doe")
        position = st.selectbox("Position", options= get_position(), index=None)
        birth_date = st.slider("Date naissance", min_value=date(1960,10,24), max_value=date(2001,9,11),
                                   value=(date(1960,10,24),date(2001,9,11)),format="DD/MM/YYYY")
        shoot_catches = st.pills("shoot catches", options=option_shoot.keys(), format_func=lambda option: option_shoot[option], selection_mode="single")
        offset = st.number_input("page", min_value=0, value=0, step=1)
    
    limit_changed = limit != st.session_state.last_player_limit
    submitted = st.form_submit_button("Filtrer")

if submitted or limit_changed:
    if submitted:
        params = {
            "first_name" : first_name,
            "last_name" : last_name,
            "nationality" : nationality,
            "min_birth_date" : birth_date[0],
            "max_birth_date" : birth_date[1],
            "position" : position,
            "min_heigth" : heigth[0],
            "max_heigth" : heigth[1],
            "min_weight" : weight[0],
            "max_weight" : weight[1],
            "shoots_catches" : shoot_catches
        }
        params.update({key: value for key, value in params.items() if value})
        st.session_state.applied_player_params = params
    else:
        params = st.session_state.applied_player_params.copy()
    
    params = {
        **params,
        "limit": int(limit),
        "page": int(offset * limit),
    }
    st.session_state.last_player_limit = limit
    
    try:
        player = get_player(params)
    except requests.RequestException as error:
        st.error(f"impossible de récuperer les joueur : {error}")
    else:
        if player:
            st.dataframe(player, hide_index=True, column_order=["first_name", "last_name", "nationality", "birth_city", "primary_position", "birth_date", "height", "height_cm", "weight", "shoots_catches"])
        else:
            st.info("Aucun joueur trouvé avec ces filtres.")
        