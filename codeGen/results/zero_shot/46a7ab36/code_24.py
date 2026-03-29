def alien_language(n, m):
    mod = 10**8 + 7
    res = 1
    for i in range(m):
        if i % 2 == 0:  # Case 1: letter can be placed anywhere
            res = (res * n) % mod
        else:
            res = ((res * n) % mod) * n  # Case 2: letter at last position and next letter has index >= 2*i
    return res

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
