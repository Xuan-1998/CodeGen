from collections import defaultdict
from functools import lru_cache

def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    memo = defaultdict(lambda: [float('inf'), float('-inf')])

    @lru_cache(None)
    def transition(x, y):
        if x <= 0 or x > n:
            return -1
        next_y = y + seq[x-1]
        next_x = x - seq[x-1]
        memo[(x, y)] = [next_x, next_y]
        return next_y

    for i in range(2, n+1):
        curr_state = (i, 0)
        while curr_state[0] > 0:
            curr_state = memo[curr_state][:]
        print(curr_state[1])

if __name__ == "__main__":
    solve()
