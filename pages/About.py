import streamlit as st
from PIL import Image
from pathlib import Path
import requests


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"
reseme_file = current_dir / "assets" / "Resume.pdf"

page_title = "Digital CV | Youssef Ahmed"
page_icon = ":wave:"
name = "Youssef Ahmed"
discription = """
Fresh Data Analyst | Faculty of Computer Science and AI
"""
email = "yaa2003ya@gmailcom"
social_media = {"LinkedIn": "https://www.linkedin.com/in/youssef-ahmed-9a5643244","GitHub": "https://github.com/youssefa7med","Facebook": "https://www.facebook.com/profile.php?id=100049906008785&mibextid=ZbWKwL","WhatsApp": "https://api.whatsapp.com/send?phone=201000139417&text=%F0%9F%93%9E"}
projects = {
    "🏆 Streamlit Fifa - Fifa 23 Analysis.":"https://fifa23-analysis.streamlit.app/",
    "🎮 Fifa 23 Analysis - FIFA 23 analysis: Player ,Clubs and Nationalities Analysis.":"https://github.com/youssefa7med/Fifa23.git",
    "🏃🏼 Streamlit Ecommerce - Streamlit for Ecommerce Analysis.":"https://ecommerce-home.streamlit.app/",
    "👨🏻‍💻 Streamlit Jobs - Streamlit for Jobs Analysis.":"https://jobindata.streamlit.app/",
    "🛍️ Ecommerce Analysis - Analyzing online data to improve digital retail performance.":"https://github.com/youssefa7med/Ecommerce.git",
    "👔 Jobs in data Analysis - Analyzing four years of data to understand trends and inform compensation decisions in the field.":"https://github.com/youssefa7med/jobs_in_data.git",
    "♻ Wuzzuf web scraping - Extracting data on data science jobs for insights on salaries and trends.":"https://github.com/youssefa7med/Web_Scrapping/tree/d4d7e019e509dc7bafbe91c073bccf4f0cceb8ae/Wuzzuf",
    "📦 Ebay iPhone scrapping - Extracting insights from listings and trends for informed purchasing decisions.":"https://github.com/youssefa7med/Web_Scrapping/tree/d4d7e019e509dc7bafbe91c073bccf4f0cceb8ae/Ebay",
    "🧑‍🏫 MIT courses scrapping - Overviewing educational offerings at MIT for academic and professional development.":"https://github.com/youssefa7med/Web_Scrapping/tree/d4d7e019e509dc7bafbe91c073bccf4f0cceb8ae/Mit_Courses",
    "⚽ Yalla Kora scrapping - Dissecting soccer matches for insights.":"https://github.com/youssefa7med/Web_Scrapping/tree/d4d7e019e509dc7bafbe91c073bccf4f0cceb8ae/Yalla_Kora",
    "📚 Diwan book scraping - Extracting digital data for analysis or collection purposes.":"https://github.com/youssefa7med/Web_Scrapping/tree/d4d7e019e509dc7bafbe91c073bccf4f0cceb8ae/Diwan_Books",
    "🚢 Titanic Supervised predection - Predicting survival on the Titanic.":"https://github.com/youssefa7med/Titanic-survived-prediction",
    "😵̷̊̊̊̊̊ Hangman Game - Guessing the word.":"https://github.com/youssefa7med/Hangman_Game",
    "✂️ Rock Paper Scissors - A game between you and the computer.":"https://github.com/youssefa7med/Rock_Paper_Game",
    "📖 Library System - A library management system.":"https://github.com/youssefa7med/Liberary-system",
    "🏦 Bank System - A bank management system.":"https://github.com/youssefa7med/Bank-system"
}

st.set_page_config(page_title=page_title, page_icon=page_icon)
# --- load CSS, resume and profile picture ---
with open (css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(reseme_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)



col2,col1 = st.columns(2,gap = "small")
with col1:
    st.image(profile_pic,width = 230)
with col2:
    st.title(name)
    st.write(discription)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=r"\assets\Resume.pdf",
        mime='application/octet-stream'
    )
    st.write("📫",email)



st.write("#")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")



st.write("#")
st.subheader("Experience & Qualifications")
st.divider()
st.write("""
    - ✔️ Fresh Data Analyst | Faculty of Computer Science and AI.
    - ✔️ Intermediate Python certificates from the Egyptian Ministry of Communications.
    - ✔️ Excellent team-player and display strong sense of initiative on tasks.
""")


st.write("#")
st.subheader("Hard Skills")
st.divider()
st.write("""
- 👨‍💻 Programming : Python (Numpy, Pandas, Scikit-learn) SQL
- 📊 Data Visualization : Plotly, Matplotlib, Seaborn
- 🕸️ Web Scrapping : Beautiful Soup
- 📚 Machine Learning : Scikit-learn
- 🗄️ Databases : MySQL
- 🌐 Web Development : Streamlit
""")

st.write("#")
st.subheader("Work History")
st.write("""---""")

# -------job 1-------
st.write("🚧", "Python Instractor | Emetdad Courses")
st.write("01/2024 - Present")
st.write("""
    - 🔷 Help students to understand important concepts of programming.
    - 🔷 Teach and guide students through Python coding.
    - 🔷 Develop students skills through coding.
    - 🔷 Help students to understand coding.

""")

st.write("#")
st.subheader("Projects & Accomplishments")
st.write('---')

for project, link in projects.items():
    st.write(f"[{project}]({link})")