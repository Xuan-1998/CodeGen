def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input() for _ in range(N)]
        dp = [[0] * N for _ in range(N)]

        no_rock_to_east = True

        for i in range(1, N):
            for j in range(N):
                if grid[i][j] == '#':
                    no_rock_to_east = False
                    break

        print(sum(f(i, j) for i in range(N) for j in range(N) if grid[i][j] == '.'))

def f(i, j):
    if i == 0 or j == N - 1:
        return 1 if no_rock_to_east else 0
    dp[i][j] = sum(f(i-1, k) for k in range(j+1) if grid[i][k] == '.')
    return dp[i][j]

if __name__ == "__main__":
    main()
