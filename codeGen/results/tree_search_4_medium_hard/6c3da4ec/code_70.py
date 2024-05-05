import sys

def max_bitwise_or(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        prev_max = dp[i - 1]
        for j in range(i):
            # Calculate the maximum bitwise OR value for two non-empty substrings
            # that have a total length of i-j and can be obtained by splitting
            # the remaining suffix s[j:i] at some position k, where 0 <= k < i-j
            max_or = 0
            left = right = 0
            for k in range(j, i):
                if (s[k] == '1'):
                    left |= 1 << (i - 1 - k)
                else:
                    right |= 1 << (k - j)
            max_or = max(max_or, left | right)

            # Update dp[i] with the maximum bitwise OR value between
            # the calculated value and the previously stored value dp[i-1]
            dp[i] = max(dp[i], prev_max + max_or)

    return bin(dp[-1])[2:]  # Convert the result to binary representation

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    print(max_bitwise_or(s))
