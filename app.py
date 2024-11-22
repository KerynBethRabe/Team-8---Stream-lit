import streamlit as st

st.set_page_config(page_title="SAND Tech Technologies Talent Platform")


def create_login_page():
    st.title("SAND  Tech Technologies Talent Platform")
    
    with st.form("login_form"):
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            # Add your authentication logic here
            st.success("Login successful!")
            
    st.markdown("---")
    st.markdown("Don't have an account? [Sign Up](#)")

def create_signup_page():
    st.title("Sign Up for SAND Tech Technologies Talent Platform")
    
    with st.form("signup_form"):
        st.subheader("Create New Account")
        
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name")
        with col2:
            last_name = st.text_input("Last Name")
            
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        # Terms and conditions checkbox
        terms = st.checkbox("I agree to the Terms and Conditions")
        
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            if password != confirm_password:
                st.error("Passwords don't match!")
            elif not terms:
                st.error("Please accept the Terms and Conditions")
            else:
                # Add your registration logic here
                st.success("Account created successfully!")

def main():
    # Create a sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Login", "Sign Up"])
    
    if page == "Login":
        create_login_page()
    else:
        create_signup_page()

if __name__ == "__main__":

    
    # Add custom CSS for styling
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            background-color: #6B46C1;
            color: white;
        }
        .stForm {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)
    
    main()
