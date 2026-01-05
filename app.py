import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Badre.RG | Portfolio", page_icon="🍊", layout="wide")

# --- HELPER: LOAD IMAGE AS BASE64 ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# --- HELPER: LOAD LOTTIE ANIMATIONS ---
@st.cache_data
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Load Assets
lottie_analytics = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")

# --- LOAD PROFILE PICTURE ---
# IMPORTANT: This looks for a file exactly named 'profile.png' in your GitHub folder
img_path = "profile.png" 
img_base64 = get_base64_image(img_path)

if img_base64:
    profile_img_src = f"data:image/png;base64,{img_base64}"
else:
    # Fallback image if your photo is missing
    profile_img_src = "https://cdn-icons-png.flaticon.com/512/4140/4140048.png"

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* 1. GLOBAL RESET */
    .stApp {
        background-color: #0c0c0c;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* 2. HIDE DEFAULTS */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* 3. BENTO CARD */
    .bento-card {
        background-color: #161616;
        border: 1px solid #2a2a2a;
        border-radius: 24px;
        padding: 30px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s, border-color 0.2s;
    }
    .bento-card:hover {
        transform: scale(1.01);
        border-color: #f97316;
    }
    
    /* 4. TYPOGRAPHY & BUTTONS */
    h1 { color: white; font-weight: 800; font-size: 3rem; margin: 0; line-height: 1.1; }
    h2 { color: white; font-weight: 700; margin-top: 40px; margin-bottom: 20px; }
    h3 { color: white; font-weight: 600; margin-top: 0; font-size: 1.3rem; }
    p, li { color: #9ca3af; font-size: 15px; line-height: 1.6; }
    strong { color: #e5e7eb; }
    
    .skill-badge {
        background: #262626; color: #d4d4d4; padding: 6px 14px; 
        border-radius: 20px; font-size: 12px; margin-right: 5px; 
        display: inline-block; font-weight: 500; border: 1px solid #333;
    }
    
    .stButton>button {
        background-color: #f97316; color: white; border-radius: 30px; 
        border: none; padding: 12px 25px; font-weight: bold; width: 100%; 
        transition: background 0.2s;
    }
    .stButton>button:hover { background-color: #ea580c; }
    
    a { color: #f97316; text-decoration: none; }
    a:hover { text-decoration: underline; }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
c1, c2 = st.columns([2, 1], gap="medium")

with c1:
    st.markdown("""
    <div class="bento-card">
        <div>
            <p style="color: #f97316; font-weight: bold; letter-spacing: 1px; font-size: 12px;">DATA SCIENTIST & SPORTS ANALYST</p>
            <h1>Badre Narayanan RG</h1>
            <p style="margin-top: 20px; font-size: 18px; color: #d1d5db;">
                I don't just write code; I decode the game. <br>
                Merging <strong>Computational Intelligence</strong> with <strong>Football Analytics</strong>.
            </p>
        </div>
        <div style="margin-top: 30px; display: flex; gap: 15px;">
            <a href="https://github.com/Badrergb/" target="_blank" style="background: #262626; color: white; padding: 12px 24px; border-radius: 30px; text-decoration: none; border: 1px solid #333;">GitHub Profile</a>
            <a href="mailto:narayananbadre@gmail.com" style="background: #262626; color: white; padding: 12px 24px; border-radius: 30px; text-decoration: none; border: 1px solid #333;">Email Me</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    # This uses your photo if found, otherwise uses the cartoon
    st.markdown(f"""
    <div class="bento-card" style="align-items: center; text-align: center; background: #111;">
        <img src="{profile_img_src}" style="width: 130px; height: 130px; border-radius: 50%; border: 4px solid #f97316; margin-bottom: 20px; object-fit: cover;">
        <h3>Open to Work</h3>
        <p style="font-size: 14px;">Coimbatore, India 📍</p>
        <div style="margin-top: 15px;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">AI/ML</span>
            <span class="skill-badge">Sports Viz</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("") 

# --- EXPERIENCE & ACHIEVEMENTS (FIXED HTML) ---
# I removed the indentation inside the HTML string to fix the "Raw Code" error
col_exp, col_ach = st.columns([1.6, 1], gap="medium")

with col_exp:
    st.markdown("""
<div class="bento-card">
    <h3 style="margin-bottom: 20px;">💼 Experience & Education</h3>
    <div style="margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <strong style="color: #f97316; font-size: 16px;">Integrated MSc Data Science</strong>
            <span style="background: #262626; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #888;">2022 - Present</span>
        </div>
        <p style="margin: 5px 0 0 0; color: #e5e7eb;">Amrita Vishwa Vidyapeetham</p>
        <p style="font-size: 13px; margin-top: 5px;">Specializing in Statistical Modeling, Machine Learning, and Database Management. CGPA: 8.0+</p>
    </div>
    <hr style="border: 0; border-top: 1px solid #333; margin: 15px 0;">
    <div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
             <strong style="color: #f97316; font-size: 16px;">Freelance Developer</strong>
             <span style="background: #262626; padding: 4px 10px; border-radius: 10px; font-size: 11px; color: #888;">2024 - Present</span>
        </div>
        <p style="margin: 5px 0 0 0; color: #e5e7eb;">Sports Analytics & Automation</p>
        <p style="font-size: 13px; margin-top: 5px;">Building automated pass network tools and tactical analysis bots using Python and Graph Theory.</p>
    </div>
</div>
    """, unsafe_allow_html=True)

with col_ach:
    st.markdown("""
<div class="bento-card">
    <h3 style="margin-bottom: 20px;">🏆 Achievements</h3>
    <ul style="padding-left: 20px; margin: 0; color: #9ca3af;">
        <li style="margin-bottom: 10px;"><strong>IBM Certified:</strong> Data Analysis with Python</li>
        <li style="margin-bottom: 10px;"><strong>Deep Learning:</strong> Specialization (Coursera - In Progress)</li>
        <li style="margin-bottom: 10px;"><strong>Project Lead:</strong> Farmer Management System (Full Stack)</li>
    </ul>
    <div style="margin-top: auto; padding-top: 20px;"></div>
""", unsafe_allow_html=True)
    
    # Resume Button Logic
    try:
        with open("resume.pdf", "rb") as f:
            st.download_button("📄 Download Full Resume", f, "Badre_Narayanan_CV.pdf", "application/pdf")
    except:
        st.button("⚠️ Resume Upload Pending", disabled=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# --- FEATURED PROJECTS ---
st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)
p1, p2, p3 = st.columns([1, 1, 1], gap="medium")

with p1:
    st.markdown("""
    <div class="bento-card">
        <div style="font-size: 30px; margin-bottom: 10px;">🌾</div>
        <h3 style="font-size: 18px;">Farmer Management</h3>
        <p style="font-size: 12px; color: #f97316; font-weight: bold; margin-bottom: 10px;">JAVA • POSTGRESQL • JSP</p>
        <p style="font-size: 14px;">Secure digital ledger for crop inventory, sales tracking, and market price integration.</p>
        <div style="margin-top: auto;">
            <a href="https://github.com/Badrergb/Farmer-Management-System" target="_blank" style="font-size: 14px; font-weight: bold;">View Source ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="bento-card">
        <div style="font-size: 30px; margin-bottom: 10px;">⚽</div>
        <h3 style="font-size: 18px;">RL Football Agent</h3>
        <p style="font-size: 12px; color: #f97316; font-weight: bold; margin-bottom: 10px;">PYTHON • TENSORFLOW • RL</p>
        <p style="font-size: 14px;">Autonomous AI agent trained with Deep Q-Networks (DQN) to make tactical decisions.</p>
        <div style="margin-top: auto;">
            <span style="font-size: 14px; color: #666;">Code Coming Soon</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="bento-card">
        <div style="font-size: 30px; margin-bottom: 10px;">🕸️</div>
        <h3 style="font-size: 18px;">Pass Network Viz</h3>
        <p style="font-size: 12px; color: #f97316; font-weight: bold; margin-bottom: 10px;">GRAPH THEORY • NETWORKX</p>
        <p style="font-size: 14px;">Visualizing player centrality and passing channels using match data.</p>
        <div style="margin-top: auto;">
             <span style="font-size: 14px; color: #666;">View Analysis</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# --- SKILLS ANALYTICS ---
f1, f2 = st.columns([2, 1], gap="medium")

with f1:
    st.markdown("<h3>Technical Arsenal</h3>", unsafe_allow_html=True)
    fig = go.Figure(go.Bar(
        x=['Python', 'SQL', 'Data Viz', 'Java', 'RL', 'Communication'],
        y=[95, 80, 85, 75, 85, 90],
        marker=dict(color='#f97316', line=dict(color='#f97316', width=1)),
        opacity=0.9
    ))
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family="Helvetica Neue"),
        height=220,
        margin=dict(t=20, b=20, l=20, r=20),
        yaxis=dict(showgrid=False, visible=False),
        xaxis=dict(showgrid=False, tickfont=dict(size=12))
    )
    st.plotly_chart(fig, use_container_width=True)

with f2:
    # CRASH FIX: Checking if lottie_analytics exists before displaying
    if lottie_analytics:
        st_lottie(lottie_analytics, height=220)
    else:
        st.markdown("<br><br><h3 style='text-align:center;'>📊 Data Viz</h3>", unsafe_allow_html=True)
