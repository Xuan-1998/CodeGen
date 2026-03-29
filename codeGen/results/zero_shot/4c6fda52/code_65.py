import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    # Preprocess the first k-1 characters
    freq = {'R': 0, 'G': 0, 'B': 0}
    for i in range(k-1):
        c = s[i]
        freq[c] += 1

    # Iterate through the rest of the string
    total_changes = 0
    for i in range(k-1, n):
        c = s[i]
        ideal_freq = {'R': (i // 3) % 3, 'G': (i // 3 + 1) % 3, 'B': (i // 3 + 2) % 3}[c]
        total_changes += abs(freq[c] - ideal_freq)

    print(total_changes)

solve()
