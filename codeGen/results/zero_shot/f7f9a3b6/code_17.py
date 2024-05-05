n = int(input())
s = input()
a = [int(x) for x in input().split()]

num_ways = 0
longest_substring_length = 0
min_substrings = float('inf')

for i in range(n):
    for j in range(26):  
        if s[i].ord() - ord('a') == j:  
            if i < a[j]:  
                continue
            else:
                break
    else:
        num_ways += 1
        longest_substring_length = max(longest_substring_length, i + 1)

min_substrings = min(min_substrings, n // sum(a))

print(num_ways % (10**9 + 7))
print(longest_substring_length)
print(min_substrings)
