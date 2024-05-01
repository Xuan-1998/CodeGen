from collections import defaultdict

DP_state = ({}, defaultdict(set))  # base case

for i in range(N):
    for s, subset in DP_state[1].items():
        new_s = set(subset) | {a[i]}
        if not(new_s in DP_state[0]):
            DP_state[0].add(frozenset(new_s))
            DP_state[1][frozenset(new_s)] = subset | {a[i]}

for s in list(DP_state[0]):  # convert to list for removal
    for i in range(N):
        new_s = set(s) - {a[i]}
        if not(new_s in DP_state[0]):
            DP_state[0].remove(frozenset(s))
            DP_state[1][frozenset(s)].update({a[i]})
        else:
            break
    else:
        DP_state[0].remove(frozenset(s))

DP_state = DP_state[1]
