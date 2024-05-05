from functools import lru_cache
from typing import Set, Dict

def can_form_polygon(n: int, moods: List[int]) -> str:
    @lru_cache(None)
    def dp(i: int, s: Set[int]) -> bool:
        if i == n - 1:
            return len(s) == n - 1
        if i < 0 or i >= n:
            return False
        if moods[i] == 1 and i in s:
            return any(dp(i-1, s | {j}) for j in range(n) if j not in s)
        else:
            return dp(i - 1, s)

    return 'YES' if dp(n - 1, set()) else 'NO'

n = int(input())
moods = list(map(int, input().split()))
print(can_form_polygon(n, moods))
