# Step 2: Initialize variables
ans = 0
max_len = 0
min_substrings = float('inf')

for i in range(n):
    for j in range(i+1, n+1):
        if all(s[k-(j-i-1)] <= a[ord(s[k-(j-i)]) - ord('a')] for k in range(i, j)):
            # Check condition
            if sum(ord(c) - ord('a') for c in set(s[i:j])) == 26:
                ans += 1
                max_len = max(max_len, j - i)
                min_substrings = min(min_substrings, (j-i)//sum(a))

print(ans % (10**9 + 7))
print(max_len)
print(min_substrings)
