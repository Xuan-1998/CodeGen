def is_valid_substring(s, start, end):
    char_counts = [0] * 26
    for i in range(start, end+1):
        char_counts[ord(s[i]) - ord('a')] += 1
    for i in range(26):
        if char_counts[i] > a[i]:
            return False
    return True

def generate_splits(s):
    n = len(s)
    dp = [1] * (n + 1)
    for i in range(2, n+1):
        for j in range(i):
            if is_valid_substring(s, j, i-1):
                dp[i] += dp[j]
    return dp

def calculate_statistics(s, a):
    dp = generate_splits(s)
    num_ways = dp[-1]
    max_length = max((i for i, x in enumerate(dp) if x == num_ways))
    min_substrings = next(i for i, x in enumerate(dp) if x >= num_ways)

    print(num_ways % (10**9 + 7))
    print(max_length)
    print(min_substrings)

if __name__ == "__main__":
    n = int(input())
    s = input()
    a = list(map(int, input().split()))
    calculate_statistics(s, a)
