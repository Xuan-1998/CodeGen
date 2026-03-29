===BEGIN CODE===
from collections import defaultdict

def max_hedgehog_beauty(n, m):
    memo = {(0, set()): 1}  # Base case: initial state with no edges
    for _ in range(m):
        edge = list(map(int, input().split()))
        tail_length = len(memo)
        visited = set()
        for (tl, v) in sorted(list(memo.items()), key=lambda x: x[0]):
            if tl < n and not (edge[0] in v or edge[1] in v):
                new_visited = v.copy()
                if edge[0] not in v:
                    new_visited.add(edge[0])
                if edge[1] not in v:
                    new_visited.add(edge[1])
                for (new_tl, new_v) in [(tl+1, new_visited)] + list(memo.items()):
                    if (new_tl, new_v) not in memo or memo[(new_tl, new_v)] < (tl+1) * (len(new_v) - len(v)):
                        memo[(new_tl, new_v)] = (tl+1) * (len(new_v) - len(v))
    return max(memo.values())

n, m = map(int, input().split())
print(max_hedgehog_beauty(n, m))
===END CODE===
