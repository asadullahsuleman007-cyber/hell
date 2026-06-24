import streamlit as st

st.title("🎓 AI Study Assistant")

user_input = st.text_area("Ask a question or paste notes")

if st.button("Generate"):
    if user_input:
        st.subheader("Summary")
        st.write(user_input[:200] + "...")

        st.subheader("Quiz")
        st.write("1. What is the main topic?")
        st.write("2. Explain the key concept.")
        st.write("3. Give one example.")
