import streamlit as st
import pandas as pd
import numpy as np
import os


main_directory = os.getcwd()
target_directory = "archive"
work_directory = os.path.join(main_directory, target_directory)

fin_data = pd.read_csv(os.path.join(main_directory, "fin_data.csv"))

@st.cache_data
def read_data():
    data = pd.read_csv(os.path.join(main_directory, "fin_data.csv"))
    return data


def show_recommendation_page():
    data = read_data()
    st.data_editor(data, num_rows="dynamic")
    pass

show_recommendation_page()