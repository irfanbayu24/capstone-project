import streamlit as st

# Importing the main_page function from page_1.py
from app import main_page


# Function to check credentials
def check_credentials(username, password):
    correct_username = "admin"  # Replace with actual username
    correct_password = "admin"  # Replace with actual password
    return username == correct_username and password == correct_password

# Function for login form
def login():
    st.title("Login Page Fraud Detection App")

    # Display the image
    st.image("dataset-cover.jpeg", use_column_width=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    
    
        #check credentials    

    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Main function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login()
    else:
        main_page()

if __name__ == "__main__":
    main()
