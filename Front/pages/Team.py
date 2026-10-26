import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "").rstrip("/")

st.title("Team")

def get_team():
    response = requests.get(f"{API_URL}/Teams", timeout=10)
    response.raise_for_status()
    return pd.DataFrame(
        response.json(),
        columns=["team_id", "short_name", "team_name", "abbreviation"],
    )

if "df_team" not in st.session_state:
    try:
        st.session_state.df_team = get_team()
    except requests.RequestException as error:
        st.error(f"Impossible de récupérer les équipes : {error}")
        st.stop()


st.data_editor(
    st.session_state.df_team,
    key="team_editor",
    num_rows="dynamic",
    disabled=["team_id"],
    hide_index=True
)

if st.button("Enregistrer"):
    editor_state = st.session_state["team_editor"]
    
    # Extraire les types de changements
    edited_rows = editor_state.get("edited_rows", {})
    added_rows = editor_state.get("added_rows", [])
    deleted_rows = editor_state.get("deleted_rows", [])
    
    has_changes = edited_rows or added_rows or deleted_rows
    
    if has_changes:
        try:
            for row_index, changes in edited_rows.items():
                team = st.session_state.df_team.loc[int(row_index)].to_dict()
                team.update(changes)
                payload = {
                    field: team[field]
                    for field in ("short_name", "team_name", "abbreviation")
                }
                response = requests.put(
                    f"{API_URL}/Teams",
                    params={"team_id": team["team_id"]},
                    json=payload,
                )
                response.raise_for_status()

            for new_row in added_rows:
                payload = {
                    field: new_row[field]
                    for field in ("short_name", "team_name", "abbreviation")
                }
                response = requests.post(
                    f"{API_URL}/Teams", json=payload
                )
                response.raise_for_status()

            for row_index in deleted_rows:
                team_id = st.session_state.df_team.loc[int(row_index), "team_id"]
                response = requests.delete(
                    f"{API_URL}/Teams",
                    params={"team_id": team_id},
                )
                response.raise_for_status()

            st.session_state.df_team = get_team()
            st.success("Les équipes ont été enregistrées.")
            st.rerun()
        except requests.RequestException as error:
            st.error(f"Impossible d'enregistrer les équipes : {error}")