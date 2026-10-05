import streamlit as st

def speak_and_notify(text, title="Jarvis Notification"):
    # Triggers browser speech synthesis and visual toast notification
    st.toast(text, icon="🤖")

def render_notification_permission_button():
    st.markdown("""
    <script>
    if (Notification.permission !== "granted") {
        Notification.requestPermission();
    }
    </script>
    """, unsafe_allow_html=True)
