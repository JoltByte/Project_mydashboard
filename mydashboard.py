import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Career Skills Dashboard")
st.write("This is a simple app to compare your skills with industry demand.")

st.sidebar.header("Enter Your Skills")
skills_input = st.sidebar.text_area("Write your skills (comma separated)", "Python, SQL, Machine Learning")

user_skills = [s.strip() for s in skills_input.split(",")]

industry_data = {
    "Skill": ["Python", "SQL", "Machine Learning", "Data Visualization", "Cloud Computing", "AI Ethics"],
    "Demand": [95, 80, 90, 70, 65, 50]
}
df = pd.DataFrame(industry_data)

st.subheader("Your Skills vs Industry Demand")
matched = df[df["Skill"].isin(user_skills)]

if not matched.empty:
    st.write("Here are your skills with demand levels:")
    st.dataframe(matched)

    fig, ax = plt.subplots()
    ax.bar(matched["Skill"], matched["Demand"], color="skyblue")
    ax.set_ylabel("Demand Level")
    ax.set_title("Your Skills Demand")
    st.pyplot(fig)
else:
    st.write("None of your skills matched the dataset. Try adding more common skills!")

st.subheader("Suggested Skills to Learn Next")
missing = [s for s in df["Skill"] if s not in user_skills]
st.write("You could learn these skills next:")
st.write(missing[:3])