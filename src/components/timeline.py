import streamlit as st
import plotly.express as px
from typing import List
from src.models.agent_log import AgentLog
from config.config import Config

def render_timeline(logs: List[AgentLog]):
    if not logs:
        st.info('No log entries yet. Add some entries using the sidebar!')
        return
        
    df = pd.DataFrame([log.dict() for log in logs])
    group_by = st.selectbox('Group by:', ['topic', 'agent_name'])
    
    fig = px.timeline(
        df,
        x_start='timestamp',
        x_end='timestamp',
        y=group_by,
        color=group_by,
        hover_data=['message']
    )
    
    fig.update_layout(
        title='Agent Collaboration Timeline',
        xaxis_title='Time',
        yaxis_title=group_by.replace('_', ' ').title(),
        height=Config.TIMELINE_HEIGHT
    )
    
    st.plotly_chart(fig, use_container_width=True)