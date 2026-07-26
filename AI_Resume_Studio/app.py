import streamlit as st
from resume_generator import generate_resume
from cover_letter import generate_cover_letter
from ats_analyzer import calculate_ats_score
from pdf_generator import create_pdf

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#312e81);
}

/* Hero Section */
.hero{
background: linear-gradient(135deg,#7C3AED,#2563EB,#06B6D4);
padding:35px;
border-radius:25px;
color:white;
text-align:center;
box-shadow:0px 20px 40px rgba(37,99,235,.45);
margin-bottom:25px;
}

/* Sidebar */
[data-testid="stSidebar"]{
background:#111827;
}

[data-testid="stSidebar"] *{
color:white;
}

/* Input Fields */

.stTextInput input,
.stTextArea textarea{

background:rgba(255,255,255,.15);

color:white;

border-radius:12px;

border:1px solid rgba(255,255,255,.2);

}

/* Main Content Text */
.stMarkdown,
.stMarkdown p,
.stMarkdown li,
.stMarkdown span{
    color:#FFFFFF !important;
}

/* Buttons */
.stButton>button{
background:linear-gradient(90deg,#8B5CF6,#3B82F6);
color:white;
font-weight:bold;
border:none;
border-radius:12px;
height:55px;
font-size:17px;
transition:0.3s;
}

.stButton>button:hover{
background:linear-gradient(90deg,#A855F7,#06B6D4);
transform:translateY(-3px);
box-shadow:0 12px 25px rgba(0,0,0,.25);
}

button[data-baseweb="tab"]{
    color:white !important;
    font-weight:600;
    font-size:17px;
}

button[data-baseweb="tab"][aria-selected="true"]{
    background:#4F46E5 !important;
    color:white !important;
    border-radius:10px;
}

/* Feature Cards */

.feature{

background:rgba(255,255,255,.12);

padding:20px;

border-radius:18px;

color:white;

text-align:center;

box-shadow:0 10px 20px rgba(0,0,0,.20);

}

/* Footer Hide */
footer{
visibility:hidden;
}

# header{
# visibility:hidden;
# }

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<h1>🤖 AI Resume Studio</h1>

<h4>Create ATS Friendly Resume & Cover Letter using Gemini AI</h4>

</div>
""",unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("👤 Candidate Details")

name = st.sidebar.text_input(
    "👤 Full Name",
    placeholder="Enter your name"
)

education = st.sidebar.text_area(
    "🎓 Education",
    placeholder="B.Tech CSE (AI & DS)"
)

skills = st.sidebar.text_area(
    "🛠 Skills",
    placeholder="Python, SQL, Machine Learning..."
)

experience = st.sidebar.text_area(
    "💼 Experience",
    placeholder="Internship / Projects / Work Experience"
)

job_role = st.sidebar.text_input(
    "🎯 Target Role",
    placeholder="Data Analyst"
)

st.sidebar.markdown("---")

st.sidebar.success("🤖 AI Powered Resume Generator")
st.sidebar.info(
"""
💡 Tips

✔ Mention all technical skills

✔ Mention projects

✔ Add internship experience
"""
)

# ---------------- FEATURE CARDS ---------------- #

st.markdown("""
<style>

.feature-card{
background:rgba(255,255,255,0.15);
backdrop-filter:blur(10px);
padding:20px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 8px 20px rgba(0,0,0,.20);
transition:0.3s;
}

.feature-card:hover{
transform:translateY(-5px);
box-shadow:0px 12px 25px rgba(59,130,246,.40);
}

.feature-title{
font-size:24px;
font-weight:bold;
margin-bottom:8px;
}

.feature-desc{
font-size:15px;
opacity:.95;
}

</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📄 Resume</div>
        <div class="feature-desc">
            Generate ATS Friendly Resume
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">✉️ Cover Letter</div>
        <div class="feature-desc">
            AI Personalized Cover Letter
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📊 ATS Score</div>
        <div class="feature-desc">
            Smart Resume Analysis
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- ACTION BUTTONS ---------------- #

btn1, btn2, btn3 = st.columns(3)

with btn1:
    generate_resume_btn = st.button("📄 Generate Resume")

with btn2:
    generate_cover_btn = st.button("✉️ Generate Cover Letter")

with btn3:
    check_ats_btn = st.button("📊 Check ATS")

st.markdown("---")

# ---------------- OUTPUT TABS ---------------- #

resume_tab,cover_tab,ats_tab=st.tabs(
[
"📄 Resume",
"✉ Cover Letter",
"📊 ATS Report"
]
)

# ---------------- RESUME ---------------- #

if generate_resume_btn:

    if name and education and skills and experience and job_role:

        with st.spinner("Generating Resume..."):

            resume = generate_resume(
                name,
                education,
                skills,
                experience,
                job_role
            )

        st.toast("Resume Generated Successfully 🎉")
        st.balloons()

        with resume_tab:

            st.success("✅ Resume Generated Successfully")

            st.markdown("### 📄 Generated Resume")

            st.markdown(resume)

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="⬇ Resume (.txt)",
                    data=resume,
                    file_name="AI_Resume.txt",
                    mime="text/plain"
                )

            with col2:

                resume_pdf = create_pdf("AI Resume", resume)

                st.download_button(
                    label="📄 Resume (.pdf)",
                    data=resume_pdf,
                    file_name="AI_Resume.pdf",
                    mime="application/pdf"
                )

    else:

        st.warning("⚠ Please fill all fields before generating the resume.")

# ---------------- COVER LETTER ---------------- #

if generate_cover_btn:

    if name and education and skills and experience and job_role:

        with st.spinner("Generating Cover Letter..."):

            cover_letter = generate_cover_letter(
                name,
                education,
                skills,
                experience,
                job_role
            )

        st.toast("Cover Letter Generated Successfully ✉️")

        with cover_tab:

            st.success("✅ Cover Letter Generated Successfully")

            st.markdown("### ✉️ Generated Cover Letter")

            st.markdown(cover_letter)

            col1, col2 = st.columns(2)

            with col1:

                st.download_button(
                    label="⬇ Cover Letter (.txt)",
                    data=cover_letter,
                    file_name="AI_Cover_Letter.txt",
                    mime="text/plain"
                )

            with col2:

                cover_pdf = create_pdf(
                "AI Cover Letter",
                cover_letter
            )

            st.download_button(
                label="📄 Cover Letter (.pdf)",
                data=cover_pdf,
                file_name="AI_Cover_Letter.pdf",
                mime="application/pdf"
            )

    else:

        st.warning("⚠ Please fill all fields before generating the cover letter.")


# ---------------- ATS ANALYSIS ---------------- #

if check_ats_btn:

    if skills:

        score, matched, missing = calculate_ats_score(skills)

        with ats_tab:

            st.markdown("## 📊 ATS Analysis Report")

            st.metric("ATS Score", f"{score}%")

            st.progress(score / 100)

            st.markdown("### ✅ Matched Skills")

            if matched:
                for skill in matched:
                    st.success(skill)
            else:
                st.info("No matching skills found.")

            st.markdown("### ❌ Missing Skills")

            if missing:
                for skill in missing:
                    st.error(skill)
            else:
                st.success("Excellent! No important skills are missing.")

    else:

        st.warning("⚠ Please enter your skills first.")

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
"""
<div style="text-align:center; padding:15px; color:white;">

<h4>🤖 AI Resume Studio</h4>

<p>Developed by <b>Muskan</b></p>

<p>B.Tech CSE (AI & Data Science)</p>

</div>
""",
unsafe_allow_html=True
)
