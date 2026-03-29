import sys

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input().strip() for _ in range(N)]
        
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    right_visible = False
                    for k in range(j+1, N):
                        if grid[i][k] == '#':
                            break
                        right_visible = True
                    dp[i][j] = right_visible
        
        answer = sum([dp[i][-1] for i in range(N)])
        print(answer)

if __name__ == "__main__":
    solve()
