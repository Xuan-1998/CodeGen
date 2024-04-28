import sys

def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    dp = [0] * (len(S) + 1)
    min_length = sys.maxsize
    last_common_char_index = -1

    for i in range(1, len(S) + 1):
        if S[i - 1] not in T:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[last_common_char_index]
        if dp[i]:
            last_common_char_index = i

    for i in range(len(S), -1, -1):
        if not dp[i]:
            return len(S) - i
    return -1


print(find_shortest_uncommon_subsequence())
