from itertools import chain

def partition_palindromes(s):
    dp = [[[] for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

    for i in range(len(s)):
        dp[i][i] = [[s[i]]]

    for length in range(2, len(s) + 1):
        for start in range(len(s) - length + 1):
            end = start + length
            if s[start] == s[end - 1]:  # Check if the first and last characters are the same
                if length == 2:  # If the length is 2, it's either a single character or two identical characters
                    dp[start][end].extend([[s[start], s[end - 1]]])
                else:
                    for i in range(length // 2):
                        if s[start + i] == s[end - i - 1]:  # Check if the first and last halves are palindromes
                            for left_partition in dp[i][start + i]:
                                for right_partition in dp[length - i - 1][end - i - 1]:
                                    yield [left_partition, right_partition]
            elif length % 2 != 0:  # If the length is odd, we only need to check the center character
                if s[start + length // 2] == s[end - length // 2]:  # Check if the center characters are the same
                    dp[start][end].extend(dp[length // 2][start + length // 2])

    return list(chain(*dp[-1][-1]))

input_string = input()
print(partition_palindromes(input_string))
