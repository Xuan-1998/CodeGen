import sys
from collections import defaultdict

def dp(u, v, k):
    if u == v:
        return "YES"
    if k == 0:
        return "NO"

    dp_table = defaultdict(lambda: {"YES" for _ in range(31)})
    dp_table[u][k] = "NO"

    for w in range(2**30):
        if (u & w) == w:
            if dp_table[w][k-1].get("YES", None) is not None:
                return "YES"
    
    return "NO"


def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        print(dp(u, v, 30))


if __name__ == "__main__":
    main()
