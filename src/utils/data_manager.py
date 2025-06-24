import json
from typing import List
from datetime import datetime
from config.config import Config
from src.models.agent_log import AgentLog

class DataManager:
    @staticmethod
    def save_logs(logs: List[AgentLog]):
        data = [log.dict() for log in logs]
        os.makedirs(os.path.dirname(Config.LOG_FILE), exist_ok=True)
        with open(Config.LOG_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def load_logs() -> List[AgentLog]:
        try:
            with open(Config.LOG_FILE, 'r') as f:
                data = json.load(f)
                return [AgentLog(**log) for log in data]
        except FileNotFoundError:
            return []