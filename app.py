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

st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)

error_input = st.text_area(
    "Python Error Traceback",
    placeholder="Paste your Python error here...\n\nTraceback (most recent call last):\n  File \"main.py\", line 12, in <module>",
    height=150,
    label_visibility="collapsed"
)

if st.button("Analyze Error →"):
    if not error_input.strip():
        st.markdown('<div style="background:#FAEEDA;border:0.5px solid #FAC775;border-radius:10px;padding:0.75rem 1rem;font-size:13px;color:#633806;margin-top:0.5rem">Please paste an error traceback to analyze.</div>', unsafe_allow_html=True)
    else:
        llm = LLMClient()
        with st.spinner("Analyzing..."):
            start_time = time.time()
            prompt = build_prompt(error_input)
            response = llm.get_response(prompt)
            end_time = time.time()

        try:
            data = json.loads(response)

            st.markdown('<div class="tag">Analysis complete</div>', unsafe_allow_html=True)
            st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f'''<div class="result-card">
                    <div class="result-label">📘 Meaning</div>
                    <div class="result-text">{data.get("meaning", "")}</div>
                </div>''', unsafe_allow_html=True)

                causes_html = "".join([f'<div class="cause-item"><div class="cause-dot"></div><span>{c}</span></div>' for c in data.get("causes", [])])
                st.markdown(f'''<div class="result-card">
                    <div class="result-label">⚠️ Causes</div>
                    {causes_html}
                </div>''', unsafe_allow_html=True)

            with col2:
                st.markdown(f'''<div class="result-card">
                    <div class="result-label">🛠 Fix</div>
                    <div class="result-text">{data.get("fix", "")}</div>
                </div>''', unsafe_allow_html=True)

                st.markdown('<div class="result-card"><div class="result-label">💡 Example</div></div>', unsafe_allow_html=True)
                st.code(data.get("example", ""), language="python")

            st.markdown(f'<p style="font-size:11px;color:#B4B2A9;margin-top:0.5rem">Response time: {round(end_time - start_time, 2)}s</p>', unsafe_allow_html=True)

        except:
            st.markdown('<div style="background:#FCEBEB;border:0.5px solid #F7C1C1;border-radius:10px;padding:0.75rem 1rem;font-size:13px;color:#501313;">Failed to parse response.</div>', unsafe_allow_html=True)
            st.write(response)
