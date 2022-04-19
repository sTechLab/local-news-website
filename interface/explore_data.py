import streamlit as st
import pandas as pd

TOP_N = 20
OUTLETS_FILEPATH = 'interface/data/outlet_example.csv'

def get_content_dataframe():
    selected_columns = ['Name', 'State', 'City', 'WebsiteUrl', 'TwitterHandle', 'FacebookUrl', 'CreatedAt']
    df = pd.read_csv(OUTLETS_FILEPATH).set_index('OutletId')
    return df[selected_columns].head(TOP_N)

def get_explore_data_page(shared_state):
    st.header("Explore The Dataset")

    st.markdown("""
        # This is the dataset
    """)

    st.table(get_content_dataframe())


if __name__ == "__main__":
    get_explore_data_page()