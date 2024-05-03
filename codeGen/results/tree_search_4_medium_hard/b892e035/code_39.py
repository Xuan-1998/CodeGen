import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        dp = [[0.0] * (1 << 16) for _ in range(n + 1)]
        state = 0
        for i in range(n):
            P0, A0, B0 = map(float, sys.stdin.readline().split())
            state |= ((state >> A0.bit_length()) & 1) << B0.bit_length()
            dp[i + 1][state] += P0 * (1 - P0) / 2
            state ^= ((state >> B0.bit_length()) & 1) << A0.bit_length()
            dp[i + 1][state] += P1 * (1 - P1) / 2
        answer = sum(dp[-1])
        print(answer / (1 << n))

if __name__ == "__main__":
    calculate_probability()
