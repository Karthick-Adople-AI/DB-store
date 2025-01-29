import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Set the name of the CSV file
CSV_FILE = "data.csv"

# Load existing data if the CSV file exists
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["Date", "Members"])

# Function to add a new entry
def add_entry(date, value):
    new_entry = {"Date": date, "Members": value}
    df.loc[len(df)] = new_entry
    df.to_csv(CSV_FILE, index=False)
    st.success("Entry added successfully!")

# Streamlit UI
st.title("Store and Edit Member Data")

# Input fields for manual entry
col1, col2 = st.columns(2)
with col1:
    selected_date = st.date_input("Select a Date", datetime.today())
with col2:
    value = st.text_input("Enter number of members:")

# Save button
if st.button("Save"):
    if value.strip().isdigit():
        add_entry(selected_date.strftime("%Y-%m-%d"), int(value))
    else:
        st.error("Please enter a valid numeric value.")

# Display existing data with edit functionality
st.subheader("Current Data")
if not df.empty:
    edited_df = st.data_editor(df, num_rows="dynamic")  # Allows editing

    # Save changes
    if st.button("Update Data"):
        edited_df.to_csv(CSV_FILE, index=False)
        st.success("Data updated successfully!")

    # Total calculation
    total_amount = edited_df["Members"].sum() * 60
    st.subheader(f"Total Amount: {total_amount} RS")
else:
    st.write("No data available yet.")
