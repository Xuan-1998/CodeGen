code
k = int(input())
s = input().strip()

# If k is equal to n, we can just return s
if k == len(s):
    print(s[:k])
else:
    # Duplicating the string and removing the last character if necessary
    duplicated_s = s + s[:-1]
    # Finding the lexicographically smallest substring of length k
    min_substring = min(duplicated_s, key=len)
    
    print(min_substring)
