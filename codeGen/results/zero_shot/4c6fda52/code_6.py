import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    # Initialize the count of misplaced characters
    changed = 0

    # Consider the last k-1 characters in the given string
    for i in range(k-1):
        if (i % 3 == 0 and s[i] != 'R') or \
           ((i+1) % 3 == 0 and s[i] != 'G') or \
           ((i+2) % 3 == 0 and s[i] != 'B'):
            changed += 1

    print(changed)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
