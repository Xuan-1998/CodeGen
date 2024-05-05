n = int(input())
s = input()
a = [int(x) for x in input().split()]

ways = 0
longest = 0
min_substrs = float('inf')

for i in range(n):
    freqs = [0] * 26
    for j in range(i, n):
        c = ord(s[j]) - ord('a')
        freqs[c] += 1
        if any(freq > a[c] for freq in freqs):
            break
    else:
        ways += 1
        longest = max(longest, i + 1)
        min_substrs = min(min_substrs, (n - i) // (i + 1))

print(ways % (10**9 + 7))
print(longest)
print(min_substrs)
