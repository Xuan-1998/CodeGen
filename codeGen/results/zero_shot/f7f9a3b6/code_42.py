import sys

def solve(n, s, a):
    ways = 0
    max_length = 0
    min_substrings = n
    
    # Count the number of ways to split the string
    for i in range(len(s)):
        cur_ones = 0
        for j in range(i, len(s)):
            if ord(s[j]) - 97 > 26:
                break
            cur_ones += (a[ord(s[j]) - 97] >= 1)
            if sum(a[:ord(s[j]) - 97 + 1]) <= j - i + 1:
                ways += 1
    
    # Find the length of the longest substring
    for i in range(len(s)):
        cur_ones = 0
        max_len = 0
        for j in range(i, len(s)):
            if ord(s[j]) - 97 > 26:
                break
            cur_ones += (a[ord(s[j]) - 97] >= 1)
            max_len = max(max_len, j - i + 1)
    
    # Find the minimum number of substrings
    for i in range(len(s)):
        cur_ones = 0
        min_sub = n
        for j in range(i, len(s)):
            if ord(s[j]) - 97 > 26:
                break
            cur_ones += (a[ord(s[j]) - 97] >= 1)
            min_sub = min(min_sub, j - i + 1)
    
    print(ways % (10**9 + 7))
    print(max_length)
    print(min_substrings)

# Read input from stdin
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Call the solve function with the input values
solve(n, s, a)
