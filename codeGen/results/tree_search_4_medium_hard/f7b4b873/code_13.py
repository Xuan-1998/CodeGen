from collections import defaultdict

def partition_palindromes(s):
    dp = defaultdict(list)
    dp[0] = [[]]

    for i in range(1, len(s) + 1):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                for p in dp[j]:
                    dp[i].extend([p] + [[s[j:i]]])

    return dp[-1]


def main():
    n = int(input())
    S = input()
    result = partition_palindromes(S)
    print(result)


if __name__ == "__main__":
    main()

