===BEGIN SOLUTION===
from collections import defaultdict

states = defaultdict(lambda: None)
for i in range(len(input())):
    state = (i % 2 == 0, s[i] == 'B')
    next_state = states[state]
    if not next_state:
        states[state] = state
    else:
        if next_state[0]:
            if input()[next_state[1]:next_state[1]+2] in ['AB', 'BA']:
                print("YES")
                exit()
        elif not next_state[0]:
            if input()[next_state[1]:next_state[1]+2] in ['AB', 'BA']:
                print("YES")
                exit()

print("NO")
===END SOLUTION===
