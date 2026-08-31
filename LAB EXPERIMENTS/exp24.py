def dialog_act(utterance):
    u = utterance.lower()
    if "?" in u or u.startswith(("what","where","when","who","why","how","can","could","would","is","are","do")):
        return "Question"
    elif u.startswith(("hi","hello","hey","greetings")):
        return "Greeting"
    elif u.startswith(("thanks","thank you","appreciate")):
        return "Thanking"
    elif u.startswith(("bye","goodbye","see you")):
        return "Farewell"
    elif u.startswith(("yes","yeah","sure","okay","please")):
        return "Agreement"
    elif u.startswith(("no","not","never")):
        return "Disagreement"
    elif "!" in u or u.startswith(("wow","great","amazing")):
        return "Exclamation"
    else:
        return "Statement"

dialog = [
    "Hello there!",
    "What is your name?",
    "My name is John",
    "Can you help me with NLP?",
    "Sure, I can help you",
    "Thanks a lot",
    "Bye, see you later"
]

print("DIALOG ACT RECOGNITION")
for utt in dialog:
    print(f"{utt:<30} -> {dialog_act(utt)}")