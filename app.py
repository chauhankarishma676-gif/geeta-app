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
    import streamlit as st

# --- 1. PAGE CONFIG & STYLING ---
st.set_page_config(page_title="Geeta AI Wisdom", page_icon="🙏")

# Custom CSS to make it look colorful (Embedded in Python)
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .shloka-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #ff9933; /* Saffron border */
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
        animation: fadeIn 1s;
    }
    .sanskrit-text {
        font-size: 26px;
        color: #d35400;
        font-weight: bold;
        text-align: center;
        margin-bottom: 15px;
    }
    .translation-box {
        background-color: #fff8e1;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)


# --- 2. THE SHLOKA DATABASE ---
geeta_data = [
    {
        "keywords": ["fear", "afraid", "scared", "worry", "dar", "anxiety"],
        "chapter": 2, "verse": 56,
        "sanskrit": "दुःखेष्वनुद्विग्नमनाः सुखेषु विगतस्पृहः। वीतरागभयक्रोधः स्थितधीर्मुनिरुच्यते॥",
        "hindi": "जो सुख में आसक्त नहीं होता और दुख में व्याकुल नहीं होता, जो राग, भय और क्रोध से मुक्त है, वही स्थितप्रज्ञ मुनि कहलाता है।",
        "english": "One who is not disturbed by misery and is free from desire for pleasure, who is free from attachment, fear, and anger, is called a sage of steady wisdom."
    },
    {
        "keywords": ["work", "job", "duty", "karma", "karm", "action"],
        "chapter": 2, "verse": 47,
        "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥",
        "hindi": "तेरा कर्म करने में ही अधिकार है, फल में कभी नहीं।",
        "english": "You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions."
    },
    {
        "keywords": ["sad", "grief", "cry", "death", "marna", "lost"],
        "chapter": 2, "verse": 20,
        "sanskrit": "न जायते म्रियते वा कदाचिन्नायं भूत्वा भविता वा न भूयः।",
        "hindi": "आत्मा न कभी जन्मती है, न मरती है।",
        "english": "The soul is never born, nor does it die; it is eternal."
    },
    {
        "keywords": ["angry", "anger", "krodh", "mad"],
        "chapter": 2, "verse:": 62,
        "sanskrit": "ध्यायतो विषयान्पुंसः सङ्गस्तेषूपजायते। सङ्गात्सञ्जायते कामः कामात्क्रोधोऽभिजायते॥",
        "hindi": "विषयों के विषय में चिन्तन करने से आसक्ति, फिर कामना, और फिर क्रोध उत्पन्न होता है।",
        "english": "From contemplation of sense objects arises attachment; from attachment arises desire; from desire arises anger."
    },
    {
        "keywords": ["god", "krishna", "bhagwan", "pray", "worship", "devotion"],
        "chapter": 9, "verse:": 22,
        "sanskrit": "अनन्याश्चिन्तयन्तो मां ये जनाः पर्युपासते।",
        "hindi": "जो मेरी अनन्य भक्ति करते हैं, उनका योगक्षेम मैं वहन करता हूँ।",
        "english": "To those who worship Me alone, thinking of no other, I secure what they lack and preserve what they have."
    }
]


# --- 3. THE APP LAYOUT ---

st.title("🙏 Geeta AI Wisdom")
st.write("Ask your life questions and find answers from the Bhagavad Gita Shlokas.")

# Input Box
user_question = st.text_input("Ask your question here (e.g., 'I am afraid', 'How to work?')", placeholder="Type your question...")

# Button
if st.button("Ask Geeta"):
    if user_question:
        found = False
        
        # Search Logic
        for item in geeta_data:
            # Check if any keyword matches the user's question
            for keyword in item["keywords"]:
                if keyword in user_question.lower():
                    # Display the Result Card
                    st.markdown(f"""
                    <div class="shloka-card">
                        <p style="color:#888; font-size:14px;">Chapter {item['chapter']}, Verse {item['verse']}</p>
                        <div class="sanskrit-text">{item['sanskrit']}</div>
                        <div class="translation-box">
                            <b>Hindi:</b> {item['hindi']}<br><br>
                            <b>English:</b> {item['english']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    found = True
                    break
            if found:
                break
        
        if not found:
            st.warning("I am still learning. Please ask about: Fear, Work, Anger, God, or Sadness.")
    else:
        st.error("Please enter a question first.")
        

