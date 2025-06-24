import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_TITLE = "Visual Timeline of Agent Collaboration"
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    LOG_FILE = os.path.join(DATA_DIR, "agent_logs.json")
    
    # Visualization settings
    TIMELINE_HEIGHT = 400
    DEFAULT_GROUP_BY = "topic"
    
    # Date format settings
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"