import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Hessian Neural Network Explorer",
    page_icon="🧠",
    layout="wide",
)

# Remove Streamlit's default padding so the embedded app fills the viewport
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; }
        #MainMenu, header, footer { visibility: hidden; }
        iframe { border: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_content = Path("hessian_pruning.html").read_text(encoding="utf-8")

st.components.v1.html(html_content, height=960, scrolling=True)
