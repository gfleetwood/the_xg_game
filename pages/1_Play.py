import streamlit as st

def calc_score(xg_guess, xg, psxg_guess, psxg):

  score = ((xg_guess - xg)**2 + (psxg_guess - psxg)**2)**(1/2)

  return(score)
  
counter = 1
if "counter" not in st.session_state: st.session_state["counter"] = counter

data = {
1: {"goal": 'https://www.youtube.com/watch?v=qAG6FThzX18', "xg": 14, "psxg": 50},
2: {"goal": 'https://www.youtube.com/watch?v=FeUNSrVtRgw', "xg": 14, "psxg": 50},
}

st.title("The xG Game")

st.video(data[1]["goal"])

#col1, col2 = st.columns(2)

xg_guess = st.slider("Guess The xG %", min_value = 0, max_value = 100, value = 50, step = 1)
psxg_guess = st.slider("Guess The PSxG %", min_value = 0, max_value = 100, value = 50, step = 1)
submit = st.button("Submit")
placeholder1 = st.text("""Your score will show here after submission.""")
#next_goal = st.button("Go To Next Goal")

if submit:
  with placeholder1.container(): 
    st.text("""
    Your xG: {} - Actual xG: {}
    Your PSxG: {} - Actual PSxG: {}
    Your Score: {}
    """.format(xg_guess, data[st.session_state["counter"]]["xg"], psxg_guess, data[st.session_state["counter"]]["psxg"], calc_score(xg_guess, data[st.session_state["counter"]]["xg"], psxg_guess, data[st.session_state["counter"]]["psxg"])))
    
#if next_goal:
#  st.session_state["counter"] = st.session_state["counter"] + 1
#  print(st.session_state["counter"])
    
 


