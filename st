import streamlit as st

# Create a list of options for the multiselection drop-down
options = ["dog", "cat", "elephant", "rat", "mat"]

# Create a multiselection drop-down widget with a type hint
selected_options: List[str] = st.multiselect("Select options:", options)

# Print the selected options to the UI
st.write(selected_options)
