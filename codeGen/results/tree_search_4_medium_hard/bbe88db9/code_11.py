def solve():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [[float('inf')] * (n+2) for _ in range(2)]
    
    dp[0][1] = 0
    
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                first_portal_room = p[j]
                second_portal_room = dp[(j+1)%2][first_portal_room] + 1
                ceiling_painted = True
            else:
                first_portal_room = p[j-1]
                second_portal_room = dp[(j+1)%2][second_portal_room] + 1
                ceiling_painted = not ceiling_painted
            
            if j % 2 == 0 and ceiling_painted or j % 2 != 0 and not ceiling_painted:
                dp[1-i%2][i+1] = min(dp[1-i%2][first_portal_room], second_portal_room) + 1
    
    return (dp[-1][-1] - 1) % 1000000007

print(solve())
