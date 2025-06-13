from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class QARetriever:
    def __init__(self, questions, answers):
        self.vectorizer = TfidfVectorizer()
        self.answers = answers
        self.question_vectors = self.vectorizer.fit_transform(questions)

    def get_best_answer(self, user_question):
        user_vec = self.vectorizer.transform([user_question])
        sims = cosine_similarity(user_vec, self.question_vectors)
        best_idx = sims.argmax()
        return self.answers.iloc[best_idx]
