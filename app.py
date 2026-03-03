import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="Geeta AI Wisdom (Free)", page_icon="🙏")

st.title("🙏 Geeta AI Problem Solver")
st.write("Apni samasya batayein, AI Geeta ke Shlokon se samadhan dega.")

# Sidebar for API Key
api_key = st.sidebar.text_input("Apni Groq API Key daalein (Free)", type="password")

user_problem = st.text_area("Aapki samasya kya hai?", height=100)

if st.button("Solution Payein"):
    if not api_key:
        st.warning("Pehle sidebar mein apni Groq API Key daalein.")
    elif not user_problem:
        st.warning("Kripya apni samasya likhein.")
    else:
        try:
            # Groq Client (Free API)
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )

            # AI Instruction
            system_instruction = (
                "You are a spiritual guide and expert in Bhagavad Geeta. "
                "When a user shares a problem, you must provide a solution based on a relevant Geeta Shloka. "
                "First, give the Sanskrit Shloka. Then, give the Hindi translation. "
                "Finally, explain how to apply this to the user's problem in simple Hindi. "
                "Be empathetic and respectful."
            )

            # Loading animation
            with st.spinner("Geeta ke anusaar soch raha hoon..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", # YE MODEL UPDATED HAI
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": user_problem}
                    ]
                )

                # Answer
                answer = response.choices[0].message.content

                st.success("Yeh hai aapka margdarshan:")
                st.markdown(answer)

        except Exception as e:
            st.error(f"Error: {e}")

            st.info("API Key sahi hai? Groq console se check karein.")
