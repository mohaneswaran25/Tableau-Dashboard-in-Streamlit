import streamlit as st

def main():
    st.title("Tableau Dashboard in Streamlit")
    tableau_url = "https://public.tableau.com/views/HRAnalyticsDashboard_16972160897800/HRAnalyticsDashboard?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=no&:toolbar=yes&:animate_transition=yes&:display_static_image=no&:display_spinner=no&:display_overlay=yes&:display_count=yes&:language=en-US&:tooltip=no&:showShareOptions=false&publish=yes&:loadOrderID=0"

    st.write("Embedded Tableau Dashboard:")
    st.components.v1.iframe(tableau_url, width=1000, height=600, scrolling=True)

if __name__ == "__main__":
    main()
