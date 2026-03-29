def count_matrices(N):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(i // 2 + 1):
            if i - j >= 0 and ((i - j) % 2 == 0 or j % 2 == 0):
                dp[i] += dp[j]
    return sum([dp[i] * (i // 2 + 1) for i in range(N + 1) if i % 2 != 0])

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(count_matrices(N))

if __name__ == "__main__":
    main()
