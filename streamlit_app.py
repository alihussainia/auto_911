import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import streamlit as st
import time
import requests


def main():
    st.set_page_config(  # Alternate names: setup_page, page, layout
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Auto911 Platform",  # String or None. Strings get appended with "• Streamlit".
        page_icon="models/assets/logo.png",  # String, anything supported by st.image, or None.
    )
    st.title("Auto911 Platform")
    """Let AI help you!"""

    ex_questions = ["""
    sequence: "My father is having chest pain"
labels: ["Medical"]
###
sequence: "The neighbor is punching someone in his front yard"
labels: ["Police"]
###
sequence: "I just witnessed an accident"
labels: ["Medical"]
###
sequence: "My mother just collapsed"
labels: ["Medical"]
###
sequence: "I see smoke coming out of my neighbors house"
labels: ["Fire"]
###
sequence: "Flames are rising out of the building?"
labels: ["Fire"]
###
sequence: "I can see a man stealing the toyota corola car"
labels: ["Police"]
###
""",
    ]

    inp = st.text_area("Please enter your problem here",ex_questions,max_chars=2000, height=150)

    response = None
    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="Submit!")

        if submit_button:

            payload = {
                "context": inp+ex_questions[0],
                "token_max_length": 50,
                "temperature": 0.35,
                "top_p": 0.9,
            }

            query = requests.post("http://api.vicgalle.net:5000/classify/", params=payload)
            response = query.json()

            st.markdown(response) # ["prompt"] + response["text"]

    st.text("App developed with ❤️ by @alihussainia")


if __name__ == "__main__":
    main()





























