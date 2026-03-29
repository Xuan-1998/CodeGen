from collections import defaultdict

def partition_palindromes(s):
    dp = defaultdict(list)
    dp[0].append([])

    for i in range(len(s)):
        for j in range(i, -1, -1):
            if s[j:i+1] == s[i:j-1:-1]:
                for partition in dp[j-1]:
                    dp[i].extend([*partition, [s[j:i+1]]])

    return [p for p in dp[-1]]

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(partition_palindromes(s))
