import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Badre Narayanan RG | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* 1. BACKGROUND GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #161b22 100%);
    }

    /* 2. SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid #30363d;
    }
    
    /* 3. PROFILE PICTURE STYLING */
    .profile-pic {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        border: 3px solid #0077b6;
        box-shadow: 0 4px 10px rgba(0, 119, 182, 0.3);
        width: 130px;
        height: 130px;
        object-fit: cover;
    }

    /* 4. BUTTON STYLING */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        background-color: #238636; /* GitHub Green */
        color: white;
        border: 1px solid rgba(240, 246, 252, 0.1);
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #2ea043;
        transform: scale(1.02);
    }
    
    /* 5. CONTACT CARD STYLING */
    .contact-card {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        text-align: center;
        margin-top: 10px;
        color: #c9d1d9;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR SECTION ---
with st.sidebar:
    # Profile Image
    st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/4140/4140048.png" class="profile-pic">', unsafe_allow_html=True)
    
    st.write("") # Spacer
    st.markdown("<h3 style='text-align: center; color: white;'>Badre Narayanan</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e; font-size: 14px;'>Data Scientist & <br> Sports Analytics Specialist</p>", unsafe_allow_html=True)

    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Me", "Projects", "Skills", "Contact"],
        icons=["house", "person-circle", "code-slash", "tools", "envelope-paper"],
        default_index=0,
        styles={
            "container": {"background-color": "transparent", "padding": "0!important"},
            "icon": {"color": "#58a6ff", "font-size": "18px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin": "5px", "color": "#c9d1d9"},
            "nav-link-selected": {"background-color": "#1f6feb", "color": "white"},
        }
    )
    
    st.markdown("---")
    
    # Attractive Contact Section
    st.markdown("### 📬 Quick Connect")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("GitHub", "https://github.com/Badrergb/", use_container_width=True)
    with col2:
        st.link_button("Email", "mailto:narayananbadre@gmail.com", use_container_width=True)

    # Styled Info Card
    st.markdown("""
    <div class="contact-card">
        <div style="font-size: 14px; margin-bottom: 5px;">📍 Coimbatore, India</div>
        <div style="font-size: 14px;">📞 +91 74188 06611</div>
    </div>
    """, unsafe_allow_html=True)


# --- HOME SECTION ---
if selected == "Home":
    st.markdown("## Hello, I'm Badre Narayanan RG 👋")
    st.markdown("#### *Building the future with Automation, AI, and Sports Analytics.*")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1.5, 1], gap="medium")
    
    with col1:
        st.write("""
        I am an **Integrated MSc Data Science** student at **Amrita Vishwa Vidyapeetham**. 
        
        Unlike a traditional developer, I specialize in the intersection of **Sports & AI**. 
        I build intelligent systems that can analyze football tactics using **Graph Theory** and **Reinforcement Learning**, 
        while also possessing the **Full-Stack Engineering** skills to deploy them as real-world applications.
        """)
        
        st.download_button(
            label="📄 Download My Resume",
            data="Placeholder PDF Data", 
            file_name="Badre_Resume.pdf",
            mime="application/pdf",
        )

    with col2:
        # A placeholder for a hero image or animation
        st.markdown("""
        <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d;">
            <h4 style="color: #58a6ff;">Current Focus</h4>
            <ul style="list-style-type: none; padding-left: 0; color: #c9d1d9;">
                <li>⚽ Football Analytics</li>
                <li>🤖 Reinforcement Learning</li>
                <li>📊 Graph Theory</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- ABOUT ME SECTION ---
elif selected == "About Me":
    st.title("About Me 👨‍💻")
    
    st.write("I am a Data Science enthusiast bridging the gap between complex data and real-world applications using Python, Java, and Machine Learning.")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🎓 Education")
        st.info("""
        **Integrated MSc Data Science** *Amrita Vishwa Vidyapeetham (2022 - 2027)*
        
        **Higher Secondary (CBSE)** *Chelammal Vidhyaashram (2022)*
        """)
        
    with col2:
        st.subheader("🏆 Certifications")
        st.success("""
        ✅ **Data Analysis with Python** - IBM  
        ✅ **Deep Learning Specialization** (In Progress)
        """)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("Featured Projects 🚀")
    
    # Helper function for project cards
    def project_card(title, tech_stack, description, link):
        with st.container():
            st.markdown(f"### {title}")
            st.caption(f"🔧 Tech Stack: {tech_stack}")
            st.write(description)
            st.link_button("View Code", link)
            st.divider()

    project_card(
        "🌾 Farmer Management System",
        "Java | PostgreSQL | JSP | NetBeans",
        "A secure digital ledger for farmers to manage crop inventory and sales, bridging the gap to market prices. Includes secure user authentication and inventory management.",
        "https://github.com/Badrergb/Farmer-Management-System"
    )

    project_card(
        "🤖 RL Football Agent",
        "Python | TensorFlow | Reinforcement Learning",
        "Autonomous AI agent trained to make optimal tactical decisions in simulated matches using Deep Q-Networks (DQN). Features reward system optimization.",
        "#"
    )

    project_card(
        "⚽ Pass Network Analysis",
        "Graph Theory | Python | Data Visualization",
        "Visualizing team performance and player centrality using Graph Theory on match data. Calculates centrality metrics and visualizes passing flow.",
        "#"
    )

# --- SKILLS SECTION ---
elif selected == "Skills":
    st.title("Technical Skills 🛠️")
    
    tab1, tab2 = st.tabs(["💻 Programming & AI", "🌐 Development & DB"])
    
    with tab1:
        st.subheader("Python & Artificial Intelligence")
        st.write("Python (Pandas, Numpy, Scikit-Learn)")
        st.progress(90)
        
        st.write("Machine Learning & RL")
        st.progress(85)
        
        st.write("Data Visualization (Matplotlib, Seaborn)")
        st.progress(80)

    with tab2:
        st.subheader("Web & Databases")
        st.write("Java Development")
        st.progress(80)
        
        st.write("SQL (MySQL, PostgreSQL)")
        st.progress(75)
        
        st.write("Web (HTML/CSS, Streamlit)")
        st.progress(70)

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("Get in Touch 📬")
    
    st.write("Feel free to reach out to me for collaborations, especially in **Sports Analytics** or **AI** projects.")
    
    # Modern Contact Form using Columns
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        contact_form = """
        <form action="https://formsubmit.co/narayananbadre@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #30363d; border-radius: 5px; background-color: #0d1117; color: white;">
            <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #30363d; border-radius: 5px; background-color: #0d1117; color: white;">
            <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 12px; margin-bottom: 10px; height: 150px; border: 1px solid #30363d; border-radius: 5px; background-color: #0d1117; color: white;"></textarea>
            <button type="submit" style="background-color: #238636; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Contact Details")
        st.markdown("📧 **Email**")
        st.caption("narayananbadre@gmail.com")
        
        st.markdown("📱 **Phone**")
        st.caption("+91 74188 06611")
        
        st.markdown("📍 **Location**")
        st.caption("Coimbatore, India")
