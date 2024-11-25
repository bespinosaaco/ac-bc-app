import streamlit as st
import acbc
import pandas as pd

ir = acbc.get_dpt_as_dataframe("/acbc1/20241119_BEA_P0.dpt")

st.dataframe(ir, use_container_width=False)