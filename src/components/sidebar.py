import streamlit as st
from datetime import datetime
from src.models.agent_log import AgentLog

def render_sidebar() -> AgentLog:
    st.sidebar.header('Add New Log Entry')
    
    agent_name = st.sidebar.text_input('Agent Name')
    topic = st.sidebar.text_input('Topic')
    message = st.sidebar.text_area('Message')
    
    if st.sidebar.button('Add Entry'):
        if agent_name and message and topic:
            return AgentLog(
                agent_name=agent_name,
                message=message,
                topic=topic,
                timestamp=datetime.now()
            )
    return None