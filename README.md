# Visual Timeline of Agent Collaboration

A Streamlit-based application for visualizing and tracking agent interactions over time. This project provides an interactive timeline view of agent collaborations, allowing users to track, analyze, and export agent communication logs.

## Features

- Interactive timeline visualization of agent interactions
- Real-time log entry addition through a user-friendly sidebar
- Flexible grouping by agent or topic
- Detailed log entry viewing with expandable sections
- Export functionality (CSV and JSON formats)
- Persistent data storage

## Project Structure
```
# Visual Timeline of Agent 
Collaboration

A Streamlit-based 
application for visualizing 
and tracking agent 
interactions over time. This 
project provides an 
interactive timeline view of 
agent collaborations, 
allowing users to track, 
analyze, and export agent 
communication logs.

## Features

- Interactive timeline 
visualization of agent 
interactions
- Real-time log entry 
addition through a 
user-friendly sidebar
- Flexible grouping by agent 
or topic
- Detailed log entry viewing 
with expandable sections
- Export functionality (CSV 
and JSON formats)
- Persistent data storage

## Project Structure
├── config/
│   └── config.py         # Configuration settings
├── src/
│   ├── components/       # UI components
│   │   ├── sidebar.py    # Sidebar input component
│   │   └── timeline.py   # Timeline visualization
│   ├── models/
│   │   └── agent_log.py  # Data models
│   └── utils/
│       └── data_manager.py # Data handling utilities
├── tests/
│   └── test_agent_log.py # Unit tests
└── requirements.txt      # Project dependencies

## Project Components
- Config : Manages application settings and constants
- Models : Defines data structures using Pydantic
- Components : Contains reusable UI elements
- Utils : Provides data management functionality

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request