import sys

def solve():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        s = input()
        changed_count = 0
        for i in range(n - k + 1):
            if (s[i] == 'R' and sum(s[i:i+k].count(c) for c in ['G', 'B'])) < 2:
                changed_count += 1
        print(changed_count)

if __name__ == "__main__":
    solve()
