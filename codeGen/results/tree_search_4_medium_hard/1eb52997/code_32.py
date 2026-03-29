from sys import stdin, stdout

def main():
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        grid = [list(stdin.readline().strip()) for _ in range(N)]
        dp = [[0] * (N - 1) for _ in range(N)]

        for i in range(N):
            for j in range(N - 1):
                if grid[i][j + 1] == '#':
                    break
            else:
                dp[i][j:] = [1] * (N - 1 - j)

        res = sum(dp[-1])
        stdout.write(str(res) + '\n')

if __name__ == "__main__":
    main()
