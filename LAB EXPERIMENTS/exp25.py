import openai

openai.api_key = "YOUR_API_KEY_HERE"

prompt = "Write a short story about a robot learning NLP."

try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    print(response.choices[0].text.strip())
except:
    print("GPT-3 API Example (without key):")
    print(f"Prompt: {prompt}")
    print("Response: The robot started learning NLP. It read thousands of sentences, understood grammar, entities and meanings. Soon it could chat with humans...")

# NEW OpenAI library (v1+) version:
"""
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY_HERE")
res = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}]
)
print(res.choices[0].message.content)
"""