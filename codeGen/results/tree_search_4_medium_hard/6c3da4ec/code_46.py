dp = {}
def dp(i):
    if i in dp:
        return dp[i]
    max_or = 0
    for j in range(1, i+1):  # Consider all possible lengths of the first substring
        for k in range(j+1, i+1):  # and all possible lengths of the second substring
            start = s[:j]  # Common prefix
            end = s[k-1:]  # Second substring (excluding the common prefix)
            bitwise_or = int(start, 2) | int(end, 2)
            dp[(j, k)] = bitwise_or
            max_or = max(max_or, bitwise_or)
    return max_or

n = int(input())  # Read input
s = input()  # Read binary string

print(dp(n))  # Print the maximum possible value in binary representation without leading zeroes.
