import sys

def solve():
    n = int(input())
    s = input()
    max_occurrences = [int(x) for x in input().split()]

    dp = [[True] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            if s[j:i+1].isalpha() and i - j + 1 <= max_occurrences[ord(s[j].lower()) - 97]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]*max_occurrences[ord(s[j].lower()) - 97])
            else:
                dp[i][j] = False

    num_ways = sum(1 for row in dp if row[-1])
    longest_substring_length = max(i for i, row in enumerate(dp) if row[-1])
    min_num_substrings = len([row for row in dp if row[-1]])

    print(sum(1 for row in dp if row[-1]) % (10**9 + 7))
    print(longest_substring_length)
    print(min_num_substrings)

if __name__ == "__main__":
    solve()
