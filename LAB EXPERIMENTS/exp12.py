grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N': [['cat'], ['dog']],
    'V': [['sees'], ['likes']]
}

def earley(words):
    n = len(words)
    chart = [set() for _ in range(n + 1)]

    start = ('S0', ('S',), 0, 0)
    chart[0].add(start)

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for state in list(chart[i]):
                lhs, rhs, dot, origin = state

                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            new_state = (symbol, tuple(rule), 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    elif i < n and symbol == words[i]:
                        new_state = (lhs, rhs, dot + 1, origin)
                        if new_state not in chart[i + 1]:
                            chart[i + 1].add(new_state)

                else:
                    for old in list(chart[origin]):
                        l, r, d, o = old

                        if d < len(r) and r[d] == lhs:
                            new_state = (l, r, d + 1, o)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    final_state = ('S0', ('S',), 1, 0)

    return final_state in chart[n]

sentence = input("Enter sentence: ").lower().split()

if earley(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")