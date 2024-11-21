import streamlit as st
import pandas as pd

st.title("AC/BC 🦦")
st.write(
    "Atlantic Canada Biochar Project\n Made by Brian Espinosa Acosta"
)

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
