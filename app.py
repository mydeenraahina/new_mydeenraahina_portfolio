import streamlit as st
import time

st.set_page_config(page_title="Mydeen Raahina Portfolio", layout="wide")

# Custom CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700&display=swap');

body, .stApp {
    background-color: #f4f6f9;
    font-family: 'Inter', sans-serif;
    color: #212529;
    padding: 0;
    margin: 0;
}

.heading {
    font-size: 32px;
    font-weight: 700;
    color: #004080;
    margin-top: 30px;
    margin-bottom: 8px;
    animation: fadeInDown 1s ease-in-out;
    text-align: left;
    padding-left: 20px;
}

.subheading {
    font-size: 22px;
    font-weight: 600;
    color: #004080;
    margin-bottom: 5px;
    animation: fadeInDown 1s ease-in-out;
    text-align: left;
    padding-left: 20px;
}

.paragraph {
    font-size: 16px;
    font-weight: 400;
    color: #004080;
    margin-top: 10px;
    margin-bottom: 20px;
    animation: fadeIn 1s ease-in-out;
    text-align: left;
    padding-left: 20px;
    line-height: 1.5;
}

.section {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #dee2e6;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    animation: fadeIn 1s ease-in-out;
    margin-bottom: 25px;
}

.stExpander > summary {
    font-size: 20px;
    font-weight: 600;
    color: #004080;
    transition: color 0.3s ease;
    padding: 10px 20px;
}

.stExpander > summary:hover {
    color: #0077cc;
    cursor: pointer;
}

.stExpander > div {
    overflow-y: auto;
    padding: 10px 20px;
    background-color: #f4f6f9;
    border-radius: 10px;
    font-size: 16px;
    line-height: 1.5;
    word-wrap: break-word;
    display: block;
    text-align: left;
}

.stExpander {
    width: 100%;
    max-width: 100%;
    background-color: #ffffff;
    border-radius: 8px;
    border: 1px solid #ced4da;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    overflow: hidden;
    /* Removed fixed height */
}

.stExpander > div p {
    font-size: 14px;
    word-wrap: break-word;
}

a {
    color: #004080;
    text-decoration: none;
    font-weight: 600;
}

a:hover {
    text-decoration: underline;
    color: #0077cc;
}

.stButton > button {
    background-color: #004080;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    border: none;
    padding: 10px 24px;
    transition: background-color 0.3s ease;
}

.stButton > button:hover {
    background-color: #002b5c;
}

.stTextInput input, .stTextArea textarea {
    background-color: #f1f3f5;
    border-radius: 8px;
    border: 1px solid #ced4da;
    padding: 10px;
    font-size: 16px;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #004080;
    outline: none;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes fadeInDown {
    from {opacity: 0; transform: translateY(-30px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="heading">Hi! I\'m MydeenRaahina 👋</div>', unsafe_allow_html=True)
    time.sleep(1.2)

    st.markdown('<div class="paragraph">🚀 AI & ML Engineering</div>', unsafe_allow_html=True)
  

    st.markdown('<div class="paragraph">⚡ Prompt Engineering</div>', unsafe_allow_html=True)


    st.markdown('<div class="paragraph">💡 Data Engineering</div>', unsafe_allow_html=True)
  

    st.markdown('<div class="paragraph">💻 Python Full Stack Development</div>', unsafe_allow_html=True)
  

    st.markdown('<div class="paragraph">🎯 Data-driven, AI-focused, and design-conscious — I build intelligent apps that solve real-world problems using machine learning, prompt engineering, and beautiful code.</div>', unsafe_allow_html=True)

with col2:
    st.image('image.png', width=400)

# Content section
col1, col2 = st.columns(2)

with col1:
    with st.expander("📖 Know More About Me"):
        st.markdown("""<div class="section">
        🎓 Gold Medalist in Computer Science with a strong foundation in AI/ML Engineering.<br>
        💼 One year of experience in AI/ML Engineering, Prompt Engineering, and Data Engineering. Skilled in building data workflows and integrating real-time AI models.<br>
        📊 Experienced in Data Analytics using Python, and proficient in full-stack development, enabling me to build end-to-end intelligent applications.<br>
        🔗 Connect with me on LinkedIn or check my code on GitHub.
        </div>""", unsafe_allow_html=True)

    with st.expander("📬 Contact Me"):
        st.markdown('<div class="section">Want to collaborate or say hi? Drop your details below 👇</div>', unsafe_allow_html=True)
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message")

            submitted = st.form_submit_button("Send")
            if submitted:
                st.success("✅ Thanks! I’ll get back to you ASAP.")

with col2:
    with st.expander("🧠 Experience"):
        st.markdown("""<div class="section">
            <strong>📍 Data Scientist Intern — Plattr Tech Studio (Sep 2024 - Dec 2024)</strong><br>
            • OCR + ML classification for Tamil/English ads (Ad Classification Project).<br>
            • Vision-based motion detection AI game inspired by Talking Tom (Visionary Project).<br><br>
            <strong>📍 AI/ML Engineer — Plattr Tech Studio (Dec 2024 - Present)</strong><br>
            • Built prompt pipelines for Tax Fixxer to auto-suggest tax-saving strategies using OpenAI & LLaMA.<br>
            • Led scraping and backend data ingestion for Wim Card using Playwright.<br>
            • Managed end-to-end AI/ML pipelines, improving model accuracy and performance.<br>
            • Developed AI-based data solutions using Python and integrated multiple machine learning algorithms.<br>""", unsafe_allow_html=True)

    with st.expander("🌐 Find Me Online"):
        st.markdown("""<div class="section">
            🔗 <a href="https://www.linkedin.com/in/mydeenraahina" target="_blank">LinkedIn</a> – Connect professionally<br>
            🧠 <a href="https://github.com/mydeenraahina" target="_blank">GitHub</a>    – View my projects and code<br>
            ✍️ <a href="https://medium.com/@raahinamydeen" target="_blank">Medium</a> -Read my blogs on Data & AI
        </div>""", unsafe_allow_html=True)

