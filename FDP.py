import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------------

st.set_page_config(
    page_title="Mathematics to Intelligence",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Mathematics to Intelligence")
st.subheader("A Digital Twin of Human Cognitive Growth")
st.markdown(
    "### Faculty Development Program - Ramaiah Technology Campus"
)

# -------------------------------------------------------
# PARTICIPANT DETAILS
# -------------------------------------------------------

st.sidebar.header("Participant Details")

name = st.sidebar.text_input("Participant Name")
department = st.sidebar.text_input("Department")

designation = st.sidebar.selectbox(
    "Designation",
    [
        "Professor",
        "Associate Professor",
        "Assistant Professor",
        "Research Scholar"
    ]
)

experience = st.sidebar.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50,
    value=5
)

# -------------------------------------------------------
# TABS
# -------------------------------------------------------

pre_tab, learn_tab, post_tab, dashboard_tab = st.tabs(
    [
        "Pre-Test",
        "Learning Content",
        "Post-Test",
        "Digital Twin Dashboard"
    ]
)

# -------------------------------------------------------
# PRE TEST
# -------------------------------------------------------

with pre_tab:

    st.header("Pre-Test")

    q1 = st.radio(
        "1. What is 25% of 200?",
        ["20", "40", "50", "60"],
        key="pre1"
    )

    q2 = st.radio(
        "2. Area of a room 10 m × 8 m?",
        ["60", "70", "80", "90"],
        key="pre2"
    )

    q3 = st.radio(
        "3. A tank fills in 5 hours. What percentage fills in 2 hours?",
        ["20%", "40%", "50%", "60%"],
        key="pre3"
    )

    q4 = st.radio(
        "4. Which route is shorter?",
        ["8 km", "12 km"],
        key="pre4"
    )

    q5 = st.radio(
        "5. Best method to save water?",
        [
            "Rainwater Harvesting",
            "Increasing Water Usage"
        ],
        key="pre5"
    )

    pre_score = 0

    if q1 == "50":
        pre_score += 2

    if q2 == "80":
        pre_score += 2

    if q3 == "40%":
        pre_score += 2

    if q4 == "8 km":
        pre_score += 2

    if q5 == "Rainwater Harvesting":
        pre_score += 2

    st.session_state["pre_score"] = pre_score

    st.success(
        f"Pre-Test Score = {pre_score}/10"
    )

# -------------------------------------------------------
# LEARNING CONTENT
# -------------------------------------------------------

with learn_tab:

    st.header("How Human Cognitive Growth Happens")

    st.markdown("""
### Simple Learning Journey

Exposure ➜ Understanding ➜ Application ➜ Analysis ➜ Innovation

Every learner travels through these stages.
""")

    st.subheader("Example 1: Child Learning Numbers")

    st.markdown("""
**Stage 1**
- Learns number 5

**Stage 2**
- Counts 5 apples

**Stage 3**
- Solves 5 + 3

**Stage 4**
- Solves word problems

**Stage 5**
- Creates own solution

This is cognitive growth.
""")

    st.subheader("Example 2: Civil Engineering Student")

    st.markdown("""
### Surveying Skill Development

| Stage | Skill |
|---------|---------|
| Beginning | 2/10 |
| After Survey Camp | 7/10 |
| After Internship | 9/10 |

The learner grows continuously.
""")

    st.subheader("What is a Digital Twin?")

    st.info("""
A Digital Twin is a virtual representation of a learner.

It tracks:

✅ Knowledge

✅ Application

✅ Problem Solving

✅ Creativity

✅ Confidence
""")

    st.subheader("Cognitive Growth Formula")

    st.latex(
        r"CGI = \frac{Knowledge + Application + ProblemSolving + Creativity + Confidence}{5}"
    )

# -------------------------------------------------------
# POST TEST
# -------------------------------------------------------

with post_tab:

    st.header("Post-Test")

    p1 = st.radio(
        "1. What is 35% of 240?",
        ["74", "84", "94", "104"],
        key="post1"
    )

    p2 = st.radio(
        "2. Concrete Volume = 10 × 5 × 0.2 ?",
        ["8", "10", "12", "15"],
        key="post2"
    )

    p3 = st.radio(
        "3. A Digital Twin tracks",
        [
            "Learning Growth",
            "Only Age",
            "Only Marks"
        ],
        key="post3"
    )

    p4 = st.radio(
        "4. Learning progression is",
        [
            "Exposure → Understanding → Application",
            "Application → Exposure"
        ],
        key="post4"
    )

    p5 = st.radio(
        "5. Best sustainability solution",
        [
            "Rainwater Harvesting",
            "Increase Water Waste"
        ],
        key="post5"
    )

    post_score = 0

    if p1 == "84":
        post_score += 2

    if p2 == "10":
        post_score += 2

    if p3 == "Learning Growth":
        post_score += 2

    if p4 == "Exposure → Understanding → Application":
        post_score += 2

    if p5 == "Rainwater Harvesting":
        post_score += 2

    st.session_state["post_score"] = post_score

    st.success(
        f"Post-Test Score = {post_score}/10"
    )

# -------------------------------------------------------
# DASHBOARD
# -------------------------------------------------------

with dashboard_tab:

    st.header("Digital Twin Dashboard")

    pre = st.session_state.get("pre_score", 0)
    post = st.session_state.get("post_score", 0)

    growth = post - pre

    c1, c2, c3 = st.columns(3)

    c1.metric("Pre-Test", pre)
    c2.metric("Post-Test", post)
    c3.metric("Growth", growth)

    # Digital Twin Dimensions

    knowledge = min(100, post * 10)
    application = min(100, post * 9)
    problem_solving = min(100, post * 8)
    creativity = min(100, post * 7)
    confidence = min(100, post * 10)

    cgi = round(
        (
            knowledge
            + application
            + problem_solving
            + creativity
            + confidence
        ) / 5,
        2
    )

    st.subheader(f"Cognitive Growth Index (CGI): {cgi}")

    # Radar Chart

    categories = [
        "Knowledge",
        "Application",
        "Problem Solving",
        "Creativity",
        "Confidence"
    ]

    values = [
        knowledge,
        application,
        problem_solving,
        creativity,
        confidence
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name=name if name else "Participant"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Growth Trend

    growth_df = pd.DataFrame(
        {
            "Stage": ["Pre-Test", "Post-Test"],
            "Score": [pre, post]
        }
    )

    st.subheader("Growth Trend")

    st.line_chart(
        growth_df.set_index("Stage")
    )

    if growth >= 4:
        category = "High Cognitive Growth"
        st.success(category)

    elif growth >= 2:
        category = "Moderate Cognitive Growth"
        st.info(category)

    else:
        category = "Low Cognitive Growth"
        st.warning(category)

    results = pd.DataFrame(
        {
            "Participant": [name],
            "Department": [department],
            "Designation": [designation],
            "Experience": [experience],
            "Pre-Test": [pre],
            "Post-Test": [post],
            "Growth": [growth],
            "Knowledge": [knowledge],
            "Application": [application],
            "Problem Solving": [problem_solving],
            "Creativity": [creativity],
            "Confidence": [confidence],
            "CGI": [cgi],
            "Category": [category]
        }
    )

    st.subheader("Result Summary")
    st.dataframe(results)

    csv = results.to_csv(index=False)

    st.download_button(
        label="📥 Download FDP Report",
        data=csv,
        file_name=f"{name}_Digital_Twin_Report.csv",
        mime="text/csv"
    )