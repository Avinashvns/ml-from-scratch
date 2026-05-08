import streamlit as st

from components.navigation import run_navigation

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="ML From Scratch",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("static/style.css", "r", encoding="utf-8") as f:
    css = f.read()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)

# =====================================================
# RUN NAVIGATION
# =====================================================

run_navigation()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    Made with Avinash Singh ❤️ Since 2026
</div>
""", unsafe_allow_html=True)