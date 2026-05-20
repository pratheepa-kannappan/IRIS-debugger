#This is the frontend file
import streamlit as st
import json
import time
from utils.llm_client import LLMClient
from utils.prompt_builder import build_prompt

st.set_page_config(page_title="IRIS AI", layout="wide", page_icon="🐛")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
    background-color: #f7f5f0;
}

.stApp { background-color: #f7f5f0; }

h1 { font-size: 2rem !important; font-weight: 600 !important; color: #2C2C2A !important; letter-spacing: -0.03em !important; }
h1 span { color: #1D9E75; }

.stTextArea textarea {
    font-family: 'DM Mono', monospace !important;
    font-size: 13px !important;
    background: #fff !important;
    border: 0.5px solid #d4cfc5 !important;
    border-radius: 10px !important;
    color: #2C2C2A !important;
}

.stButton > button {
    width: 100%;
    background: #2C2C2A !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 0.75rem !important;
    transition: background 0.2s !important;
}
.stButton > button:hover { background: #1D9E75 !important; }

.result-card {
    background: #f7f5f0;
    border: 0.5px solid #d4cfc5;
    border-radius: 12px;
    padding: 1.1rem;
    margin-bottom: 0.75rem;
}

.result-label {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #888780;
    margin-bottom: 0.5rem;
}

.result-text { font-size: 14px; color: #2C2C2A; line-height: 1.6; }

.cause-item { display: flex; gap: 8px; margin-bottom: 4px; font-size: 13px; color: #444441; }
.cause-dot { width: 5px; height: 5px; border-radius: 50%; background: #BA7517; margin-top: 7px; flex-shrink: 0; }

.tag {
    display: inline-block;
    background: #EAF3DE;
    color: #3B6D11;
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 11px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1>IR<span style="color:#1D9E75">IS</span> AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#888780; font-size:0.95rem; margin-top:-0.5rem;">Python visualizer, visual debugger</p>', unsafe_allow_html=True)

