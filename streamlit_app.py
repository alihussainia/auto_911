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
Q: "My father is having chest pain"\n
A: Tell me exactly what happened\n
###\n
Q: "The neighbor is punching someone in his front yard"\n
A: Tell me exactly what happened\n
###\n
Q: "My mother just collapsed"\n
A: Tell me exactly what happened\n
###\n
Q: "I just witnessed an accident"\n
A: Tell me exactly what happened\n
###\n
Q: "I see smoke coming out of my neighbors house"\n
A: Tell me exactly what happened\n
###\n
Q: "Is the patient conscious?"\n
A: No, he is not\n
###\n
Q: "Is the patient breathing?"\n
A: Yeah, he is breathing\n
###\n

Q: Fetch the three max salaries from the Worker table;\n
A:""",
    ]

    inp = st.text_area("Please enter your problem here",ex_questions,max_chars=2000, height=150)

    response = None
    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="Submit!")

        if submit_button:

            payload = {
                "context": inp,
                "token_max_length": 50,
                "temperature": 0.35,
                "top_p": 0.9,
            }

            query = requests.post("http://api.vicgalle.net:5000/generate", params=payload)
            response = query.json()

            st.markdown(response["prompt"] + response["text"])
            st.text(f"Replied in {response['compute_time']:.3} s.")

    if False:
        col1, col2, *rest = st.beta_columns([1, 1, 10, 10])

        def on_click_good():
            response["rate"] = "good"
            print(response)

        def on_click_bad():
            response["rate"] = "bad"
            print(response)

        col1.form_submit_button("👍", on_click=on_click_good)
        col2.form_submit_button("👎", on_click=on_click_bad)

    st.text("App developed with ❤️ by @alihussainia")


if __name__ == "__main__":
    main()





























