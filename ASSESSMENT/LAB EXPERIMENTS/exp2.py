def fsa_ends_with_ab(s):
    state = 0
    for ch in s:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0
    return state == 2

string = input("Enter string: ")
if fsa_ends_with_ab(string):
    print("Accepted - String ends with 'ab'")
else:
    print("Rejected - String does not end with 'ab'")