from io import StringIO

def read_input():
    # Read input strings from standard input
    str1 = ''
    for line in StringIO(input()).readlines():
        str1 += line.strip()

    str2 = ''
    for line in StringIO(input()).readlines():
        str2 += line.strip()

    return str1, str2

def find_max_common_substrings(str1, str2):
    # Get the lengths of input strings
    n = len(str1)

    # Create dynamic programming table dp
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    max_length = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

def main():
    str1, str2 = read_input()
    result = find_max_common_substrings(str1, str2)
    print(result)

if __name__ == "__main__":
    main()
