import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import Config
from src.components.sidebar import render_sidebar
from src.components.timeline import render_timeline
from src.utils.data_manager import DataManager

# Set page config
st.set_page_config(page_title=Config.APP_TITLE, layout="wide")

# Initialize session state
if 'logs' not in st.session_state:
    st.session_state.logs = DataManager.load_logs()

# Title
st.title(Config.APP_TITLE)

# Render sidebar and handle new entries
new_log = render_sidebar()
if new_log:
    st.session_state.logs.append(new_log)
    DataManager.save_logs(st.session_state.logs)
    st.success('Entry added successfully!')

# Render timeline
render_timeline(st.session_state.logs)

# Export functionality
if st.session_state.logs:
    if st.button('Export Logs'):
        df = pd.DataFrame([log.dict() for log in st.session_state.logs])
        
        st.download_button(
            label="Download as CSV",
            data=df.to_csv(index=False),
            file_name="agent_logs.csv",
            mime="text/csv"
        )
        
        st.download_button(
            label="Download as JSON",
            data=json.dumps([log.model_dump() for log in st.session_state.logs], indent=2),
            file_name="agent_logs.json",
            mime="application/json"
        )