import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Travel Planner")
st.title("AI Travel Itineary planner")
st.write("plan your trip itineary by enter city and interests")

with st.form("planner_form"):
    city=st.text_input("enter the city")
    interest=st.text_input("Itineary values with comma seperate")
    submitted=st.form_submit_button("generate Itineary")

    if submitted:
        if city and interest:
            planner=TravelPlanner()
            planner.set_city(city)
            planner.set_interest(interest)
            itineary=planner.create_itineary()

            st.subheader("your Itineary")
            st.markdown(itineary)

        else:
            st.warning("fill city and interest dont miss anyone")