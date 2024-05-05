from itertools import combinations

def find_palindromic_partitions(s):
    dp = [[False] * len(s) for _ in range(len(s))]
    memo = {}
    start = [0] * (len(s) + 1)

    for length in range(1, len(s) + 1):
        for start_index in range(len(s) - length + 1):
            end_index = start_index + length
            if length == 1 or s[start_index:end_index].lower() == s[start_index:end_index][::-1]:
                dp[start_index][end_index] = True
                memo[(start_index, end_index)] = True

    partitions = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i][j]:
                partition = list(range(i, j + 1))
                if partition not in partitions:
                    partitions.append(partition)

    return partitions

if __name__ == "__main__":
    s = input()
    print(find_palindromic_partitions(s))
