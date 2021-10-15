# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 06:54:00 2021
@author: Muhammad Ali
@github: @alihussainia
"""

import streamlit as st
import requests

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


st.set_page_config(page_title="Auto911 AI based Emergency Response Application", page_icon="pill", layout='centered', initial_sidebar_state='auto', menu_items=None)

st.title("Auto 911 App")
st.write("A web app that answers your 911 queries using AI")

inp = st.text_area("Please enter your problem here", max_chars=2000, height=150)

context = """A 911 emergency is when someone needs help right away because of an injury or an immediate danger. For example, call 911 if: there's a fire. someone has passed out. someone suddenly seems very sick and is having a hard time speaking or breathing or turns blue.

Q:Emergency! Armed person on campus
A:This is Jane, 911 operator from an EMERGENCY response team. You reported that there is an armed individual at large on campus. [Shots have been fired.] If you are on campus, go into the nearest available room and lock the door. If you are not on campus, stay away. This threat is real and imminent! Follow instructions from university officials or local authorities. More information on campus emergencies may be found at WEB ADDRESS. Go to nearest room and lock door. If off campus, do not enter campus. Follow instructions from authorities. 

Q:Hostile intruder on campus
A:Evacuate immediately from where you are right now and hide somewhere. Remain calm. Follow the instructions of emergency and other university personnel. After leaving the area, go to the YOUR UNIVERSITY Emergency web site: _______________________or other local sources for more information. Please limit phone use so phone lines are available for emergency messaging. Standby for additional messages. Personnel in those areas not listed for evacuation should remain in place, be alert to changing conditions.

Q:Emergency! The lab is under a biological threat
A: If you are in the vicinity of campus, prepare immediately for possible evacuation. Listen for instructions from university officials or local authorities and follow them quickly and carefully. More information on campus emergencies, especially steps to take if you notice a suspicious substance, may be found at WEB ADDRESS

Q:Fuck! Bomb has been found on campus
A:This is Jane, 911 operator from an Rescue Squad. If you are in the vicinity of the [building], prepare immediately for possible evacuation. If you are not in the area, stay away. Listen for instructions from university officials or local authorities and follow them quickly and carefully.

Q:I see smoke coming out of my neighbors house
A:Please do not get close to your neighbors house but please try calling them to make sure is it Fire or they are doing barbeque!

Q:How to remove Fire from clothing?
A:Roll around on floor to smother flame or drench with water. Obtain medical attention; if necessary, call 911 (9-911 from a campus phone). Report incident to supervisor and/or the Police

Q: Someone attacked my friend and he has recieved minor cuts and puncture wounds
A: Please guide him/her to vigorously wash injury with soap and water for several minutes. Obtain medical attention and report incident to supervisor and/or the Police, 

Q: There is FIre in the building
A: Collect your personal belongings (ie. purse, briefcase, etc.) and take them with you as you exit the building. After evacuation, report to an Emergency Assembly Area. Do not reenter the building until instructed to do so by appropriate personnel (University Police, Boone Police Department or Boone Fire Department).

"""

response = None

submit_button = st.button('Help!')
payload={}
if submit_button and inp=="":
  st.write("Please enter your problem above")

elif submit_button and inp!="":
  payload = {
      "context": context+inp,
      "token_max_length": 100,
      "temperature": 1.0,
      "top_p": 0.9,
  }

  response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()

  st.markdown(response["text"]) 


st.text("App developed with ❤️ by @alihussainia")

st.text(f"Connect with me via Email at malirashid1994@gmail.com")
