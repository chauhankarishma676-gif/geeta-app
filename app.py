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
    /* Container for the App */
.app-container {
    max-width: 600px;
    margin: 120px auto;
    padding: 20px;
    text-align: center;
}

/* Input Area */
.input-area {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 30px;
}

#userInput {
    width: 70%;
    padding: 12px;
    border-radius: 8px;
    border: 2px solid #ccc;
    font-size: 16px;
}

button {
    padding: 12px 25px;
    background-color: #ff9933; /* Saffron color */
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    font-size: 16px;
}

button:hover {
    background-color: #e68a00;
}

/* The Result Card */
.shloka-card {
    background-color: #fff;
    color: #333;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    text-align: left;
    border-left: 5px solid #ff9933;
    animation: fadeIn 0.5s;
}

.verse-no {
    font-size: 0.9rem;
    color: #888;
    margin-bottom: 10px;
    text-transform: uppercase;
    font-weight: bold;
}

.sanskrit {
    font-size: 1.4rem;
    color: #d35400; /* Dark Orange/Saffron for Sanskrit */
    margin-bottom: 15px;
    font-weight: bold;
    text-align: center;
}

.hindi, .english {
    margin-top: 10px;
    font-size: 1rem;
    line-height: 1.5;
    color: #555;
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Container for the App */
.app-container {
    max-width: 600px;
    margin: 120px auto;
    padding: 20px;
    text-align: center;
}

/* Input Area */
.input-area {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 30px;
}

#userInput {
    width: 70%;
    padding: 12px;
    border-radius: 8px;
    border: 2px solid #ccc;
    font-size: 16px;
}

button {
    padding: 12px 25px;
    background-color: #ff9933; /* Saffron color */
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    font-size: 16px;
}

button:hover {
    background-color: #e68a00;
}

/* The Result Card */
.shloka-card {
    background-color: #fff;
    color: #333;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    text-align: left;
    border-left: 5px solid #ff9933;
    animation: fadeIn 0.5s;
}

.verse-no {
    font-size: 0.9rem;
    color: #888;
    margin-bottom: 10px;
    text-transform: uppercase;
    font-weight: bold;
}

.sanskrit {
    font-size: 1.4rem;
    color: #d35400; /* Dark Orange/Saffron for Sanskrit */
    margin-bottom: 15px;
    font-weight: bold;
    text-align: center;
}

.hindi, .english {
    margin-top: 10px;
    font-size: 1rem;
    line-height: 1.5;
    color: #555;
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
