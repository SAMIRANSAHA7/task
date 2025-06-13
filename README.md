# 🩺 MedQuAD Medical Q&A Chatbot

This chatbot uses the MedQuAD dataset to answer medical questions using TF-IDF retrieval and basic NER (Named Entity Recognition).

## 🚀 Setup

```bash
pip install -r code/requirements.txt
python -m spacy download en_core_web_sm
cd code
python downloader.py
streamlit run app.py
```

Dataset: [MedQuAD on GitHub](https://github.com/abachaa/MedQuAD)
