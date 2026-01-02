import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Badre Narayanan RG | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
)

# --- CUSTOM CSS ---
# This adds a modern gradient background and styles the buttons
st.markdown("""
    <style>
    /* 1. MAIN BACKGROUND GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #141414 0%, #1e2a38 100%);
        background-attachment: fixed;
    }

    /* 2. CARD/CONTAINER STYLING */
    div[data-testid="stMetric"], div[data-testid="stMarkdownContainer"] p {
        color: #e0e0e0; /* Light text for dark mode */
    }
    
    /* 3. SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #0e1117;
        border-right: 1px solid #262730;
    }
    
    /* 4. BUTTON STYLING */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #0077b6; /* Primary Blue */
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0096c7;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)
    st.markdown("## Navigation")
    
    # REPLACED RADIO BUTTONS WITH OPTION MENU
    selected = option_menu(
        menu_title=None,  # Required
        options=["Home", "About Me", "Projects", "Skills", "Contact"],
        icons=["house", "person", "code-slash", "tools", "envelope"],  # Bootstrap Icons
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#0077b6", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#0077b6"},
        }
    )
    
    st.markdown("---")
    st.write("📍 **Coimbatore, India**")
    st.write("📧 narayananbadre@gmail.com")
    st.markdown("[GitHub Profile](https://github.com/Badrergb/)")

# --- HOME SECTION ---
if selected == "Home":
    st.title("Hello, I'm Badre Narayanan RG 👋")
    st.subheader("Data Scientist | Full Stack Developer | Sports Analytics")
    
    col1, col2 = st.columns([1, 2], gap="medium")
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", caption="Badre Narayanan RG", width=300)
        
    with col2:
        st.markdown("""
        ### 🚀 Building the future with Automation, AI, and Sports Analytics.
        
        I am an **Integrated MSc Data Science** student at **Amrita Vishwa Vidyapeetham**. 
        Unlike a traditional developer, I specialize in the intersection of **Sports & AI**. 
        
        I build intelligent systems that can analyze football tactics using **Graph Theory** and **Reinforcement Learning**, 
        while also possessing the **Full-Stack Engineering** skills to deploy them as real-world applications.
        """)
        
        st.download_button(
            label="📄 Download Resume",
            data="Placeholder for actual resume PDF bytes",
            file_name="Badre_Narayanan_Resume.pdf",
            mime="application/pdf"
        )
        st.info("💡 Check out the 'Projects' tab to see my work in Sports Analytics!")

# --- ABOUT ME SECTION ---
elif selected == "About Me":
    st.title("About Me 👨‍💻")
    
    st.markdown("""
    I am a Data Science enthusiast bridging the gap between complex data and real-world applications using Python, Java, and Machine Learning.
    Currently, I am focused on mastering **Reinforcement Learning** and **Graph Theory** applied to football analytics.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🎓 Education")
        st.markdown("""
        **Integrated MSc Data Science** *Amrita Vishwa Vidyapeetham (2022 - 2027)*
        
        **Higher Secondary (CBSE)** *Chelammal Vidhyaashram (2022)*
        """)
        
    with col2:
        st.subheader("🏆 Certifications")
        st.markdown("""
        ✅ **Data Analysis with Python** - IBM  
        ✅ **Deep Learning Specialization** (In Progress)
        """)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("Featured Projects 📂")
    st.markdown("Here are some of the key projects I've worked on.")
    st.markdown("---")
    
    # Helper function to create project cards
    def project_card(title, tech, desc, link, link_text="View Code"):
        with st.container():
            st.markdown(f"### {title}")
            st.caption(f"🔧 {tech}")
            st.write(desc)
            st.link_button(link_text, link)
            st.markdown("---")

    project_card(
        "🌾 Farmer Management System", 
        "Java | PostgreSQL | JSP",
        "A secure digital ledger for farmers to manage crop inventory and sales, bridging the gap to market prices.",
        "https://github.com/Badrergb/Farmer-Management-System"
    )

    project_card(
        "🤖 RL Football Agent", 
        "Python | TensorFlow | RL",
        "Autonomous AI agent trained to make optimal tactical decisions in simulated matches using Deep Q-Networks (DQN).",
        "#"
    )

    project_card(
        "⚽ Pass Network Analysis", 
        "Graph Theory | Python | Data Viz",
        "Visualizing team performance and player centrality using Graph Theory on match data.",
        "#"
    )

# --- SKILLS SECTION ---
elif selected == "Skills":
    st.title("Technical Skills 🛠️")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("Python & AI")
        st.progress(90, text="Python (Pandas, Numpy, Scikit-Learn)")
        st.progress(85, text="Machine Learning & RL")
        st.progress(80, text="Data Visualization (Matplotlib, Seaborn)")

    with col2:
        st.subheader("Development & DB")
        st.progress(80, text="Java Development")
        st.progress(75, text="SQL (MySQL, PostgreSQL)")
        st.progress(70, text="Web (HTML/CSS, Streamlit)")

    st.subheader("Other Skills")
    st.markdown("`Graph Theory` `Sports Analytics` `Automation` `Tableau`")

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("Get in Touch 📬")
    
    st.write("Feel free to reach out to me for collaborations, especially in **Sports Analytics** or **AI** projects.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📧 **Email**\n\nnarayananbadre@gmail.com")
    with col2:
        st.info("📱 **Phone**\n\n+91 74188 06611")
    with col3:
        st.info("📍 **Location**\n\nCoimbatore, India")
    
    st.markdown("---")
    
    st.subheader("Send me a message")
    contact_form = """
    <form action="https://formsubmit.co/narayananbadre@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #444; border-radius: 5px; background-color: #262730; color: white;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 12px; margin-bottom: 10px; border: 1px solid #444; border-radius: 5px; background-color: #262730; color: white;">
        <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 12px; margin-bottom: 10px; height: 150px; border: 1px solid #444; border-radius: 5px; background-color: #262730; color: white;"></textarea>
        <button type="submit" style="background-color: #0077b6; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)