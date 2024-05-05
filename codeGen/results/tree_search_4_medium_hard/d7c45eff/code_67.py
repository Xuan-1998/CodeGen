def lexicographically_smallest_string(n, k):
    if k >= n:
        return s * (k // n) + s[:k % n]

    dp = {0: ''}

    for i in range(1, n + 1):
        prev_str = dp.get(i - 1, '')
        curr_str = prev_str[:-1] if i > 1 else ''
        dp[i] = min([prev_str, curr_str + s[-1]], key=lambda x: (x, len(x)))

    return dp[k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input()
    print(lexicographically_smallest_string(n, k))
