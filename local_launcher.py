import os
import sys

script_path = os.path.join(os.path.dirname(__file__), "ac-bc_app.py")
os.system(f"streamlit run {script_path}")
