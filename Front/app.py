import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

st.title("NHL Stats")

