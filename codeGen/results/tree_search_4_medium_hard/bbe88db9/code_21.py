import sys

def main():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for room in range(1, n + 1):
        if dp[room - 1]:  # Vasya has painted a cross on the ceiling
            next_room = p[room]
        else:
            next_room = 0 if room == 1 else p[1]
        
        dp[next_room] = dp.get(next_room, False) or dp[room]
    
    print(dp[n])
