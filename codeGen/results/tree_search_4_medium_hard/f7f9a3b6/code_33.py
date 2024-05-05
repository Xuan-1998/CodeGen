def solve():
    n = int(input())  # Length of the message
    s = input()  # Message itself
    a = [int(x) for x in input().split()]  # Array of maximum occurrences per character

    memo = {}  # Memoization table

    def dp(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        
        if i == 0:
            return 1
        
        result = 0
        for c in set(s[:i]):
            occurrences = s[:i].count(c)
            if occurrences <= a[ord(c)-97]:
                for l in range(max(0, i-a[ord(c)-97]), i):
                    for m in range(min(j-1, max(0, (i-l)//a[ord(c)-97]))+1):
                        for n in range(min(k-1, m)):
                            if s[l:i].count(c) <= a[ord(c)-97]:
                                result += dp(l, m, n)
        
        memo[(i, j, k)] = result
        return result

    ways = 0
    longest_substring_length = 0
    min_substrings = float('inf')

    for i in range(n+1):
        for j in range(min(i//a[ord(c)-97]+1, 10**3) for c in set(s[:i])):
            for k in range(26):
                ways += dp(i, j, k)
                longest_substring_length = max(longest_substring_length, dp(n-1, min(n//a[ord(c)-97]+1, 10**3), k))
                min_substrings = min(min_substrings, dp(i, j, k))

    print(ways % (10**9 + 7))  # Number of ways to split the message
    print(longest_substring_length)  # Length of the longest substring
    print(min_substrings)  # Minimum number of substrings

if __name__ == '__main__':
    solve()
