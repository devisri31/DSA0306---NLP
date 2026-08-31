grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N': [['cat'], ['dog']],
    'V': [['sees'], ['likes']]
}

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and symbol == words[pos]:
            return pos + 1
        return None

    for rule in grammar[symbol]:
        current = pos
        success = True

        for s in rule:
            result = parse(s, words, current)
            if result is None:
                success = False
                break
            current = result

        if success:
            return current

    return None

sentence = input("Enter sentence: ").lower().split()

result = parse('S', sentence, 0)

if result == len(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")