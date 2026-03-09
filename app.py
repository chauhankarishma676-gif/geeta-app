import streamlit as st

# 1. PAGE CONFIGURATION (Changes Tab Name)
st.set_page_config(
    page_title="Geeta AI Wisdom",
    page_icon="🙏",
    layout="centered"
)

# 2. APP TITLE
st.title("🙏 Geeta AI Wisdom")
st.markdown("---")

# 3. MAIN APP LOGIC
# The API Key check has been removed so users can use the app directly.

user_question = st.text_input("Enter your question here:", placeholder="e.g., How to find peace?")

if st.button("Seek Wisdom"):
    if user_question:
        with st.spinner("Generating wisdom..."):
            # --- YOUR AI LOGIC GOES HERE ---
            # Since you removed the API key requirement, put your AI code here.
            # If you have a key saved in Streamlit Secrets, it will use it automatically.
            
            # Example response (Replace this with your actual AI call):
            st.success("Here is your wisdom:")
            st.markdown("**Krishna says:** Perform your duty without attachment to the results.")
            
    else:
        st.warning("Please enter a question to proceed.")

# 4. SIDEBAR (Optional Info)
with st.sidebar:
    st.header("About")
    st.info("This app provides wisdom from the Bhagavad Geeta.")
