from collections import defaultdict

def partition_palindromic(S):
    statespace = defaultdict(set)
    statespace[(0, S[0], [])].add([[]])
    
    for i in range(len(S)):
        for (j, remaining, partition) in [(i, S[:i+1], state) for state in statespace[(0, S[0], [])] for i in range(len(state[-1]))]:
            if j < len(remaining):
                for k in range(j+1):
                    if remaining[k:j+1] == remaining[k:j+1][::-1]:
                        statespace[(j, remaining[:k]+remaining[j:], partition + [remaining[k:j+1]]]).update([p + [remaining[k:j+1]] for p in state])
    
    return [{partition} for state in statespace.values() for partition in state]
