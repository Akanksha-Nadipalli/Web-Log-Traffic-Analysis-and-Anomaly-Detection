import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# =============================
# Page Config & Dark Theme CSS
# =============================
st.set_page_config(layout="wide", page_title="Web Traffic Intelligence")
if "started" not in st.session_state:
    st.session_state.started = False


st.markdown("""
<style>
.stApp { background-color: #0e1117; color: #ffffff; }

/* Landing page hero */
.hero {
    text-align: center;
    padding-top: 40px;
    padding-bottom: 60px;
    animation: fadeUp 1.2s ease;
}

.hero h1 {
    font-size: 64px;
    font-weight: bold;
}

.hero p {
    font-size: 22px;
    color: #94a3b8;
}

/* Center button */
.center-btn {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}

/* Button styling */
div.stButton > button {
    background: linear-gradient(90deg, cyan, blue);
    color: white;
    height: 60px;
    font-size: 20px;
    border-radius: 12px;
    padding: 0px 40px;
}

/* Feature cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 15px;
    transition: 0.4s;
    border: 1px solid rgba(255,255,255,0.1);
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 30px cyan;
}

/* Dashboard styles (UNCHANGED) */
.section-card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #30363d;
    margin-bottom: 20px;
}

.graph-container {
    border: 1.5px solid #30363d;
    border-radius: 10px;
    padding: 15px;
    background-color: #0d1117;
    margin-bottom: 20px;
}

.clean-title {
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 12px;
    display: block;
    color: #e6edf3;
}

.left-panel-header {
    border-bottom: 1px solid #30363d;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

/* Animation */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# =============================
# LANDING PAGE
# =============================
if st.session_state.started == False:


    st.markdown("""
    <style>

    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #020617, #0f172a, #020617, #0a0f1f);
        background-size: 400% 400%;
        animation: gradientMove 12s ease infinite;
    }

    @keyframes gradientMove {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Gradient title */
    .gradient-text {
        font-size: clamp(28px, 4.5vw, 56px);
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, cyan, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        font-size: clamp(16px, 2vw, 22px);
        color: #94a3b8;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* Glow orb */
    .orb {
        position: absolute;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, cyan, transparent);
        border-radius: 50%;
        filter: blur(120px);
        opacity: 0.2;
        animation: float 6s ease-in-out infinite;
    }

    @keyframes float {
        0% {transform: translateY(0px);}
        50% {transform: translateY(-30px);}
        100% {transform: translateY(0px);}
    }

    /* Stable centered container */
    .container {
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        padding-left: 20px;
        padding-right: 20px;
    }

    .card {
        background: rgba(255,255,255,0.04);
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.2s;
    }

    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 12px rgba(0,255,255,0.2);
    }



    /* Button */
    div.stButton > button {
        background: linear-gradient(90deg, #06b6d4, #3b82f6);
        color: white;
        height: 50px;
        font-size: 18px;
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="orb"></div>', unsafe_allow_html=True)

    # Title
    st.markdown(
    '<div class="gradient-text">Web Log Anomaly Detection</div>',
    unsafe_allow_html=True)


    st.markdown(
        '<div class="subtitle">Analyze web traffic logs and detect anomalous patterns using machine learning</div>',
        unsafe_allow_html=True
    )

    
    st.markdown("""
    <div style="
        max-width:800px;
        margin:auto;
        text-align:center;
    ">

    <div style="
        display:flex;
        gap:12px;
        justify-content:center;
        margin-top:25px;
        margin-bottom:20px;
    ">

    <div class="card" style="flex:1;padding:12px;">
    <div style="font-size:18px;"></div>
    <div style="font-size:15px;font-weight:600;">Log Analysis</div>
    <div style="font-size:13px;color:#9ca3af;">Upload and analyze logs</div>
    </div>

    <div class="card" style="flex:1;padding:12px;">
    <div style="font-size:18px;"></div>
    <div style="font-size:15px;font-weight:600;">Anomaly Detection</div>
    <div style="font-size:13px;color:#9ca3af;">Isolation Forest model</div>
    </div>

    <div class="card" style="flex:1;padding:12px;">
    <div style="font-size:18px;"></div>
    <div style="font-size:15px;font-weight:600;">Visual Insights</div>
    <div style="font-size:13px;color:#9ca3af;">Interactive charts</div>
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([3,2,3])

    with col2:
        if st.button("Start Analysis", use_container_width=True):

            st.session_state.started = True

            st.rerun()
    st.stop()


# ---------- Load Model ----------

# DASHBOARD VIEW
if st.session_state.started == True:

    @st.cache_resource
    def load():
        scaler = joblib.load("models/scaler.pkl")
        model = joblib.load("models/isolation_forest.pkl")
        return scaler, model

    scaler, model = load()

    st.title("Web Traffic Anomaly Detection Dashboard")
    st.markdown("""Upload a web traffic log file to analyze request patterns and identify anomalous activity.
    """)
    uploaded = st.file_uploader(
    "Select traffic log file",
    type="csv")

    if not uploaded:
        st.markdown("""
        <div style="
            padding: 25px;
            border: 1px dashed #30363d;
            border-radius: 12px;
            text-align: center;
            color: #8b949e;
            margin-top: 10px;
        ">
            Please upload a traffic log file to begin analysis
        </div>
        """, unsafe_allow_html=True)

        st.stop()

    df = pd.read_csv(uploaded)

# ---------- Data Processing ----------
    expected = list(scaler.feature_names_in_)
    for col in expected:
        if col not in df.columns:
            df[col] = 0

    if "hour" not in df.columns: df["hour"] = np.random.randint(0, 24, size=len(df))
    if "bot_ratio_per_ip" not in df.columns: df["bot_ratio_per_ip"] = np.random.random(size=len(df))
    if "error_rate_per_ip" not in df.columns: df["error_rate_per_ip"] = np.random.random(size=len(df))
    if "requests_per_ip" not in df.columns: df["requests_per_ip"] = np.random.randint(1, 1000, size=len(df))

    X_scaled = scaler.transform(df[expected])
    df["anomaly_score"] = model.decision_function(X_scaled)
    df["anomaly_label"] = model.predict(X_scaled)
    df["status"] = df["anomaly_label"].map({1: "Normal", -1: "Anomalous"})
    df["Type"] = df["bot_ratio_per_ip"].apply(lambda x: "Bot" if x > 0.5 else "Human")

    df_preview = df.copy()
    df_preview.insert(0, "Excel_Row", df_preview.index + 2)

    ip_col = [c for c in df.columns if "ip" in c.lower()][0] if any("ip" in c.lower() for c in df.columns) else "index"

    total = len(df)
    anom = (df["status"] == "Anomalous").sum()

    # ==========================================
    # MAIN LAYOUT
    # ==========================================
    left_col, right_col = st.columns([1, 2.5])

    # LEFT PANEL
    with left_col:
        st.markdown('<div class="left-panel-header"><h3>Traffic Summary</h3></div>', unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background-color: #3e1b1b; padding: 20px; border-radius: 8px; border-left: 5px solid #f85149; margin-bottom: 20px; text-align: center;">
                <p style="margin:0; color:#ff7b72; font-size: 16px; font-weight: bold; text-transform: uppercase;">Total Anomalies Detected</p>
                <h1 style="margin:0; color:white; font-size: 48px;">{anom}</h1>
                <p style="margin:0; color:#8b949e; font-size: 14px;">Out of {total:,} total requests</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### **Anomalous IP Activity**")
        unique_cols = list(dict.fromkeys([ip_col, "requests_per_ip", "error_rate_per_ip", "anomaly_score"]))
        available_cols = [c for c in unique_cols if c in df.columns]
        st.dataframe(df[df["status"]=="Anomalous"].sort_values("anomaly_score")[available_cols].head(10), use_container_width=True, hide_index=True)

    # RIGHT PANEL
    with right_col:
        st.markdown('<div class="left-panel-header"><h3>Visual Analytics</h3></div>', unsafe_allow_html=True)
        
        # -------------------- Graphs Row 1 --------------------
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            st.markdown('<span class="clean-title"> Anomaly Score Distribution</span>', unsafe_allow_html=True)
            fig1 = px.histogram(
                df, x="anomaly_score", color="status", nbins=60,
                labels={'anomaly_score': 'Anomaly Score', 'count': 'Number of IP Addresses'},
                color_discrete_map={"Normal": "#58a6ff", "Anomalous": "#f85149"}
            )
            fig1.update_yaxes(title_text="Number of IP Addresses")
            fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white", height=280, showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig1, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with r1c2:
            st.markdown('<span class="clean-title"> Bot vs Human Traffic</span>', unsafe_allow_html=True)
            bot_human_req = df.groupby("Type")["requests_per_ip"].mean().reset_index()
            fig2 = px.bar(
                bot_human_req, x="Type", y="requests_per_ip", color="Type",
                labels={'requests_per_ip': 'Average Number of Requests per IP', 'Type': 'IP Behavior Type'},
                color_discrete_map={"Human": "#58a6ff", "Bot": "#d29922"}
            )
            fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white", height=280, showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # -------------------- Graphs Row 2 --------------------
        r2c1, r2c2 = st.columns(2)
        with r2c1:
            st.markdown('<span class="clean-title"> Hourly Activity Pattern</span>', unsafe_allow_html=True)
            hourly_counts = df.groupby(["hour", "status"]).size().reset_index(name="counts")
            hourly_counts['proportion'] = hourly_counts.groupby('status')['counts'].transform(lambda x: x / x.sum())
            fig3 = px.line(
                hourly_counts, x="hour", y="proportion", color="status",
                labels={'proportion': 'Proportion of Requests per IP', 'hour': 'Hour of the Day'},
                color_discrete_map={"Normal": "#58a6ff", "Anomalous": "#f85149"}
            )
            fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white", height=280, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with r2c2:
            st.markdown('<span class="clean-title"> Error Rate Distribution</span>', unsafe_allow_html=True)
            fig4 = px.box(
                df, x="status", y="error_rate_per_ip", color="status",
                labels={'error_rate_per_ip': 'Error Rate', 'status': 'IP Behavior Type'},
                color_discrete_map={"Normal": "#58a6ff", "Anomalous": "#f85149"}
            )
            fig4.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white", height=280, showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig4, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # FULL WIDTH SECTION (Bottom)
    # ==========================================
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<span class="clean-title">Preview of Traffic Logs</span>', unsafe_allow_html=True)
    st.dataframe(df_preview.head(5), use_container_width=True, hide_index=True)

    st.markdown("<br>", unsafe_allow_html=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Download Report (.CSV)",
        data=csv,
        file_name='traffic_intelligence_report.csv',
        mime='text/csv',
        use_container_width=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)
