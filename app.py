import streamlit as st

# Initialize session state for user authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Initialize user data (this would typically be a database in a real application)
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}

# Create a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Go to", ["Home", "Login", "Sign Up", "Dashboard", "Settings", "User   Profile", "Applicant Portal", "Selection Team Portal"])

# Sign Up Page
def sign_up():
    st.title("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        if email in st.session_state['user_data']:
            st.error("Email already exists! Please log in or use a different email.")
        elif password == confirm_password:
            # Save the new user (for demo purposes)
            st.session_state['user_data'][email] = password  
            st.success("Account created successfully! You can now log in.")
        else:
            st.error("Passwords do not match!")

# Login Page
def login():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Check the credentials against the stored user data
        if email in st.session_state['user_data'] and st.session_state['user_data'][email] == password:
            st.session_state['authenticated'] = True
            st.success("Login successful!")
            # Redirect to home after logging in
            st.rerun()  # Refresh the app to navigate to the home page
        else:
            st.error("Invalid email or password.")

# Home Page
def home():
    st.title("Welcome to SAND Technologies Talent Platform")
    st.write("Select an option from the sidebar to get started.")

# Create content based on selection
if st.session_state['authenticated']:
    if selection == "Home":
        home()
    elif selection == "Dashboard":
        st.title("Dashboard")
        st.write("This is your dashboard.")
    elif selection == "Settings":
        st.title("Settings")
        st.write("Manage your application settings here.")
    elif selection == "User   Profile":
        st.title("User   Profile")
        st.write("View and edit your profile details here.")
    elif selection == "Applicant Portal":
        st.title("Applicant Portal")
        st.write("Welcome to the applicant portal. Here you can view and manage your applications.")
    elif selection == "Selection Team Portal":
        st.title("Selection Team Portal")
        st.write("Welcome to the selection team portal. Here you can manage applications and teams.")
else:
    if selection == "Login":
        login()
    elif selection == "Sign Up":
        sign_up()
    else:
        st.warning("Please log in or sign up to access the other pages.")

