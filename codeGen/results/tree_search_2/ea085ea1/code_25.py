def max_common_substrings(str1, str2):
    N = len(str1)
    dp = {}

    for i in range(N):
        for j in range(i + 1, N + 1):
            for k in range(N):
                for l in range(k + 1, N + 1):
                    # Check if there are any common characters between the substrings
                    if all(c1 == c2 or c1 == '*' and c2 != '*' or c1 == '@' and c2 != '@' for c1, c2 in zip(str1[i:j], str2[k:l])):
                        # If there is a connection from state (str1[m..n], str2[p..q]) to state (str1[i..j], str2[k..l]), add it to the DP table
                        dp[(str1[i:j], str2[k:l])] = max(dp.get((str1[i:j], str2[k:l]), 0) + 1, dp.get((str1[m..n], str2[p..q]), 0))
                    else:
                        # If there is no connection from state (str1[m..n], str2[p..q]) to state (str1[i..j], str2[k..l]), set the value to 0
                        dp[(str1[i:j], str2[k:l])] = 0

    return max(dp.values())

# Read input strings from standard input
str1, str2 = [line.strip() for line in sys.stdin.readlines()]

print(max_common_substrings(str1, str2))
