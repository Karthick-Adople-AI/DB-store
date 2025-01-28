import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Set the name of the CSV file
CSV_FILE = "data.csv"

# Function to add a new entry
def add_entry(value):
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Create a new entry
    new_entry = {"Date": current_date, "Value": value}
    
    # Check if the CSV file exists
    if os.path.exists(CSV_FILE):
        # Append the new entry to the existing file
        df = pd.read_csv(CSV_FILE)
        df = df.append(new_entry, ignore_index=True)
    else:
        # Create a new DataFrame for the new entry
        df = pd.DataFrame([new_entry])
    
    # Save the DataFrame to the CSV file
    df.to_csv(CSV_FILE, index=False)
    st.success("Entry added successfully!")

# Streamlit app UI
st.title("Store Values with Current Date")

# Input field for the value
value = st.text_input("Enter a value:")

# Button to save the value
if st.button("Save"):
    if value.strip():
        add_entry(value)
    else:
        st.error("Please enter a valid value.")

# Display the current content of the CSV file
st.subheader("Current Data")
if os.path.exists(CSV_FILE):
    data = pd.read_csv(CSV_FILE)
    st.dataframe(data)
else:
    st.write("No data available yet.")
