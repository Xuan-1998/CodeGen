import sys

def min_changes(s, k):
    n = len(s)
    last_k_chars = s[-(k-1):]
    changes_needed = 0

    for i in range(n-k+1):
        if s[i:i+k] != last_k_chars:
            changes_needed += k - (i % k) + (last_k_chars.count('R') + last_k_chars.count('G'))
            break
    return changes_needed

while True:
    n, k = map(int, sys.stdin.readline().split())
    if n == 0 and k == 0:
        break
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
