import pytest
from datetime import datetime
from src.models.agent_log import AgentLog

def test_agent_log_creation():
    log = AgentLog(
        agent_name="TestAgent",
        message="Test message",
        topic="Testing",
        timestamp=datetime.now()
    )
    assert log.agent_name == "TestAgent"
    assert log.topic == "Testing"