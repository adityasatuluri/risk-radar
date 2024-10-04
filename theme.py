import streamlit as st

def red_dark():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@200..900&display=swap');

        body {
            color: white;
            background-color: #0E1117;
            font-family: 'Unbounded', sans-serif;
            font-weight: 200;
        }

        h1, h2 {
            font-family: 'Unbounded', sans-serif;
            color:  #FF2929;   Red primary color */
        }

        h1 {
            font-size: 3em;
            margin-bottom: 0.5em;
        }

        h2 {
            font-size: 2em;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            border-radius: 5px; /* Rounded corners */
            overflow: hidden; /* Ensure borders are rounded */
        }

        th, td {
            text-align: left;
            border: 1px solid #FF2929;  /* Red border */
        }

        th {
            background-color: #991b00;  /* Darker red background for headers */
            color: white;
        }

        tr:hover {
            background-color: rgba(252, 36, 3, 0.1); /* Light red hover effect */
        }

        .skill-button {
            display: inline-block;
            padding: 0.5em 1em;
            margin: 0.2em;
            border-radius: 15px;
            color: white;
            font-size: 0.9em;
            font-weight: 500;
            text-align: center;
            border: 0.5px solid #FF2929;  /* Red border */
        }

        .skill-button:hover {
            background-color: rgba(252, 36, 3, 0.4); /* Darker red on hover */
        }

        .stDownloadButton {
            background-color: #0E1117;
            color: #FF2929;  /* Red text for download button */
        }

        .stSidebar {
            background-color: #060E11;
        }

        .q-container {
            background-color: #200500;  /* Dark red container background */
            border-radius: 10px;
        }

        .r-container {
            background-color: #991b00;  /* Darker red response container */
            padding: 15px;
            border-radius: 10px;
        }

        .stChatMessage {
            background-color: transparent;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <style>
            * {
                font-weight: 200;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
