# main.py
import streamlit as st
from streamlit.web import cli as stcli
import sys
import os

if __name__ == '__main__':
    # This is a programmatic way to run a Streamlit app.
    # It's useful for cases like this where you want to call another file.
    sys.argv = ["streamlit", "run", "model_ui.py"]
    sys.exit(stcli.main())