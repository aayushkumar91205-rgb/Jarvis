import streamlit as st

def render_collapsible_sidebar():
    st.markdown("### ⚡ NAVIGATION")
    
    mode = st.radio(
        "Select Operating Mode",
        ["Realtime", "Text Chat", "Action Hub", "Time Table", "Admin Dashboard"],
        key="navigation_mode_radio"
    )
    st.session_state.mode = mode
    
    st.markdown("---")
    st.markdown("### 🚀 QUICK ACTIONS")
    if st.button("📚 Math Study Sheet", use_container_width=True):
        st.session_state.mode = "Action Hub"
        st.rerun()
    if st.button("⏱️ Focus Pomodoro", use_container_width=True):
        st.session_state.mode = "Time Table"
        st.rerun()
