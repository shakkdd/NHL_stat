from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql+psycopg2://{os.getenv("DB_PATH")}"

engine = create_engine(DATABASE_URL)

session_local =  sessionmaker(bind = engine, autocommit = False)

class Base(DeclarativeBase):
    pass

def getdb():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        
def init_db():
    from API.models import Game, Game_goalie_stats, Game_goals, Game_play_players
    from API.models import Game_shift, Game_skater_stats, Game_team_stats, Penaltie, Player, Play, Team
    
    Base.metadata.create_all(bind= engine)