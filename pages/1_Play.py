import streamlit as st

def calc_score(xg_guess, xg, psxg_guess, psxg):

  score = round(((xg_guess - xg)**2 + (psxg_guess - psxg)**2)**(1/2))

  return(score)
  
def increment_counter():
  st.session_state.counter += 1

data = {
1: {"goal": 'https://www.youtube.com/watch?v=qAG6FThzX18', "xg": 14, "psxg": 50},
2: {"goal": 'https://www.youtube.com/watch?v=dbH60x3l9o8', "xg": 42, "psxg": 93},
}
  
counter = 1
if "counter" not in st.session_state: st.session_state["counter"] = counter
if st.session_state["counter"] > len(data): st.session_state["counter"] = 1

st.title("The xG Game")

col1, col2 = st.columns(2)

col1.video(data[st.session_state["counter"]]["goal"])

xg_guess = col2.slider("Guess The xG %", min_value = 0, max_value = 100, value = 50, step = 1)
psxg_guess = col2.slider("Guess The PSxG %", min_value = 0, max_value = 100, value = 50, step = 1)
submit = col2.button("Submit")
placeholder1 = col2.text("""Your score will show here after submission.""")
next_goal = col2.button("Next Goal", on_click = increment_counter)

if submit:
  with placeholder1.container(): 
    st.text("""
    Your xG: {}% - Actual xG: {}% 
    Your PSxG: {}% - Actual PSxG: {}% 
    Your Score: {}
    """.format(
    xg_guess, 
    data[st.session_state["counter"]]["xg"], 
    psxg_guess, 
    data[st.session_state["counter"]]["psxg"], 
    calc_score(xg_guess, data[st.session_state["counter"]]["xg"], psxg_guess, data[st.session_state["counter"]]["psxg"]))
    )
 


