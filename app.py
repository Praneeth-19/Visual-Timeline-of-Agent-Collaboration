import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
from datetime import datetime
import json

# Set page config
st.set_page_config(page_title="Agent Collaboration Timeline", layout="wide")

# Initialize session state for logs if not exists
if 'logs' not in st.session_state:
    st.session_state.logs = []

# Function to add new log entry
def add_log_entry(agent_name, message, topic):
    log = {
        'agent_name': agent_name,
        'message': message,
        'topic': topic,
        'timestamp': datetime.now().isoformat()
    }
    st.session_state.logs.append(log)

# Title
st.title('Visual Timeline of Agent Collaboration')

# Sidebar for adding new entries
with st.sidebar:
    st.header('Add New Log Entry')
    agent_name = st.text_input('Agent Name')
    topic = st.text_input('Topic')
    message = st.text_area('Message')
    
    if st.button('Add Entry'):
        if agent_name and message and topic:
            add_log_entry(agent_name, message, topic)
            st.success('Entry added successfully!')

# Main content
if st.session_state.logs:
    # Convert logs to DataFrame
    df = pd.DataFrame(st.session_state.logs)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Group selection
    group_by = st.selectbox('Group by:', ['topic', 'agent_name'])
    
    # Create timeline visualization using plotly
    fig = px.timeline(df, 
                      x_start='timestamp',
                      x_end='timestamp',
                      y=group_by,
                      color=group_by,
                      hover_data=['message'])
    
    fig.update_layout(title='Agent Collaboration Timeline',
                      xaxis_title='Time',
                      yaxis_title=group_by.replace('_', ' ').title(),
                      height=400)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display detailed log entries
    st.header('Log Entries')
    for log in sorted(st.session_state.logs, key=lambda x: x['timestamp'], reverse=True):
        with st.expander(f"{log['topic']} - {log['agent_name']} ({log['timestamp']})"): 
            st.write(log['message'])
    
    # Export functionality
    if st.button('Export Logs'):
        df_export = pd.DataFrame(st.session_state.logs)
        st.download_button(
            label="Download as CSV",
            data=df_export.to_csv(index=False),
            file_name="agent_logs.csv",
            mime="text/csv"
        )
        
        # Export as JSON
        st.download_button(
            label="Download as JSON",
            data=json.dumps(st.session_state.logs, indent=2),
            file_name="agent_logs.json",
            mime="application/json"
        )
else:
    st.info('No log entries yet. Add some entries using the sidebar!')