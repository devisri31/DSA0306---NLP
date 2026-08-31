import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

text1 = "Machine learning is a field of AI. It uses algorithms to learn from data. These algorithms improve with experience."
text2 = "Machine learning is a field of AI. The cat sat on the mat. Algorithms improve with experience."

def coherence_score(text):
    doc = nlp(text)
    sents = [s.text for s in doc.sents]
    if len(sents) < 2:
        return 0
    vec = TfidfVectorizer().fit_transform(sents)
    sims = cosine_similarity(vec)
    score = 0
    count = 0
    for i in range(len(sents)-1):
        score += sims[i][i+1]
        count += 1
    return score / count if count>0 else 0

print(f"Coherent Text Score: {coherence_score(text1):.4f}")
print(f"Incoherent Text Score: {coherence_score(text2):.4f}")

if coherence_score(text1) > 0.2:
    print("Text1: Coherent")
else:
    print("Text1: Incoherent")