import sys

def solve():
    n = int(sys.stdin.readline())
    p_list = list(map(int, sys.stdin.readline().split()))
    
    memo = {(n+1, True, 0): 0}
    for room in range(n, 0, -1):
        for visited in [False, True]:
            crosses = 0
            min_moves = float('inf')
            if not visited:
                min_moves = min(min_moves, memo[(room+1, False, 0)] + 1)
            else:
                for i in range(room):
                    if p_list[i] == room and (crosses % 2) == 1:
                        min_moves = min(min_moves, memo[(p_list[i], True, crosses+1)] + 1)
            memo[(room, visited, crosses)] = min_moves
    
    print(memo[(1, False, 0)] % 1000000007)

solve()
