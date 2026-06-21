import streamlit as st
import streamlit.components.v1 as components
from transc import get_transcript
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ----------------------------------------------------------------------------

st.set_page_config(page_title="Video Summarizer", page_icon="🎬", layout="wide")

# Custom CSS for UI enhancements and hiding native Streamlit top-right menus
st.markdown("""
<style>
/* 1. Change primary button (Get Summary) to cyan blue */
button[kind="primary"] {
    background-color: #00BFFF !important;
    border-color: #00BFFF !important;
    color: white !important;
}
button[kind="primary"]:hover {
    background-color: #008CBA !important;
    border-color: #008CBA !important;
}

/* 2. Wrap st.code text line-by-line and add vertical scrollbar */
div[data-testid="stCodeBlock"] pre, div[data-testid="stCodeBlock"] code {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
}
div[data-testid="stCodeBlock"] {
    max-height: 400px;
    overflow-y: auto;
    border: 1px solid #ddd;
    border-radius: 5px;
}

/* 3. Hide Streamlit's native top-right UI elements */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stStatusWidget"] {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.header("Video Summarizer 🎬")

# Initialize session state for the summary and input link
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "yt_link" not in st.session_state:
    st.session_state.yt_link = ""

def clear_app_state():
    st.session_state.summary = ""
    st.session_state.yt_link = ""

full_yt = st.text_input("Enter video link", key="yt_link")

# Create closely packed columns for buttons using a spacer at the end
col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1, 1, 5], gap="small")

with col1:
    get_sum = st.button("✨ Get Summary", type="primary", use_container_width=True)
with col2:
    stop_btn = st.button("🛑 Stop", use_container_width=True)
with col3:
    clear_btn = st.button("🗑️ Clear", on_click=clear_app_state, use_container_width=True)
with col4:
    print_btn = st.button("🖨️ Print", use_container_width=True)

# Handle Stop action
if stop_btn:
    st.warning("✋ Summarization process stopped.")
    st.stop()

# Handle Print action (injects JS to trigger native print)
if print_btn:
    components.html("""
    <script>
    parent.window.print();
    </script>
    """, height=0)

# Handle Get Summary action
if get_sum and full_yt:
    video_id = ""
    try:
        video_id = full_yt.split("v=")[-1].split("&")[0]
        if len(video_id) != 11 and "=" in full_yt:
            video_id = full_yt.split("=")[1]
    except Exception:
        video_id = full_yt

    if video_id:
        success, tx = get_transcript(video_id)
        
        if not success:
            st.error(f"⚠️ {tx}")
            st.stop()
        
        with st.spinner("Downloading/Loading the model (this might take a few minutes the first time)..."):
            tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
            model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
        
        with st.spinner("Analyzing transcript and generating summary (this takes 20-40 seconds)..."):
            inputs = tokenizer(tx[:4000], return_tensors="pt", max_length=1024, truncation=True)
            outputs = model.generate(**inputs, max_length=230)
            res = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.session_state.summary = res
    
        st.success("✅ Summary Completed!")

# Display summary if it's available in session state
if st.session_state.summary:
    st.markdown("### 📝 Your Summary:")
    try:
        # Native Streamlit parameter to force text wrapping
        st.code(st.session_state.summary, language="markdown", wrap_lines=True)
    except TypeError:
        # Fallback for older Streamlit versions without losing the scrollbar request
        st.text_area("", st.session_state.summary, height=350, label_visibility="collapsed")

