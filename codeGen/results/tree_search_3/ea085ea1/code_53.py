def find_longest_common_substring(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    state = {}

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                state[(i, j)] = (str1[:i], str2[:j])

    max_length = 0
    longest_common_substrings = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                longest_common_substrings.append(state[(i, j)][0])

    return len(longest_common_substrings)

def main():
    str1 = input()
    str2 = input()
    print(find_longest_common_substring(str1, str2))

if __name__ == "__main__":
    main()

