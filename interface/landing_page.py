import streamlit as st
from .image_urls import bucket_image_urls


def get_landing_page(shared_state):
    st.header("Local News")
    st.markdown(
        """
        ### Introduction

        ### Abstract

        During the COVID-19 pandemic, local news organizations have played an important role in keeping communities informed about the spread and impact of the virus.
        We explore how political, social media, and economic factors impacted the way local media reported on COVID-19 developments at a national scale between January 2020 and July 2021. 
        We construct and make available a dataset of over 10,000 local news organizations and their social media handles across the U.S.
        Building on this data, we analyze how local and national media covered four key COVID-19 news topics: *Statistics and Case Counts*, *Vaccines and Testing*, *Public Health Guidelines*, and *Economic Effects*.
        Our results show that news outlets with larger population reach reported proportionally more on COVID-19 than more local outlets.
        Separating the analysis by topic, we expose more nuanced trends, for example that outlets with a smaller population reach covered the *Statistics and Case Counts* topic proportionally more, and the *Economic Effects* topic proportionally less.
        Our analysis further shows that while people engaged proportionally less with outlets with a smaller population reach, they engaged proportionally more and used stronger reactions for COVID-19 posts.
        Finally, we demonstrate that COVID-19 posts in Republican-leaning counties generally received more comments and fewer likes than in Democratic counties, perhaps indicating controversy.

        ### Key Takeaways
        - first
        - second

        ### Privacy and Ethical Considerations


        *Marianne Aubin Le Quéré ([@marianneaubin](https://twitter.com/marianneaubin)), Ting-Wei Chiang ([@chiangtingwei](https://twitter.com/chiangtingwei)), Mor Naaman ([@informor](https://twitter.com/informor)).*

    """
    )
    
    # st.image(img, use_column_width=True)
    st.markdown("""
        ![Figure 1]({})
        **Figure 1:** This is a CT logo
    """.format(bucket_image_urls["ct-logo"]))


if __name__ == "__main__":
    get_landing_page()