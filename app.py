import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Badre's Portfolio",
    page_icon="⚡",
    layout="wide",
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* 1. BACKGROUND & TEXT */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #161b22 100%);
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    
    /* 2. SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid #30363d;
    }
    
    /* 3. PROFILE PICTURE */
    .profile-pic {
        display: block;
        margin: auto;
        border-radius: 50%;
        border: 4px solid #58a6ff;
        box-shadow: 0 4px 12px rgba(88, 166, 255, 0.4);
        width: 140px;
        height: 140px;
        object-fit: cover;
    }

    /* 4. CUSTOM BUTTONS */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 8px;
        border: none;
        height: 3em;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #2ea043;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/4140/4140048.png" class="profile-pic">', unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 style='text-align: center; color: white;'>Badre Narayanan</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: #8b949e;'>⚽ Sports Analytics | 🤖 AI</div>", unsafe_allow_html=True)
    
    st.write("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Skills", "Contact"],
        icons=["house-heart", "rocket-takeoff", "cpu", "envelope-paper-heart"], # FANCY ICONS
        default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "icon": {"color": "#58a6ff", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "color": "#c9d1d9"},
            "nav-link-selected": {"background-color": "#1f6feb"},
        }
    )
    
    st.markdown("---")
    
    # Social Buttons with Emojis
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🐱 GitHub", "https://github.com/Badrergb/", use_container_width=True)
    with col2:
        st.link_button("📧 Email", "mailto:narayananbadre@gmail.com", use_container_width=True)

# --- HOME SECTION ---
if selected == "Home":
    st.markdown("## Hi, I'm Badre! 👋")
    st.markdown("### *I teach computers to watch Football.* ⚽📺")
    
    st.divider()

    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.write("""
        I am an **Integrated MSc Data Science** student at **Amrita Vishwa Vidyapeetham**. 🎓
        
        Most data scientists look at numbers. **I look at the game.** I specialize in building AI systems that understand:
        
        * 🧠 **Tactics** (using Reinforcement Learning)
        * 🕸️ **Passing Networks** (using Graph Theory)
        * ⚡ **Real-time Decisions** (using Automation)
        """)
        
        # Resume Button (Commented out until you upload the file)
        # with open("resume.pdf", "rb") as pdf_file:
        #    st.download_button("📄 Download Resume", data=pdf_file.read(), file_name="Badre_Resume.pdf")

    with col2:
        st.info("💡 **My Goal:** To bridge the gap between abstract Math and the beautiful game of Football.")
        st.success("🏗️ **Currently building:** A tactical AI assistant for coaches.")

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("My Creations 🛠️")
    st.write("Check out my top projects below.")
    st.write("")

    # Project 1: Farmer
    with st.container():
        st.subheader("🌾 Farmer Management System")
        st.caption("📅 Sept 2025 | ☕ Java & SQL")
        st.write("A digital ledger to help farmers manage crops and sell directly to markets.")
        st.markdown("**Tech:** `Java` `PostgreSQL` `NetBeans`")
        st.link_button("🔗 View Code on GitHub", "https://github.com/Badrergb/Farmer-Management-System")
    
    st.divider()

    # Project 2: Football AI
    with st.container():
        st.subheader("🥅 RL Football Agent")
        st.caption("📅 Dec 2025 | 🐍 Python & AI")
        st.write("An autonomous AI agent trained to play football tactically using **Reinforcement Learning (DQN)**.")
        st.markdown("**Tech:** `TensorFlow` `Gym` `Python`")
        st.button("🚧 Demo Coming Soon", disabled=True) # Disabled button for coming soon
    
    st.divider()

    # Project 3: Pass Networks
    with st.container():
        st.subheader("🕸️ Pass Network Analysis")
        st.caption("📅 Nov 2025 | 📊 Graph Theory")
        st.write("Visualizing how players connect on the field using Centrality Metrics and Graph Theory.")
        st.markdown("**Tech:** `NetworkX` `Matplotlib` `Pandas`")
        st.button("🚧 View Visualization", disabled=True)

# --- SKILLS SECTION ---
elif selected == "Skills":
    st.title("What I Bring to the Table ⚡")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧠 The Brain (AI & Data)")
        st.write("`🐍 Python` `🐼 Pandas` `🔢 NumPy`")
        st.progress(90)
        st.write("`🤖 Scikit-Learn` `🥅 Reinforcement Learning`")
        st.progress(80)

    with col2:
        st.markdown("### 🏗️ The Build (Dev & Web)")
        st.write("`☕ Java` `🗄️ SQL (PostgreSQL)`")
        st.progress(85)
        st.write("`🌐 Streamlit` `☁️ GitHub Actions`")
        st.progress(70)

    st.info("🌟 **Superpower:** I can explain complex Graph Theory using Football analogies!")

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("Let's Chat! 📬")
    
    st.write("Got a project? Love Football? Just want to say hi? Drop a message!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        contact_form = """
        <form action="https://formsubmit.co/narayananbadre@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="👤 Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
            <input type="email" name="email" placeholder="📧 Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
            <textarea name="message" placeholder="💬 Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; height: 150px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
            <button type="submit" style="background-color: #238636; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%;">🚀 Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📍 Find Me Here")
        st.markdown("🇮🇳 **Coimbatore, India**")
        st.markdown("📧 **narayananbadre@gmail.com**")
        st.markdown("📱 **+91 74188 06611**")
        st.link_button("🤝 Connect on LinkedIn", "#")
