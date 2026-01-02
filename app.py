import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Badre Narayanan RG | Portfolio",
    page_icon="💼",
    layout="wide",
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* 1. BACKGROUND & TEXT */
    .stApp {
        background-color: #0e1117;
    }
    h1, h2, h3 {
        color: #58a6ff; /* Professional Blue */
        font-family: 'Helvetica', sans-serif;
    }
    p, div {
        color: #e6e6e6;
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
        border: 3px solid #30363d; /* Subtle dark border */
        width: 140px;
        height: 140px;
        object-fit: cover;
    }

    /* 4. BUTTONS */
    .stButton>button {
        background-color: #1f6feb; /* Corporate Blue */
        color: white;
        border-radius: 6px;
        border: none;
        height: 3em;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    .stButton>button:hover {
        background-color: #388bfd;
    }
    
    /* 5. CONTACT CARD */
    .contact-info {
        background-color: #161b22;
        padding: 15px;
        border-radius: 6px;
        border: 1px solid #30363d;
        margin-top: 10px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/4140/4140048.png" class="profile-pic">', unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 style='text-align: center; color: white; margin-bottom: 0;'>Badre Narayanan</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e; font-size: 14px;'>Data Scientist | Sports Analytics</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Professional Menu (No emojis in titles)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Skills", "Contact"],
        icons=["house", "briefcase", "tools", "envelope"], # Standard Bootstrap Icons
        default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "icon": {"color": "#8b949e", "font-size": "18px"},
            "nav-link": {"font-size": "15px", "color": "#c9d1d9", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": #21262d, "color": "white", "border-left": "3px solid #58a6ff"},
        }
    )
    
    st.write("---")
    
    # Clean Links
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("GitHub", "https://github.com/Badrergb/", use_container_width=True)
    with col2:
        st.link_button("Email", "mailto:narayananbadre@gmail.com", use_container_width=True)

# --- HOME SECTION ---
if selected == "Home":
    st.title("Badre Narayanan RG")
    st.subheader("Data Scientist & Full Stack Developer")
    
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        I am an **Integrated MSc Data Science** student at **Amrita Vishwa Vidyapeetham**.
        
        I specialize in the intersection of **Sports Analytics** and **Artificial Intelligence**. 
        My work focuses on building intelligent systems that analyze football tactics using advanced computational methods.
        
        **Core Competencies:**
        * Reinforcement Learning
        * Graph Theory & Network Analysis
        * Full-Stack Application Development
        """)
        
        # Resume Download Placeholder
        # with open("resume.pdf", "rb") as pdf_file:
        #    st.download_button("Download Resume", data=pdf_file.read(), file_name="Badre_Resume.pdf")

    with col2:
        st.markdown("""
        <div style="background-color: #161b22; padding: 20px; border: 1px solid #30363d; border-radius: 6px;">
            <strong style="color: white;">Current Focus</strong>
            <ul style="color: #8b949e; padding-left: 20px; margin-top: 10px;">
                <li>Tactical AI Assistants</li>
                <li>Performance Analysis</li>
                <li>Real-time Decision Systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("Projects")
    st.write("A selection of technical projects demonstrating data science and development capabilities.")
    st.markdown("---")

    # Project 1
    with st.container():
        st.subheader("Farmer Management System")
        st.caption("Java | PostgreSQL | NetBeans")
        st.write("""
        Developed a secure digital ledger system for agricultural inventory management. 
        Facilitates direct sales to markets and includes robust user authentication.
        """)
        st.link_button("View Source Code", "https://github.com/Badrergb/Farmer-Management-System")
    
    st.markdown("---")

    # Project 2
    with st.container():
        st.subheader("RL Football Agent")
        st.caption("Python | TensorFlow | Reinforcement Learning")
        st.write("""
        Designed an autonomous agent using Deep Q-Networks (DQN) to simulate and optimize tactical decision-making in football.
        Focuses on reward system optimization and state-space exploration.
        """)
        st.button("Code Coming Soon", disabled=True)
    
    st.markdown("---")

    # Project 3
    with st.container():
        st.subheader("Pass Network Analysis")
        st.caption("Python | NetworkX | Graph Theory")
        st.write("""
        Applied Graph Theory centrality metrics to match data to visualize player connectivity and team performance structure.
        """)
        st.button("View Visualization", disabled=True)

# --- SKILLS SECTION ---
elif selected == "Skills":
    st.title("Technical Proficiency")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("Data Science & AI")
        st.write("**Python (Pandas, NumPy)**")
        st.progress(90)
        st.write("**Machine Learning & RL**")
        st.progress(85)
        st.write("**Data Visualization**")
        st.progress(80)

    with col2:
        st.subheader("Development")
        st.write("**Java Development**")
        st.progress(80)
        st.write("**SQL & Databases**")
        st.progress(75)
        st.write("**Web Technologies**")
        st.progress(70)

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("Contact Information")
    st.write("Available for collaborations in Sports Analytics and AI research.")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.subheader("Send a Message")
        contact_form = """
        <form action="https://formsubmit.co/narayananbadre@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 4px; border: 1px solid #30363d; background-color: #0d1117; color: white;">
            <input type="email" name="email" placeholder="Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 4px; border: 1px solid #30363d; background-color: #0d1117; color: white;">
            <textarea name="message" placeholder="Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; height: 150px; border-radius: 4px; border: 1px solid #30363d; background-color: #0d1117; color: white;"></textarea>
            <button type="submit" style="background-color: #1f6feb; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Details")
        st.markdown("""
        <div class="contact-info">
            <div style="margin-bottom: 10px;"><strong>Email:</strong> narayananbadre@gmail.com</div>
            <div style="margin-bottom: 10px;"><strong>Phone:</strong> +91 74188 06611</div>
            <div><strong>Location:</strong> Coimbatore, India</div>
        </div>
        """, unsafe_allow_html=True)
