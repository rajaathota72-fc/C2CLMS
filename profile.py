import streamlit as st
def display(profile_details,rating,rewards):
    avatar = profile_details["Avatar"]
    name =  profile_details["Name"]
    st.markdown("<h1 style='text-align:center; color: #0ea2bd;'> Name: " + name + "</h1>", unsafe_allow_html=True)
    st.markdown("___")
    cols = st.columns([0.75,1,1])
    cols[0].image("Images/Profileavatars/"+avatar+".png",width=225)
    cols[1].markdown("")
    cols[2].markdown("")
    cols[1].markdown("<h3 style='text-align:center; color: #ffffff;'>Rewards</h3>",unsafe_allow_html=True)
    cols[2].markdown("<h3 style='text-align:center; color: #ffffff;'>Skill Rating</h3>", unsafe_allow_html=True)
    cols[1].markdown("<h1 style='text-align:center; color: #FFD700;'>"+ str(int(rewards))+"✨"+"</h1>", unsafe_allow_html=True)
    cols[2].markdown("<h1 style='text-align:center; color: #0ea2bd;'>"+ str(int(rating)*"💫")+"</h1>", unsafe_allow_html=True)
    cols[1].markdown("<h6 style='text-align:center; color: #0ea2bd;'>(100 max)</h5>", unsafe_allow_html=True)
    cols[2].markdown("<h6 style='text-align:center; color: #0ea2bd;'>(5 star max)</h5>", unsafe_allow_html=True)


