def palindromePartitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    partitions = []

    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j+1]):
                dp[i][j] = True

    def backtrack(start, path):
        if start == len(s):
            partitions.append(path)
            return
        for end in range(start, len(s)):
            if dp[start][end]:
                backtrack(end + 1, [s[start:end+1]] + path)

    backtrack(0, [])
    return partitions

def main():
    s = input()
    result = palindromePartitions(s)
    print(result)

if __name__ == "__main__":
    main()
