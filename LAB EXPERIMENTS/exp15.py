grammar = {
    'S': [
        (['NP', 'VP'], 1.0)
    ],
    'NP': [
        (['Det', 'N'], 0.6),
        (['N'], 0.4)
    ],
    'VP': [
        (['V', 'NP'], 0.7),
        (['V'], 0.3)
    ],
    'Det': [
        (['the'], 0.5),
        (['a'], 0.5)
    ],
    'N': [
        (['cat'], 0.5),
        (['dog'], 0.5)
    ],
    'V': [
        (['sees'], 0.5),
        (['likes'], 0.5)
    ]
}

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and symbol == words[pos]:
            return pos + 1, 1.0
        return None, 0

    best_pos = None
    best_prob = 0

    for rule, probability in grammar[symbol]:
        current = pos
        prob = probability
        valid = True

        for s in rule:
            result, p = parse(s, words, current)

            if result is None:
                valid = False
                break

            current = result
            prob *= p

        if valid and prob > best_prob:
            best_pos = current
            best_prob = prob

    return best_pos, best_prob

sentence = input("Enter sentence: ").lower().split()

pos, probability = parse('S', sentence, 0)

if pos == len(sentence):
    print("Sentence accepted")
    print("Probability:", probability)
else:
    print("Sentence rejected")