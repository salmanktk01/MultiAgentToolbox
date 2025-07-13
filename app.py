import streamlit as st
import asyncio
from agent_runner import run_agent_query
import time

# Configure page
st.set_page_config(
    page_title="Multi-Agent Toolbox",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Hide default Streamlit styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom styling for the app */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-subtitle {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.2rem;
        font-weight: 300;
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #333;
    }
    
    .feature-desc {
        font-size: 1rem;
        color: #666;
        opacity: 0.9;
    }
    
    /* Main query card */
    .query-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        border: 2px solid #e0e0e0 !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        transition: border-color 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Response styling */
    .response-success {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        color: white;
    }
    
    .response-error {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        color: white;
    }
    
    .response-content {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1rem;
        color: #333;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Sidebar styling */
    .sidebar-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        color: white;
    }
    
    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: white;
    }
    
    .sidebar-content {
        color: rgba(255, 255, 255, 0.8);
        line-height: 1.6;
    }
    
    /* Example queries */
    .example-queries {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .example-tag {
        background: #f0f2f6;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        color: #333;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    
    /* Block container adjustments */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1 class="main-title">🤖 Multi-Agent Toolbox</h1>
    <p class="main-subtitle">Your intelligent assistant for weather information and mathematical calculations</p>
</div>
""", unsafe_allow_html=True)

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌤️</div>
        <div class="feature-title">Weather</div>
        <div class="feature-desc">Get real-time weather information for any city worldwide</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Main query interface
    st.markdown('<div class="query-card">', unsafe_allow_html=True)
    
    st.markdown("I can help you with weather forecasts and mathematical calculations.")
    
    user_prompt = st.text_input(
        "",
        placeholder="Ask me about weather or math...",
        label_visibility="collapsed"
    )
    
    submit_button = st.button("🚀 Submit Query", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔢</div>
        <div class="feature-title">Math</div>
        <div class="feature-desc">Perform calculations and solve mathematical problems</div>
    </div>
    """, unsafe_allow_html=True)

# Process query
if submit_button and user_prompt.strip():
    with st.spinner("🔄 Processing your request..."):
        try:
            time.sleep(0.5)  # Small delay for better UX
            result = asyncio.run(run_agent_query(user_prompt))
            final_response = result["messages"][-1].content
            
            # Display success response
            st.markdown(f"""
            <div class="response-success">
                <h3>✅ Agent Response</h3>
                <div class="response-content">
                    {final_response}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("Query processed successfully! 🎉")
            
        except Exception as e:
            # Display error response
            st.markdown(f"""
            <div class="response-error">
                <h3>❌ Error Occurred</h3>
                <div class="response-content">
                    {str(e)}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.error("An error occurred while processing your request.")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: rgba(255,255,255,0.6);">
    <p>🚀 Powered by LangChain, Groq, and OpenWeatherMap</p>
</div>
""", unsafe_allow_html=True)