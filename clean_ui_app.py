from __future__ import annotations

import hashlib
import hmac
import math
import secrets
import sqlite3
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Loyola CS Digital Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

DB_PATH = Path(__file__).with_name("clean_ui_users.db")

TOPICS = [
    "Faculty",
    "Fees",
    "Courses",
    "Library",
    "Hostel",
    "Admission",
    "Principal",
    "HOD",
    "Scholarships",
    "Creator",
    "Vice Principal",
    "Student Achievements",
]

QUICK_LINKS = [
    ("Admissions", "admission"),
    ("Fee Structure", "fee structure"),
    ("Faculty Team", "faculty"),
    ("Scholarships", "scholarships"),
    ("Principal", "principal"),
    ("Student Achievements", "student achievements"),
]


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Fraunces:wght@600;700&display=swap');

        :root {
            --page-bg: radial-gradient(circle at top left, #eff8f0 0%, #f7f3ea 48%, #e2ece4 100%);
            --panel: rgba(255, 255, 255, 0.82);
            --panel-strong: rgba(255, 255, 255, 0.96);
            --border: rgba(22, 92, 58, 0.14);
            --text: #173126;
            --muted: #51685c;
            --brand: #1f6a46;
            --brand-deep: #12442d;
            --accent: #d8a93a;
            --shadow: 0 18px 45px rgba(18, 68, 45, 0.10);
        }

        html, body, [class*="css"] {
            font-family: 'Manrope', sans-serif;
            color: var(--text);
            margin: 0 !important;
            padding: 0 !important;
        }

        .stApp {
            background: var(--page-bg);
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stHeader"] {
            background: transparent;
            height: 0 !important;
            min-height: 0 !important;
            display: none !important;
        }

        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"] {
            display: none !important;
        }

        footer {
            display: none !important;
        }

        header {
            display: none !important;
        }

        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            margin-top: 0 !important;
            max-width: 100% !important;
        }

        [data-testid="stAppViewContainer"] {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        [data-testid="stAppViewContainer"] > .main {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        [data-testid="stAppViewContainer"] > .main > div {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(16, 66, 44, 0.96), rgba(12, 47, 33, 0.98));
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        [data-testid="stSidebar"] * {
            color: #f4f7f2 !important;
        }

        .hero-card, .login-card, .content-card, .feature-card {
            background: var(--panel);
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            backdrop-filter: blur(10px);
        }

        .hero-card {
            padding: 1.8rem 2rem;
            border-radius: 28px;
            margin-bottom: 1.1rem;
            background:
                linear-gradient(135deg, rgba(230, 242, 233, 0.98), rgba(248, 238, 214, 0.98)),
                linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.88));
            color: #111111;
        }

        .hero-title {
            font-family: 'Fraunces', serif;
            font-size: 2.4rem;
            line-height: 1.1;
            margin-bottom: 0.45rem;
        }

        .hero-copy {
            font-size: 1rem;
            max-width: 760px;
            color: #1f1f1f;
        }

        .feature-card, .content-card {
            border-radius: 24px;
            padding: 1rem 1.1rem;
            margin-bottom: 1rem;
        }

        .feature-title {
            font-weight: 800;
            color: var(--brand-deep);
            margin-bottom: 0.2rem;
        }

        .feature-copy {
            color: var(--muted);
            font-size: 0.95rem;
            margin: 0;
        }

        .login-shell {
    min-height: auto !important;   /* 🔥 remove forced height */
    display: block !important;     /* 🔥 remove vertical centering */
    padding: 0 !important;         /* 🔥 remove spacing */
    margin: 0 !important;
        }

        .login-grid {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 1.4rem;
            width: min(1180px, 100%);
            margin: 0 auto;
        }

        .login-showcase {
            position: relative;
            overflow: hidden;
            min-height: 640px;
            padding: 2.2rem;
            border-radius: 34px;
            border: 1px solid rgba(18, 68, 45, 0.10);
            background:
                radial-gradient(circle at top right, rgba(216, 169, 58, 0.28), transparent 28%),
                radial-gradient(circle at bottom left, rgba(31, 106, 70, 0.20), transparent 35%),
                linear-gradient(145deg, rgba(255,255,255,0.92), rgba(243, 248, 243, 0.88));
            box-shadow: var(--shadow);
        }

        .login-showcase::before {
            content: "";
            position: absolute;
            inset: auto -90px -110px auto;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            background: rgba(31, 106, 70, 0.10);
            filter: blur(3px);
        }

        .login-card {
            max-width: 100%;
            padding: 1.8rem;
            border-radius: 34px;
            background: rgba(255,255,255,0.95);
            border: 1px solid rgba(18, 68, 45, 0.10);
            box-shadow: var(--shadow);
        }

        .eyebrow {
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.18em;
            color: var(--brand);
            font-weight: 800;
        }

        .login-title {
            font-family: 'Fraunces', serif;
            font-size: 2rem;
            margin: 0.25rem 0 0.5rem;
            color: var(--brand-deep);
        }

        .muted {
            color: var(--muted);
            margin-bottom: 1rem;
        }

        .showcase-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.48rem 0.9rem;
            border-radius: 999px;
            background: rgba(31, 106, 70, 0.08);
            border: 1px solid rgba(31, 106, 70, 0.10);
            color: var(--brand-deep);
            font-size: 0.84rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 1.1rem;
        }

        .showcase-title {
            font-family: 'Fraunces', serif;
            font-size: 3rem;
            line-height: 1.02;
            color: #111111;
            max-width: 620px;
            margin-bottom: 1rem;
        }

        .showcase-copy {
            max-width: 600px;
            color: #2e3f36;
            font-size: 1.03rem;
            line-height: 1.7;
            margin-bottom: 1.4rem;
        }

        .showcase-chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }

        .showcase-chip {
            padding: 0.72rem 0.95rem;
            border-radius: 18px;
            background: rgba(255,255,255,0.74);
            border: 1px solid rgba(18, 68, 45, 0.10);
            color: #111111;
            font-weight: 700;
            font-size: 0.92rem;
        }

        .showcase-metrics {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
            margin-top: 1rem;
        }

        .showcase-metric {
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(18, 68, 45, 0.10);
            border-radius: 22px;
            padding: 1rem;
        }

        .showcase-metric strong {
            display: block;
            font-size: 1.4rem;
            color: #111111;
            margin-bottom: 0.2rem;
        }

        .showcase-metric span {
            color: #3a4f44;
            font-size: 0.9rem;
        }

        .login-card-head {
            margin-bottom: 1rem;
        }

        .auth-badge {
            display: inline-block;
            padding: 0.38rem 0.75rem;
            border-radius: 999px;
            background: rgba(216, 169, 58, 0.16);
            color: #6b4b00;
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }

        .auth-title {
            font-family: 'Fraunces', serif;
            font-size: 2rem;
            color: #111111;
            margin-bottom: 0.45rem;
        }

        .auth-copy {
            color: #4f5f56;
            font-size: 0.98rem;
            line-height: 1.6;
            margin-bottom: 1.15rem;
        }

        .auth-panel {
            margin-top: 0.35rem;
        }

        [data-testid="stForm"] {
            background: transparent;
            border: none;
            padding: 0;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.6rem;
            margin-bottom: 1rem;
        }

        .stTabs [data-baseweb="tab"] {
            background: rgba(244, 247, 244, 1);
            border: 1px solid rgba(18, 68, 45, 0.08);
            border-radius: 14px;
            padding: 0.6rem 1rem;
            color: #22372d;
            font-weight: 700;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(31,106,70,0.12), rgba(216,169,58,0.18));
            color: #111111 !important;
        }

        .stat-band {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
            margin-top: 1.2rem;
        }

        .stat-pill {
            background: rgba(255,255,255,0.85);
            border: 1px solid rgba(22, 92, 58, 0.10);
            border-radius: 18px;
            padding: 0.8rem 0.9rem;
            color: #111111;
        }

        .stat-pill strong {
            display: block;
            font-size: 1.1rem;
        }

        .section-title {
            font-family: 'Fraunces', serif;
            color: var(--brand-deep);
            margin-bottom: 0.8rem;
        }

        .stChatMessage {
            background: var(--panel-strong);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 0.8rem 1rem;
            box-shadow: 0 10px 24px rgba(16, 66, 44, 0.05);
        }

        .stTextInput input, .stChatInput input {
            border-radius: 14px !important;
            border: 1px solid rgba(31, 106, 70, 0.18) !important;
            color: #111111 !important;
            background: rgba(255,255,255,0.96) !important;
        }

        .stTextInput label, .stChatInput label, .stMarkdown, p, li, span, div {
            color: var(--text);
        }

        .stButton > button {
            border-radius: 14px;
            border: 1px solid rgba(31, 106, 70, 0.18);
            background: linear-gradient(135deg, #1f6a46, #2f845d);
            color: white;
            font-weight: 700;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 8px 18px rgba(31, 106, 70, 0.18);
        }

        .sidebar-note {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 0.9rem;
            font-size: 0.92rem;
        }

        @media (max-width: 900px) {
            .login-grid {
                grid-template-columns: 1fr;
            }

            .login-showcase {
                min-height: auto;
            }

            .showcase-title {
                font-size: 2.2rem;
            }

            .showcase-metrics {
                grid-template-columns: 1fr;
            }

            .hero-title {
                font-size: 1.8rem;
            }

            .stat-band {
                grid-template-columns: 1fr;
            }
        
}
        </style>
        """,
        unsafe_allow_html=True,
    )


def load_chatbot_core() -> tuple[dict, callable]:
    app_source = Path(__file__).with_name("app.py").read_text(encoding="utf-8", errors="ignore")
    start = app_source.index("# DATA")
    end = app_source.index("# CHAT MEMORY")
    namespace = {"math": math}
    exec(app_source[start:end], namespace)
    return namespace["study_notes"], namespace["get_answer"]


def get_db_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def hash_password(password: str, salt: str | None = None) -> tuple[str, str]:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100_000)
    return salt, digest.hex()


def init_database() -> None:
    with get_db_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                full_name TEXT NOT NULL,
                salt TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        connection.commit()

    seed_user("loyola", "Loyola Admin", "loyola123")
    seed_user("student", "Student User", "loyola123")


def seed_user(username: str, full_name: str, password: str) -> None:
    username = username.strip().lower()
    with get_db_connection() as connection:
        existing = connection.execute(
            "SELECT 1 FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        if existing:
            return
        salt, password_hash = hash_password(password)
        connection.execute(
            "INSERT INTO users (username, full_name, salt, password_hash) VALUES (?, ?, ?, ?)",
            (username, full_name.strip(), salt, password_hash),
        )
        connection.commit()


def create_user(username: str, full_name: str, password: str) -> tuple[bool, str]:
    username = username.strip().lower()
    full_name = full_name.strip()

    if len(username) < 3:
        return False, "Username must be at least 3 characters."
    if len(full_name) < 2:
        return False, "Full name must be at least 2 characters."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    with get_db_connection() as connection:
        existing = connection.execute(
            "SELECT 1 FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        if existing:
            return False, "Username already exists."

        salt, password_hash = hash_password(password)
        connection.execute(
            "INSERT INTO users (username, full_name, salt, password_hash) VALUES (?, ?, ?, ?)",
            (username, full_name, salt, password_hash),
        )
        connection.commit()
    return True, "Signup successful. You can now log in."


def verify_login(username: str, password: str) -> tuple[bool, str | None]:
    username = username.strip().lower()
    with get_db_connection() as connection:
        user = connection.execute(
            "SELECT username, full_name, salt, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    if not user:
        return False, None

    _, digest = hash_password(password, user["salt"])
    if hmac.compare_digest(digest, user["password_hash"]):
        return True, user["full_name"]
    return False, None


def get_images_for_prompt(prompt: str) -> tuple[list[str], int]:
    text = prompt.lower()
    width = 160

    if "hod" in text:
        return ["ramana.jpg"], width
    if "faculty" in text:
        return ["samuel.jpg", "sujith.jpg", "karthik.jpg", "himaja.jpg"], width
    if "principal" in text:
        return ["joji.jpg"], width
    if "creator" in text or "who created you" in text:
        return ["suhel.jpg"], width
    if "vana father" in text or "vice principal" in text:
        return ["vana.jpg"], width
    if "sujitha" in text:
        return ["sujitha.jpg"], width
    if "student achievements" in text:
        return ["achievement.jpg", "physics.jpg"], 620
    return [], width


def init_state() -> None:
    init_database()
    st.session_state.setdefault("clean_logged_in", False)
    st.session_state.setdefault("clean_messages", [])
    st.session_state.setdefault("failed_attempts", 0)
    st.session_state.setdefault("quick_question", "")
    st.session_state.setdefault("current_user", "")


def render_login() -> None:
    st.markdown('<div class="login-shell">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="login-grid">
            <div class="login-showcase">
                <div class="showcase-kicker">Campus Portal Experience</div>
                <div class="showcase-title">A smarter front door for your Loyola assistant</div>
                <p class="showcase-copy">
                    Sign in through a polished student portal that feels modern, trustworthy, and
                    easy to use. The new design keeps your chatbot logic safe in the background
                    while presenting a cleaner experience in the foreground.
                </p>
                <div class="showcase-chip-row">
                    <div class="showcase-chip">Professional landing layout</div>
                    <div class="showcase-chip">Database login and signup</div>
                    <div class="showcase-chip">Original chatbot code preserved</div>
                </div>
                <div class="showcase-metrics">
                    <div class="showcase-metric">
                        <strong>24/7</strong>
                        <span>Instant access to admissions, fees, and faculty details</span>
                    </div>
                    <div class="showcase-metric">
                        <strong>Secure</strong>
                        <span>Passwords are stored as hashes inside a local SQLite database</span>
                    </div>
                    <div class="showcase-metric">
                        <strong>Creative</strong>
                        <span>Custom glassmorphism panels with a more premium visual style</span>
                    </div>
                </div>
            </div>
            <div class="login-card">
                <div class="login-card-head">
                    <div class="auth-badge">Student Access</div>
                    <div class="auth-title">Welcome back</div>
                    <p class="auth-copy">
                        Log in to continue chatting with the Loyola CS Digital Assistant,
                        or create a new account to get started in a few seconds.
                    </p>
                </div>
                <div class="auth-panel">
        """,
        unsafe_allow_html=True,
    )

    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

    with login_tab:
        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submit = st.form_submit_button("Login")

        if submit:
            is_valid, full_name = verify_login(username, password)
            if is_valid:
                st.session_state.clean_logged_in = True
                st.session_state.current_user = full_name or username.strip()
                st.session_state.failed_attempts = 0
                st.success("Login successful.")
                st.rerun()
            st.session_state.failed_attempts += 1
            st.error("Invalid username or password.")

    with signup_tab:
        with st.form("signup_form", clear_on_submit=True):
            full_name = st.text_input("Full Name", placeholder="Enter your full name")
            new_username = st.text_input("New Username", placeholder="Choose a username")
            new_password = st.text_input("New Password", type="password", placeholder="Create a password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")
            signup = st.form_submit_button("Create Account")

        if signup:
            if new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                created, message = create_user(new_username, full_name, new_password)
                if created:
                    st.success(message)
                else:
                    st.error(message)

    if st.session_state.failed_attempts:
        st.info(f"Failed attempts: {st.session_state.failed_attempts}")

    st.markdown(
        """
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("## Loyola Assistant")
        if st.session_state.current_user:
            st.markdown(f"Logged in as: **{st.session_state.current_user}**")
        st.markdown(
            """
            <div class="sidebar-note">
                Ask about admissions, faculty, fees, scholarships, library timings, and
                department information from one place.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")

        if st.button("Clear chat", use_container_width=True):
            st.session_state.clean_messages = []
            st.rerun()

        if st.button("Logout", use_container_width=True):
            st.session_state.clean_logged_in = False
            st.session_state.clean_messages = []
            st.session_state.current_user = ""
            st.rerun()

        st.markdown("### Quick Topics")
        for topic in TOPICS:
            if st.button(topic, use_container_width=True, key=f"topic_{topic}"):
                st.session_state.quick_question = topic.lower()


def render_header() -> None:
    logo_col, text_col = st.columns([1, 8], vertical_alignment="center")
    with logo_col:
        st.image("loyola_logo.png", width=80)
    with text_col:
        st.markdown(
            """
            <div class="hero-card">
                    <div class="hero-title">Campus help, redesigned for clarity</div>
                <div class="hero-copy">
                    This version keeps your existing chatbot knowledge intact and wraps it in a
                    cleaner, more modern interface with a database-backed login and signup experience.
                </div>
                <div class="stat-band">
                    <div class="stat-pill"><strong>12+</strong> Quick campus topics</div>
                    <div class="stat-pill"><strong>Secure</strong> SQLite login and signup</div>
                    <div class="stat-pill"><strong>Safe</strong> Original code untouched</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_feature_cards() -> None:
    cols = st.columns(3)
    cards = [
        ("Cleaner look", "Soft glass panels, improved spacing, and a student-friendly landing view."),
        ("Better login", "Users can now sign up and log in through a local SQLite database."),
        ("Same knowledge", "Answers still come from your existing program data loaded directly from app.py."),
    ]
    for col, (title, copy) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-title">{title}</div>
                    <p class="feature-copy">{copy}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_quick_links() -> None:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="section-title">Popular Questions</h3>', unsafe_allow_html=True)
    cols = st.columns(len(QUICK_LINKS))
    for col, (label, value) in zip(cols, QUICK_LINKS):
        with col:
            if st.button(label, use_container_width=True, key=f"quick_{value}"):
                st.session_state.quick_question = value
    st.markdown("</div>", unsafe_allow_html=True)


def main() -> None:
    apply_theme()
    init_state()

    if not st.session_state.clean_logged_in:
        render_login()
        return

    study_notes, get_answer = load_chatbot_core()
    _ = study_notes

    render_sidebar()
    render_header()
    render_feature_cards()
    render_quick_links()

    if not st.session_state.clean_messages:
        st.session_state.clean_messages.append(
            {
                "role": "assistant",
                "content": "Hello! I am your Loyola college assistant. Ask me about fees, faculty, admissions, scholarships, or courses.",
                "images": [],
            }
        )

    for msg in st.session_state.clean_messages:
        with st.chat_message(msg["role"]):
            for img in msg.get("images", []):
                width = msg.get("image_width", 160)
                if Path(img).exists():
                    st.image(img, width=width)
            st.markdown(msg["content"], unsafe_allow_html=True)

    user_input = st.chat_input("Ask anything about your college...")
    if st.session_state.quick_question:
        user_input = st.session_state.quick_question
        st.session_state.quick_question = ""

    if not user_input:
        return

    st.session_state.clean_messages.append(
        {"role": "user", "content": user_input, "images": []}
    )
    with st.chat_message("user"):
        st.write(user_input)

    answer = get_answer(user_input)
    images, width = get_images_for_prompt(user_input)

    assistant_message = {
        "role": "assistant",
        "content": answer,
        "images": images,
        "image_width": width,
    }
    st.session_state.clean_messages.append(assistant_message)

    with st.chat_message("assistant"):
        for img in images:
            if Path(img).exists():
                st.image(img, width=width)
        st.markdown(answer, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
