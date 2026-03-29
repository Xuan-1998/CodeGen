def partition_palindromes(S):
    def is_palindrome(s):
        return s == s[::-1]

    dp = {0: [[]]}
    result = []

    for i in range(1, len(S) + 1):
        dp[i] = []
        for j in range(i):
            if S[j:i] and is_palindrome(S[j:i]):
                if j == 0:
                    dp[i].append([S[j:i]])
                else:
                    for p in dp[j]:
                        dp[i].append(p + [S[j:i]])

    for partitions in reversed(list(dp.values())):
        result.extend(partitions)

    return result


# Test the function
if __name__ == "__main__":
    S = input()
    print(partition_palindromes(S))
