import streamlit as st

def render_realtime_orb(display_name, groq_api_key=""):
    st.markdown("""
    <style>
    .jarvis-orb-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 30px;
    }
    .jarvis-orb {
        width: 120px;
        height: 120px;
        background: radial-gradient(circle, #00d2ff 0%, #3a7bd5 100%);
        border-radius: 50%;
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.6);
        animation: pulse-orb 2s infinite ease-in-out;
    }
    @keyframes pulse-orb {
        0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(0, 210, 255, 0.4); }
        50% { transform: scale(1.05); box-shadow: 0 0 45px rgba(0, 210, 255, 0.8); }
        100% { transform: scale(0.95); box-shadow: 0 0 20px rgba(0, 210, 255, 0.4); }
    }
    </style>
    <div class="jarvis-orb-container">
        <div class="jarvis-orb"></div>
        <h3 style="margin-top: 15px; color: #00d2ff;">JARVIS REALTIME ONLINE</h3>
    </div>
    """, unsafe_allow_html=True)
    
    quick_prompt = st.text_input("💬 Quick Command to Jarvis...", placeholder="Ask anything...", key="realtime_quick_input")
    return quick_prompt
