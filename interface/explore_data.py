import streamlit as st
import pandas as pd
# import networkx as nx
import matplotlib.pyplot as plt

N = 20
OUTLET_DATASET_URL = "https://raw.githubusercontent.com/sTechLab/local-news-dataset/main/local_news_outlets_dataset.csv"
OUTLET_DATASET_FILEPATH = './data/local_news_outlets_dataset.csv'
STATE_NAMES = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
    'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
    'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
    'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
    'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

def get_content_dataframe(selected_state, selected_ranking):
    selected_columns = ['Name', 'State', 'City', 'WebsiteUrl', 'TwitterId', 'FacebookId']
    extra_columns = ['TwitterFollowersCount', 'FacebookSubscriberCount', 'PopulationReach', 'ContentNetworkNeighbors'] 
    all_df = pd.read_csv(OUTLET_DATASET_FILEPATH).set_index('OutletId')
    df = all_df.copy()
    if selected_state != 'All':
            df = df[df.State == selected_state]
    if selected_ranking != 'All':
        if selected_ranking == "Highest Twitter Followers Count":
            df = df.sort_values(['TwitterFollowersCount', 'State', 'City', 'Name'], ascending=[False, True, True, True])
        elif selected_ranking == "Highest Facebook Subscribers Count":
            df = df.sort_values(['FacebookSubscriberCount', 'State', 'City', 'Name'], ascending=[False, True, True, True])
        elif selected_ranking ==  "Highest Population Reach":
            df = df.sort_values(['PopulationReach', 'State', 'City', 'Name'], ascending=[False, True, True, True])
        elif selected_ranking == "Lowest Population Reach":
            df = df.sort_values(['PopulationReach', 'State', 'City', 'Name'])
        elif selected_ranking == "Highest Content Network Neighbors":
            df = df.sort_values(['ContentNetworkNeighbors', 'State', 'City', 'Name'], ascending=[False, True, True, True])
        elif selected_ranking == "Lowest Content Network Neighbors":
            df = df.sort_values(['ContentNetworkNeighbors', 'State', 'City', 'Name'])
    # for printing
    for col in ['TwitterId', 'FacebookId'] + extra_columns:
        df[col] = df[col].apply(lambda x: str(int(round(x))) if pd.notnull(x) else x)
    df = df.fillna('')
    return df.head(N)[selected_columns + extra_columns]

# def get_network_graph():
#     G = nx.karate_club_graph()
#     fig, ax = plt.subplots()
#     pos = nx.kamada_kawai_layout(G)
#     nx.draw(G, pos, with_labels=True)
#     return fig

def get_explore_data_page(shared_state):
    st.header("Explore The Dataset")

    st.markdown("""
### This is the dataset
what is this dataset

""")
    
    col1, col2 = st.columns(2)
    selected_state = col1.selectbox(
        "Select State",
        ["All"] + sorted(STATE_NAMES) + ['non-US'],
    )
    selected_ranking = col2.selectbox(
        "Rank by",
        [
            "All",
            "Highest Twitter Followers Count",
            "Highest Facebook Subscribers Count",
            "Highest Population Reach",
            "Lowest Population Reach",
            "Highest Content Network Neighbors",
            "Lowest Content Network Neighbors"
        ],
    )

    st.table(get_content_dataframe(selected_state, selected_ranking))

    st.markdown("""
### Field Description
| Field      | Description                                                                                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutletId   | Unique local news outlet ID of this dataset (from 0 to 10256)                                                                                                                    |
| Name       | Name of the local news outlet                                                                                                                                                    |
| State      | Official United States Postal Service (USPS) Code for the States and District of Columbia, listed as “non-US” if outlet location is not in the US and “NA” if location not found |
| City       | Name of the city where the outlet is located, listed as “non-US” if outlet location is not in the US and “NA” if location not found                                              |
| WebsiteUrl | Website URL of the local news outlet                                                                                                                                             |
| TwitterId  | Unique identifier of Twitter account                                                                                                                                             |
| FacebookId | Unique identifier of Facebook account, also known as platformId on CrowdTangle                                                                                                   |
""")
 
    # st.pyplot(get_network_graph())



if __name__ == "__main__":
    get_explore_data_page()