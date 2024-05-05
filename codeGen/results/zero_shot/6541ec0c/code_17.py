import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    xor_values = {i: 0 for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if values[i] != values[j]:
                xor_values[i] ^= xor_values[j]
    seen_xor_values = set()
    for value in xor_values.values():
        if value not in seen_xor_values:
            seen_xor_values.add(value)
            print("YES" if len(seen_xor_values) == 1 else "NO")
        else:
            break
