import sys

def solve():
    n = int(input())
    beacons = []
    for _ in range(n):
        a, b = map(int, input().split())
        beacons.append((a, b))
    
    beacons.sort()
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_power = 0
        for j in range(i - 1, -1, -1):
            if beacons[j][1] > max_power:
                max_power = beacons[j][1]
                break
        dp[i] = max_power
    
    res = 0
    total_power = sum(beacon[1] for beacon in beacons)
    for i in range(n, -1, -1):
        if total_power - dp[i] > 0:
            res += 1
            total_power -= max(beacon[1] for beacon in beacons[:i])
    
    print(res)

if __name__ == "__main__":
    solve()
