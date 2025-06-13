import streamlit as st
from preprocess import load_medquad_xml
from qa_retrieval import QARetriever
from med_entity_ner import extract_entities

st.set_page_config(page_title="Medical Q&A Chatbot", layout="wide")
st.title("🩺 Medical Q&A Chatbot using MedQuAD")

data_path = "../data/MedQuAD-master"
df = load_medquad_xml(data_path)

st.write(f"Loaded {len(df)} Q&A pairs.")

if df.empty:
    st.error("No data loaded. Check the dataset path.")
else:
    retriever = QARetriever(df['question'], df['answer'])

    question = st.text_input("Ask a medical question:")
    if question:
        answer = retriever.get_best_answer(question)
        st.subheader("Answer:")
        st.write(answer)

        st.subheader("Recognized Medical Entities:")
        entities = extract_entities(question)
        if entities:
            for ent, label in entities:
                st.write(f"- **{ent}** ({label})")
        else:
            st.write("No entities found.")
