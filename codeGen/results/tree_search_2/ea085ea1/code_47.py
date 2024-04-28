def find_max_common_substrings():
    N = int(input())  # Get the length of each string from input

    str1 = input().strip()  # Read the first string from input
    str2 = input().strip()  # Read the second string from input

    dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:  # Check if characters match
                if i == 1 or j == 1:  # Base case: first character matches
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

    max_common_substrings = max([max(row) for row in dp])
    print(max_common_substrings)

find_max_common_substrings()
