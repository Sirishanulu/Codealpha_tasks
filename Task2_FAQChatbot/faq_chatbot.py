import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 70px;
    font-weight: bold;
    color: #4F8BF9;
    margin-bottom: 0px;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: gray;
    margin-top: -15px;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# FAQ DATASET
# -----------------------------
faq_data = {
    "What is Artificial Intelligence?":
    "Artificial Intelligence (AI) enables machines to perform tasks that normally require human intelligence.",

    "What is Machine Learning?":
    "Machine Learning is a subset of AI that allows systems to learn from data and improve automatically.",

    "What is Deep Learning?":
    "Deep Learning is an advanced branch of Machine Learning that uses neural networks with multiple layers.",

    "What is Python?":
    "Python is a popular programming language used in AI, Data Science, Web Development, and Automation.",

    "What is Natural Language Processing?":
    "Natural Language Processing (NLP) helps computers understand, analyze, and generate human language.",

    "What are the applications of AI?":
    "AI is used in healthcare, finance, education, robotics, recommendation systems, and self-driving vehicles.",

    "Why is Python popular for AI?":
    "Python is easy to learn and has powerful libraries such as NumPy, Pandas, TensorFlow, and Scikit-learn.",

    "What is Data Science?":
    "Data Science is the process of collecting, analyzing, and interpreting data to gain useful insights.",

    "What is Computer Vision?":
    "Computer Vision enables computers to understand and analyze images and videos.",

    "What is Generative AI?":
    "Generative AI creates new content such as text, images, audio, and code.",

    "What is ChatGPT?":
    "ChatGPT is an AI chatbot developed by OpenAI that can answer questions and generate text.",

    "What is a Neural Network?":
    "A Neural Network is a system inspired by the human brain used in Machine Learning.",

    "What is Robotics?":
    "Robotics combines AI, engineering, and automation to build intelligent machines."
}

# -----------------------------
# PREPROCESSING
# -----------------------------
def preprocess(text):
    return text.lower().strip()

questions = list(faq_data.keys())
answers = list(faq_data.values())

processed_questions = [preprocess(q) for q in questions]

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📚 FAQ Topics")

for q in questions:
    st.sidebar.write("•", q)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<p class="main-title">🤖 AI FAQ Chatbot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Smart Answers • Instant Learning • Powered by NLP</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

# -----------------------------
# USER INPUT
# -----------------------------
user_question = st.chat_input("Ask your question here...")

if user_question:

    with st.chat_message("user"):
        st.write(user_question)

    processed_user_question = preprocess(user_question)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        processed_questions + [processed_user_question]
    )

    similarity_scores = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    best_match_index = similarity_scores.argmax()
    confidence_score = similarity_scores[0][best_match_index]

    if confidence_score > 0.20:

        answer = answers[best_match_index]

        response = (
            f"{answer}\n\n"
            f"📊 Match Confidence: {confidence_score * 100:.1f}%"
        )

    else:

        response = (
            "❌ Sorry, I couldn't find a relevant answer.\n\n"
            "Try asking about AI, Machine Learning, Python, NLP, Data Science, Robotics, or ChatGPT."
        )

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.chat_history.append(("user", user_question))
    st.session_state.chat_history.append(("assistant", response))

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    '<p class="footer">🚀 Developed for CodeAlpha Artificial Intelligence Internship</p>',
    unsafe_allow_html=True
)