import streamlit as st
import os, re
from interface.landing_page import get_landing_page
from interface.explore_data import get_explore_data_page
import interface.SessionState as SessionState
from interface.image_urls import bucket_image_urls

st.set_page_config(
    page_title="Local News - a Social Media Dataset",
    page_icon="./interface/img/favicon.ico",
    initial_sidebar_state="expanded",
)


@st.cache
def insert_html_header(name, snippet):
    a = os.path.dirname(st.__file__) + "/static/index.html"
    with open(a, "r") as f:
        data = f.read()
        if snippet not in data:
            print("Inserting {}".format(name))
            with open(a, "w") as ff:
                new_data = re.sub("<head>", "<head>" + snippet, data)
                ff.write(new_data)
        else:
            print("{} already inserted".format(name))


## Google analytics
# insert_html_header(
#     "Google Analytics Tag",
#     """
# <!-- Global site tag (gtag.js) - Google Analytics -->
# <script async src="https://www.googletagmanager.com/gtag/js?id=G-[id]"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){dataLayer.push(arguments);}
#   gtag('js', new Date());

#   gtag('config', 'G-[id]');
# </script>
# """,
# )

query_params = st.experimental_get_query_params()
app_state = st.experimental_get_query_params()

session_state = SessionState.get(first_query_params=query_params)
first_query_params = session_state.first_query_params

PAGES = {
    "Overview": get_landing_page,
    "Explore The Dataset": get_explore_data_page,
}
PAGE_OPTIONS = list(PAGES.keys())

LIMIT = None

class SharedState:
    pass


@st.cache(allow_output_mutation=True)
def prepare_shared_state():
    print("Preparing Shared State")
    state = SharedState()
    print("Shared State Loaded")
    return state


def get_selected_page_index():
    # query_params = st.experimental_get_query_params()
    if "page" in app_state:
        if "page" in first_query_params:
            selected_page = first_query_params["page"][0]
            if selected_page in PAGE_OPTIONS:
                return PAGE_OPTIONS.index(selected_page)
    return 0


shared_state = prepare_shared_state()

## CSS
st.markdown(
    """
    <style>
    img.logo {
        margin: 0px auto;
        margin-top: -45px;
        margin-bottom: 25px;
        width: 200px;
    }

    img.logo-2 {
        margin: 0px auto;
        margin-top: 25px;
        width: 200px;
    }

    img {
        max-width: 100%;
    }
    </style>
""",
    unsafe_allow_html=True,
)


st.sidebar.markdown(
    """
    <img src="{}" class="logo" alt="CT logo" />
""".format(
        bucket_image_urls["jacobs-logo-transparent"]
    ), unsafe_allow_html=True
)


#st.sidebar.title("Go to")

selection = st.sidebar.radio("Go to", PAGE_OPTIONS, index=get_selected_page_index())

st.sidebar.markdown(
    """
    - [The Paper (arXiv)]()
    - [Download The Full Dataset (Github)](https://github.com/sTechLab/local-news-dataset)  
"""
)

app_state["page"] = selection


def get_query_params():
    if PAGE_OPTIONS.index(selection) == 0:
        return {}
    else:
        return {"page": app_state["page"]}


st.experimental_set_query_params(**get_query_params())

page = PAGES[selection]
page(shared_state)
