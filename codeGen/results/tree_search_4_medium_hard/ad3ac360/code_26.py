def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

n = int(input())  # Read the length of the string from stdin
s = input()       # Read the string itself from stdin

dp = [float('inf')] * n
dp[0] = 0  # Base case: an empty string has no cuts needed

for i in range(n):
    for j in range(i, n):
        if isPalindrome(s, i, j) and (j - i < 2 or dp[j - i - 1]):
            dp[j - i] = min(dp[j - i], dp[i - 1] + 1 if i > 0 else 1)

print(min(dp))  # Print the minimum number of cuts needed
