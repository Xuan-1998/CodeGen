from collections import defaultdict

def count_positive_invertible_matrices():
    T = int(input())
    dp = defaultdict(int)

    for _ in range(T):
        N = int(input())
        if N <= 2:
            print(1)  # Base case: there's only one invertible matrix (identity) when the trace is 0 or 1
        else:
            for t in range(3, N + 1):
                count = 0
                for k in range(min(t // 2, t - k)):
                    if t - k >= 0 and k >= 0:  # Check constraints i - k >= 0, j - k >= 0, and t - k >= 0
                        count += dp.get(k, 0)
                print(count)

count_positive_invertible_matrices()
