from datetime import datetime
from pydantic import BaseModel

class AgentLog(BaseModel):
    agent_name: str
    message: str
    topic: str
    timestamp: datetime
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }