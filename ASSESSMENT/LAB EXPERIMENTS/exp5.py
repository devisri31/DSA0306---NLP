from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "running", "playing", "studies", "studying",
    "connected", "connection", "happiness",
    "flying", "wolves", "cars"
]

print("Original Word\t\tStemmed Word")
print("-" * 40)

for word in words:
    stem = stemmer.stem(word)
    print(f"{word:20}{stem}")

w = input("\nEnter a word: ")
print(f"Stemmed Word: {stemmer.stem(w)}")