import sys
from functools import lru_cache

@lru_cache(None)
def update_state(i, a, b):
    return (i-1, a^(b>>i), b<<1)

def solve():
    a, b = map(int, input().split())
    modulo = 10**9 + 7
    total_xor = 0

    for i in range(31):
        if i >= len(bin(a)) and i >= len(bin(b)):
            break
        state = update_state(i, a, b)
        total_xor += state[1]
        a, b = state

    print(total_xor % modulo)

if __name__ == "__main__":
    solve()
