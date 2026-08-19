import streamlit as st
import string

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Password Validator & Advisor",
    page_icon="🔐",
    layout="wide"
)

# =========================================================
# ORIGINAL FUNCTIONS (AS PER YOUR ORIGINAL LOGIC)
# =========================================================

def checker(pas):
    if len(pas) < 8:
        return 'Password should have at least eight characters'
    if not any(ch in string.ascii_uppercase for ch in pas):
        return 'Password must include at least one uppercase letter'
    if not any(ch in string.ascii_lowercase for ch in pas):
        return 'Password must include at least one lowercase letter'
    if not any(ch in string.digits for ch in pas):
        return 'Password must include at least one digit'
    if not any(ch in string.punctuation for ch in pas):
        return 'Password must include at least one special character'
    return 'Valid Password'


def strength(pas):
    score = 0

    conditions = [
        len(pas) >= 8,
        len(pas) >= 12,
        len(pas) >= 16,
        any(ch.isupper() for ch in pas),
        any(ch.islower() for ch in pas),
        any(ch.isdigit() for ch in pas),
        any(ch in string.punctuation for ch in pas),
        len(set(pas)) > len(pas) / 2
    ]

    score = sum(conditions)

    if score <= 2:
        return "Very Weak"
    elif score <= 4:
        return "Weak"
    elif score <= 5:
        return "Moderate"
    elif score <= 6:
        return "Strong"
    elif score <= 7:
        return "Very Strong"
    else:
        return "Excellent"


def has_repeated_characters(pas):
    for ch in set(pas):
        if pas.count(ch) >= 4:
            return True
    return False


def show_recommendations():
    return [
        "Avoid commonly used passwords.",
        "Avoid using the same character repeatedly.",
        "Avoid predictable sequences, such as 123456 or abcdef.",
        "Avoid common keyboard patterns, such as qwerty or asdfgh.",
        "Avoid using easily guessable personal information."
    ]


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
/* Base Background */
.stApp {
    background: radial-gradient(circle at 10% 10%, rgba(94, 53, 177, 0.20), transparent 30%),
                radial-gradient(circle at 90% 20%, rgba(33, 150, 243, 0.15), transparent 30%),
                #080b14;
    color: #f5f7ff;
}

/* Top padding taaki lock icon cut na ho */
.block-container {
    max-width: 1100px;
    padding-top: 80px !important;
    padding-bottom: 50px;
}

.hero {
    text-align: center;
    margin-bottom: 35px;
}

.hero-icon {
    font-size: 80px;
    line-height: 1.3;
    display: inline-block;
}

.hero-title {
    font-size: 50px;
    line-height: 1.2;
    font-weight: 800;
    color: #ffffff;
    margin-top: 10px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    margin-top: 25px;
    margin-bottom: 16px;
}

/* Password Input Label */
div[data-testid="stTextInput"] label p {
    font-size: 22px !important;
    font-weight: 600 !important;
    color: #e9edf7 !important;
    margin-bottom: 8px !important;
}

/* Input Container Box Size */
div[data-testid="stTextInput"] div[data-baseweb="input"] {
    background: #0d1322 !important;
    border: 2px solid #46506b !important;
    border-radius: 14px !important;
    min-height: 70px !important;
    height: 70px !important;
    padding: 0 14px !important;
}

/* Password Text inside Input */
div[data-testid="stTextInput"] input {
    background: transparent !important;
    color: #ffffff !important;
    font-size: 24px !important;
    font-weight: 500 !important;
    height: 100% !important;
}

/* Placeholder styling */
div[data-testid="stTextInput"] input::placeholder {
    font-size: 20px !important;
    color: #6b778f !important;
}

/* Eye toggle button */
div[data-testid="stTextInput"] button {
    transform: scale(1.35);
    margin-right: 8px;
}

/* Input focus state */
div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
    border: 2px solid #7957ff !important;
    box-shadow: 0 0 0 4px rgba(121, 87, 255, 0.25) !important;
}

/* Analyze Button */
.stButton > button {
    height: 58px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: 700;
    background: linear-gradient(90deg, #7048ff, #3287f6);
    color: white;
    border: none;
}

.stButton > button:hover {
    color: white;
    border: none;
    transform: translateY(-1px);
}

/* Result Cards */
.result-card {
    border-radius: 14px;
    padding: 24px;
    text-align: center;
    margin: 15px 0 25px 0;
}

.result-title {
    font-size: 28px;
    font-weight: 800;
}

.result-strength {
    font-size: 22px;
    margin-top: 8px;
}

/* Requirement boxes & Tips */
.requirement {
    background: #111727;
    border: 1px solid #29334a;
    border-radius: 12px;
    padding: 16px 12px;
    text-align: center;
    color: #e8edf8;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 12px;
}

.tip {
    background: #111727;
    border: 1px solid #29334a;
    border-left: 4px solid #7957ff;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 10px;
    color: #e1e7f3;
    font-size: 16px;
    line-height: 1.5;
}

.footer {
    text-align: center;
    color: #69748a;
    margin-top: 40px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# UI LAYOUT
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-icon">🔐</div>
    <div class="hero-title">Password Validator & Advisor</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Test Your Password</div>', unsafe_allow_html=True)

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type a password to test..."
)

check = st.button("🔍 Analyze Password", use_container_width=True)

if check:
    if not password:
        st.warning("Please enter a password first.")
    else:
        result = checker(password)
        st.markdown('<div class="section-title">Validation Result</div>', unsafe_allow_html=True)

        if result != "Valid Password":
            st.markdown(f"""
            <div class="result-card" style="background:#2a1115; border:1px solid #6e2630;">
                <div class="result-title">❌ Invalid Password</div>
                <div class="result-strength">{result}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            current_strength = strength(password)
            st.markdown(f"""
            <div class="result-card" style="background:#10251d; border:1px solid #1f6b4c;">
                <div class="result-title">✓ Valid Password</div>
                <div class="result-strength">Strength: <strong>{current_strength}</strong></div>
            </div>
            """, unsafe_allow_html=True)

            if has_repeated_characters(password):
                st.warning("⚠️ Warning: Password contains too many repeated characters.")
            else:
                st.success("✓ No excessive character repetition detected.")


# =========================================================
# REQUIREMENTS & TIPS
# =========================================================

st.markdown('<div class="section-title">Password Requirements</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="requirement">🔢 At least 8 characters</div>', unsafe_allow_html=True)
    st.markdown('<div class="requirement">🔡 Lowercase letter</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="requirement">🔠 Uppercase letter</div>', unsafe_allow_html=True)
    st.markdown('<div class="requirement">🔢 At least one digit</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="requirement">🔣 Special character</div>', unsafe_allow_html=True)
    st.markdown('<div class="requirement">🧩 Character variety</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">🛡️ Password Security Advisor</div>', unsafe_allow_html=True)

for number, tip in enumerate(show_recommendations(), start=1):
    st.markdown(f"""
    <div class="tip">
        <strong>{number}.</strong> {tip}
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Password Validator & Advisor • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
