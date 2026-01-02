import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Badre Narayanan | Portfolio", page_icon="⚽", layout="wide")

# --- HELPER FUNCTION FOR ANIMATIONS ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Assets (Lottie Animations)
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_football = load_lottieurl("https://lottie.host/5aee9356-3d60-449e-b91c-7c01d957ba5c/F45s73X1f7.json")
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")

# --- CUSTOM CSS (Glassmorphism & Hover Effects) ---
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }
    
    /* Profile Image Styling */
    .profile-pic {
        border-radius: 50%;
        border: 4px solid #3b82f6;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
        display: block;
        margin-left: auto;
        margin-right: auto;
        transition: transform 0.3s ease;
    }
    .profile-pic:hover {
        transform: scale(1.05);
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }
    
    /* Text Styling */
    h1, h2, h3 {
        color: #60a5fa !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    p, li {
        color: #cbd5e1 !important;
        font-size: 16px;
    }
    
    /* Custom Button */
    .stButton>button {
        background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        height: 45px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/4140/4140048.png" class="profile-pic" width="140">', unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 style='text-align: center; color: white; margin: 0;'>Badre Narayanan</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>Data Scientist | Sports Analytics</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Skills", "Contact"],
        icons=["house", "rocket", "bar-chart-line", "envelope"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "icon": {"color": "#60a5fa", "font-size": "18px"},
            "nav-link": {"font-size": "15px", "color": "#cbd5e1", "margin": "5px"},
            "nav-link-selected": {"background-color": "#1e293b", "color": "#fff", "border-left": "4px solid #3b82f6"},
        }
    )
    
    st.write("---")
    st.markdown("### 🌐 Connect")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("GitHub", "https://github.com/Badrergb/", use_container_width=True)
    with col2:
        st.link_button("Email", "mailto:narayananbadre@gmail.com", use_container_width=True)

# --- HOME SECTION ---
if selected == "Home":
    col1, col2 = st.columns([1.5, 1], gap="medium")
    
    with col1:
        st.markdown("# 🚀 Data Science Meets Football")
        st.markdown("### Hi, I'm **Badre Narayanan**")
        st.markdown("""
        I don't just analyze data; I visualize the game. 
        
        I am an **Integrated MSc Data Science** student at **Amrita Vishwa Vidyapeetham** specializing in **Sports Analytics** and **AI**. 
        I build systems that help computers understand football tactics using Graph Theory and Reinforcement Learning.
        
        * 🧠 **Tactical AI Assistants**
        * 📊 **Performance Analytics**
        * ⚡ **Full-Stack Deployment**
        """)
        
        st.write("") # Spacer

        # Action Buttons
        c1, c2 = st.columns([1, 1])
        with c1:
            st.link_button("📂 View Projects", "https://github.com/Badrergb/", use_container_width=True)
        with c2:
            # Resume Download Logic
            try:
                with open("resume.pdf", "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.download_button(
                    label="📄 Download CV",
                    data=pdf_bytes,
                    file_name="Badre_Narayanan_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except FileNotFoundError:
                st.warning("⚠️ Resume not uploaded yet")

    with col2:
        # Lottie Animation
        if lottie_coding:
            st_lottie(lottie_coding, height=350, key="coding")

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("🏆 Featured Projects")
    st.markdown("Explore my work in Sports AI and Software Development.")
    st.write("")

    # Project 1
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
             st.image("https://cdn-icons-png.flaticon.com/512/2640/2640635.png", width=100)
        with col2:
            st.subheader("🌾 Farmer Management System")
            st.markdown("**Tech:** `Java` `PostgreSQL` `NetBeans`")
            st.write("A secure digital ledger for farmers to manage crop inventory and sales, designed to bridge the gap to market prices.")
            st.link_button("View Code", "https://github.com/Badrergb/Farmer-Management-System")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 2
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
             st.image("https://cdn-icons-png.flaticon.com/512/1165/1165187.png", width=100)
        with col2:
            st.subheader("🤖 RL Football Agent")
            st.markdown("**Tech:** `Python` `TensorFlow` `Reinforcement Learning`")
            st.write("Autonomous AI agent trained using Deep Q-Networks (DQN) to make optimal tactical decisions in simulated matches.")
            st.button("Demo Coming Soon", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
             st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
        with col2:
            st.subheader("🕸️ Pass Network Analysis")
            st.markdown("**Tech:** `NetworkX` `Matplotlib` `Graph Theory`")
            st.write("Visualizing team performance and player centrality using Graph Theory on match data to identify passing channels.")
            st.button("View Viz", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- SKILLS SECTION ---
elif selected == "Skills":
    st.title("⚡ Technical Arsenal")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("My Expertise")
        st.markdown("""
        I combine strong **Data Science foundations** with **Software Engineering** capabilities.
        
        * **Languages:** Python, Java, SQL
        * **AI/ML:** Scikit-Learn, TensorFlow, RL
        * **Data Viz:** Plotly, Seaborn, Tableau
        * **Web:** Streamlit, HTML/CSS
        """)
        if lottie_football:
            st_lottie(lottie_football, height=200)
        
    with col2:
        # INTERACTIVE RADAR CHART
        categories = ['Python/AI', 'Data Viz', 'SQL/DB', 'Graph Theory', 'Web Dev', 'Communication']
        values = [90, 85, 80, 75, 70, 85]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values, theta=categories, fill='toself', name='Badre Narayanan',
            line_color='#3b82f6', fillcolor='rgba(59, 130, 246, 0.4)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color='white')),
                bgcolor="rgba(0,0,0,0)"
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color='white'),
            showlegend=False,
            height=400,
            margin=dict(l=40, r=40, t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("📬 Get In Touch")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h4>Contact Details</h4>
            <p>📧 narayananbadre@gmail.com</p>
            <p>📱 +91 74188 06611</p>
            <p>📍 Coimbatore, India</p>
        </div>
        """, unsafe_allow_html=True)
        if lottie_contact:
            st_lottie(lottie_contact, height=200)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        contact_form = """
        <form action="https://formsubmit.co/narayananbadre@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #475569; background-color: #1e293b; color: white;">
            <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #475569; background-color: #1e293b; color: white;">
            <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 12px; margin-bottom: 10px; height: 150px; border-radius: 5px; border: 1px solid #475569; background-color: #1e293b; color: white;"></textarea>
            <button type="submit" style="background-color: #3b82f6; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
