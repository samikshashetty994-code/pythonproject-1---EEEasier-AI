from formulas import FORMULAS
from ocr import extract_text
from ai import ask_ai
import streamlit as st
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="EEEasier AI",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020617,#0f172a,#1e3a8a);
background-attachment:fixed;
}

section[data-testid="stSidebar"]{
background:#111827;
border-right:1px solid #374151;
}

h1{
color:#60a5fa !important;
font-size:48px;
font-weight:bold;
}

h2,h3,h4,h5,p,label{
color:white!important;
}

div.stButton > button{
background:linear-gradient(90deg,#2563eb,#7c3aed);
color:white;
border:none;
border-radius:12px;
height:50px;
font-size:18px;
font-weight:bold;
transition:0.3s;
}

div.stButton > button:hover{
background:linear-gradient(90deg,#7c3aed,#2563eb);
transform:scale(1.03);
}

.stTextInput input,
.stTextArea textarea{
background:#1f2937;
color:white;
border-radius:10px;
}

.stSelectbox{
color:white;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    selected = option_menu(
        menu_title="⚡ EEEasier AI",

        options=[
            "Home",
            "Scan Question",
            "Upload Notes",
            "Circuit Explainer",
            "AI Chat",
            "Formula Finder",
            "Numerical Solver",
            "About"
        ],

        icons=[
            "house",
            "camera",
            "file-earmark-text",
            "cpu",
            "robot",
            "book",
            "calculator",
            "info-circle"
        ],

        default_index=0
    )

# ---------------- HOME ---------------- #

if selected=="Home":

    st.title("⚡ EEEasier AI")

    st.subheader("Your Personal Electrical Engineering Assistant")

    col1,col2,col3=st.columns(3)

    with col1:
        st.info("📷 Scan Engineering Questions")

    with col2:
        st.info("📄 Upload PDF Notes")

    with col3:
        st.info("🤖 AI Chatbot")

# ---------------- SCAN QUESTION ---------------- #

elif selected == "Scan Question":

    st.title("📷 Scan Question")

    uploaded = st.file_uploader(
        "Upload Question Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded:

        st.image(uploaded)

        if st.button("Solve Question"):

            with st.spinner("Reading Question..."):

                question = extract_text(uploaded)

            st.subheader("Extracted Text")

            st.write(question)

            with st.spinner("Solving..."):
                print("Sending to AI:", question)

                answer = ask_ai(question)

                print("AI Response:", answer)

            st.subheader("Answer")

            st.success(answer)

# ---------------- PDF ---------------- #

elif selected == "Upload Notes":

    st.title("📄 Upload Notes")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_pdf:

        st.success("PDF uploaded successfully!")

        if st.button("Analyze Notes"):
            with st.spinner("Reading notes..."):
                text = extract_pdf_text(uploaded_pdf)

            st.subheader("Extracted Notes")

            st.write(text[:2000])  # display first 2000 characters

            with st.spinner("Generating explanation..."):
                summary = ask_ai(
                    """
                    You are an Electrical Engineering professor.
                    Analyze these notes and provide:
                    - Important concepts
                    - Key formulas
                    - Short explanations
                    - Exam points

                    Notes:
                    """
                    + text
                )

            st.subheader("AI Explanation")

            st.write(summary)

# ---------------- CIRCUIT ---------------- #

elif selected=="Circuit Explainer":

    st.title("🔌 Circuit Diagram Explainer")

    st.file_uploader(
        "Upload Circuit",
        type=["jpg","jpeg","png"]
    )

# ---------------- CHAT ---------------- #

elif selected == "Chat":

    st.title("💬 EEEasier AI Chat")

    st.write(
        "Ask any Electrical and Electronics Engineering question."
    )

    user_question = st.text_area(
        "Enter your question"
    )

    if st.button("Ask AI"):

        if user_question:

            with st.spinner("Thinking..."):

                response = ask_ai(
                    """
                    You are EEEasier AI, an Electrical and Electronics Engineering tutor.

                    Answer the question clearly.
                    Include:
                    - Concept explanation
                    - Important formulas (if applicable)
                    - Practical applications
                    - Examples

                    Question:
                    """
                    + user_question
                )

            st.subheader("AI Response")

            st.write(response)

        else:

            st.warning("Please enter a question")

# ---------------- FORMULA ---------------- #
# ---------------- FORMULA ---------------- #

elif selected == "Formula Finder":

    st.title("📘 Formula Finder")

    topic = st.selectbox(
        "Choose Topic",
        FORMULAS.keys()
    )

    formula = st.selectbox(
        "Choose Formula",
        FORMULAS[topic].keys()
    )

    st.subheader(formula)

    st.code(
        FORMULAS[topic][formula]
    )

# ---------------- NUMERICAL ---------------- #
elif selected == "Numerical Solver":

    st.title("🧮 Numerical Solver")

    problem = st.text_area(
        "Enter your electrical numerical problem"
    )

    if st.button("Solve Numerical"):

        if problem:

            with st.spinner("Solving..."):

                solution = ask_ai(
                    """
                    Solve this Electrical Engineering numerical problem.

                    Show:
                    1. Given values
                    2. Formula used
                    3. Step-by-step calculation
                    4. Final answer

                    Problem:
                    """
                    + problem
                )

            st.subheader("Solution")
            st.write(solution)

        else:
            st.warning("Please enter a problem")

# ---------------- ABOUT ---------------- #

elif selected=="About":

    st.title("About")

    st.write("""
EEEasier AI

An AI-powered Electrical Engineering Assistant.

Features

• OCR Question Scanner

• AI Chat

• Formula Finder

• Circuit Explainer

• PDF Notes Reader

• Numerical Solver
""")
