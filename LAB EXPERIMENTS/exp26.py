from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator = pipeline("translation_en_to_fr", model=model, tokenizer=tokenizer)

text = "Hello, how are you? Machine learning is amazing."
result = translator(text, max_length=100)

print(f"English: {text}")
print(f"French: {result[0]['translation_text']}")

texts = ["Good morning", "I love natural language processing"]
for t in texts:
    print(f"{t} -> {translator(t)[0]['translation_text']}")