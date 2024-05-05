def find_winner(M, X):
    dp = [0] * (X + 1)
    for i in range(2, X + 1):
        if i % M == 0:
            dp[i] = (dp[i - M] + 1) % X
        else:
            dp[i] = (dp[i - 1] + 1) % X

    return [i for i in range(1, X + 1) if i % M != 0][:-1]

def main():
    T = int(input())
    for _ in range(T):
        M, X = map(int, input().split())
        print(*find_winner(M, X), sep='\n')

if __name__ == "__main__":
    main()
