import streamlit as st

st.title("The xG Game")

st.markdown("""
Expected Goals, xG, is a statistic that has been increasingly visible in football, but what does it mean? You'd look at an opportunity and say, "He should score there!", or "That was a tough chance," xG does the same but attaches a probability. The probability is based on historical shot data and a number of factors dependent on who made the xG model. 

Two factors xG models don't use is the way the player hits the shot, and which part of the goal it is hit to. That's what Post Shot Expected Goals, PSxG, models do, i.e it uses the same factors as its companion xG model plus these two. A notable difference between the two metrics based on their definitions is that off target shots can have an xG of any value, while their PSxG is always 0.

So let's play the xG Game! You have ten shots that ended up in goals, and you have to guess the xG and PSxG of each as a percentage. A perfect score is 0 because your guesses and the actual value would match up perfectly. The theoretical worse score is 100 in the context of this game. (If you're curious the score being used is the Brier score: https://en.wikipedia.org/wiki/Brier_score.) All data comes from FBREF via Opta: https://fbref.com/en/matches/3a6836b4/Burnley-Manchester-City-August-11-2023-Premier-League. Scroll down to the "Shots" table to see the data.

Go the the Play tab to begin.
""")
