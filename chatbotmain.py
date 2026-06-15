
import streamlit as st


st.set_page_config(
    page_title = "Health Assistant",
    page_icon = "🩺",
    layout = "wide"
)
st.title("Smart Health Advisor")
st.caption("Ask questions, understand symptoms,live healthier")
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

.stTextInput input {
    border-radius: 12px;
}

.big-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #dbeafe 0%,
        #ecfeff 50%,
        #f0fdf4 100%
    );
}
</style>
""", unsafe_allow_html=True)
st.markdown("### Try asking:")
st.markdown("""
- I have a fever and cough
- How can I improve my sleep?
- Suggest a healthy diet plan
- What causes headaches?
""")
col1, col2, col3 = st.columns(3)

col1.metric("💧 Water Goal", "2L/day")
col2.metric("🚶 Steps Goal", "10,000")
col3.metric("😴 Sleep Goal", "8 hrs")
col1, col2, col3 = st.columns(3)

col1.metric("💧 Water Goal", "2L/day")
col2.metric("🚶 Steps Goal", "10,000")
col3.metric("😴 Sleep Goal", "8 hrs")

st.markdown("""
<div class='big-card'>
<h3>👋 Welcome!</h3>
<p>Describe your symptoms, ask health questions, or get wellness advice.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("🤒 Fever")
with col2:
    st.button("🤕 Headache")
with col3:
    st.button("🥗 Diet")
with col4:
    st.button("🏃 Fitness")
with st.sidebar:
    st.title("⚙️ Menu")
    st.info("AI-powered health guidance")
    st.markdown("---")
    st.markdown("### Features")
    st.write("✅ Symptom Analysis")
    st.write("✅ Health Tips")
    st.write("✅ Wellness Guidance")
question = st.text_input("Ask freely , Care wisely")
def health(question):
    response = ollama.chat(
        model = 'llama3.2:1b ',
        messages = [
            {
                'role' : 'system',
                'content' : """You are a health assistant.
                rules :
                - always be respectful
                - Be polite and friendly
                - keep answers short and to the point  """
               
            },
            {
                'role' : 'user',
                'content' : question
            }
        ]
    ) 
    return response['message']['content']

if st.button("Send"):
          st.write(health(question))
          