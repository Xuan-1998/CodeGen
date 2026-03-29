import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[[float('inf')] * 2 for _ in range(2)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    
    for room in range(n):
        for visited in range(2):
            for crosses in range(2):
                if dp[room][visited][crosses] != float('inf'):
                    if not visited and room < n + 1:
                        next_room, next_visited, next_crosses = (room + 1, 0, 0)
                    elif visited and crosses % 2 == 1:
                        next_room, next_visited, next_crosses = (p[room], 0, 1)
                    else:
                        next_room, next_visited, next_crosses = (room + 1, 1, 1)
                    dp[next_room][next_visited][next_crosses] = min(dp[next_room][next_visited][next_crosses],
                                                                    dp[room][visited][crosses] + 1)
    
    return dp[n][1][0] % 1000000007

print(solve())
