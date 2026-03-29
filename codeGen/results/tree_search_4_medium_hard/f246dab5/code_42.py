import sys

def calculate_fare(trips):
    dp = [[0] * (3 + max(trip)) for trip in trips]
    
    for i, t in enumerate(trips):
        dp[i][0] = 20 if i > 0 else 0
        
        for j in range(1, min(i // 90 + 1, 2) + 1):
            if i - j * 90 >= 0:
                dp[i][j] = dp[i - j * 90][j - 1] + 50
            else:
                dp[i][j] = dp[i - 1][0] + 20
        
        for k in range(2, min(i // 1440 + 1, 3) + 1):
            if i - k * 1440 >= 0:
                dp[i][k] = dp[i - k * 1440][k - 1] + 120
            else:
                dp[i][k] = dp[i - 1][0] + 20
    
    return [dp[i][0] for i in range(len(trips))]

trips = []
while True:
    try:
        trip = int(input())
        trips.append(trip)
    except:
        break

print(*calculate_fare(trips), sep='\n')
