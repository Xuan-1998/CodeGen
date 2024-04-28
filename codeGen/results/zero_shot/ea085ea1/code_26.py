n = int(input())
str1 = input()
str2 = input()

def find_max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    ending_positions = []

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if i < n and j < m:
                    ending_positions.append((i, j))
                    max_length += 1

    max_common_substrings = []
    while max_length > 0:
        (end_i, end_j) = ending_positions.pop()
        start_i = end_i - dp[end_i][end_j]
        start_j = end_j - dp[end_i][end_j]

        substring = str1[start_i:end_i + 1]
        max_common_substrings.append(substring)
        max_length -= len(substring)

    print(len(max_common_substrings))
