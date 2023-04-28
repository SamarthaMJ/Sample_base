import streamlit as st
from deta import Deta

# Connect to Deta
deta = Deta("d0rvgq6trvd_F5YogUjMGK1SFTAusPwWWvv3MBPLoTrC")
db = deta.Base("new_base_2")

# Create Streamlit app
st.write("Please enter your name and age below:")

# Get user input
name = st.text_input("Name:")
age = st.number_input("Age:", min_value=0, max_value=120)

# Save to Deta database
if st.button("Submit"):
    db.put({'name': name, 'age': age})
    st.success("Your data has been saved!")

# Display all saved data
st.write("Here are all the users in the database:")
db_content = db.fetch().items
st.write(db_content)
