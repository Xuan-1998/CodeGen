from functools import lru_cache

def partition_palindromes(s):
    @lru_cache(None)
    def is_palindrome(sub):
        return sub == sub[::-1]

    dp = [[[] for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j+1]):
                for x in dp[i][j]:
                    dp[i][j+1].append([*x, s[i:j+1]])
                dp[i][j+1].append([s[i:j+1]])

    return [p for sub in dp[0][-1] for p in partition_palindromes(sub)]

def main():
    N = int(input())
    S = input()

    result = partition_palindromes(S)

    print(result)

if __name__ == "__main__":
    main()
