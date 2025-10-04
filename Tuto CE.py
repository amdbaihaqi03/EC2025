import streamlit as st

# ----- PAGE SETUP -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ----- HEADER SECTION -----
col1, col2 = st.columns([0.5, 1.5])

with col1:
    st.image("https://github.com/user-attachments/assets/2c5db5d3-26d2-4695-bdd7-b8323db49fff", caption="Ahmad Baihaqi", use_container_width=True)  # Replace with your image path or URL

with col2:
    st.markdown("<h1 style='font-size: 34px; margin-bottom: 4px;'>Ahmad Baihaqi Bin Ruzlan</h1>", unsafe_allow_html=True)
    st.write("📍 Location: Kelantan, Malaysia")
    st.write("✉️ Email: azbaihaqi03@gmail.com")
    st.write("📞 Phone: +60143593135")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)")

st.markdown("---")

# ----- EDUCATION SECTION -----
st.header("🎓 Education")
st.write("**Bachelor of Information Technology with Honours**, University Malaysia Kelantan (2022 – 2026)")
st.write("- Major in Artificial Intelligence")

st.markdown("---")

# ----- WORK EXPERIENCE SECTION -----
st.header("💼 Work Experience")
st.write("**Software Intern**, Tech Company (Jun 2023 – Aug 2023)")
st.write("- Developed internal dashboard using Python and Streamlit")
st.write("- Automated data processing tasks, reducing manual work by 40%")
st.write("- Collaborated with the data team to deploy ML models")

st.write("**Freelance Web Developer** (2022 – Present)")
st.write("- Built personal and business websites using HTML, CSS, and JavaScript")
st.write("- Customized WordPress themes and improved SEO performance")

st.markdown("---")

# ----- SKILLS SECTION -----
st.header("🧠 Skills")
skills_col1, skills_col2 = st.columns(2)

with skills_col1:
    st.write("- Python")
    st.write("- IoT Systems")
    st.write("- SQL")
    
st.markdown("---")

# ----- PROJECTS SECTION -----
st.header("🚀 Projects & Achievements")
st.write("**Water Leakage Detection IoT System**")
st.write("- Designed an IoT-based system using ESP8266 to detect water leakage in real time")
st.write("- Integrated with a mobile app for instant notifications")

st.write("**Weather Monitoring System**")
st.write("- Developed a real-time weather monitoring device using sensors to measure temperature, humidity, and rainfall")
st.write("- Displayed collected data on Blynk dashboard to monitor the system")

st.markdown("---")

# ----- FOOTER -----
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 0.9em;'>
        © 2025 Baihaqi Ruzlan | Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
