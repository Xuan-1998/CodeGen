n = int(input())
marks_above = list(map(int, input().split()))

dp = [0] * n
above_water = [0]

for i in range(n):
    above_water.append(sum(marks_above[:i+1]))
    
for i in range(1, n):
    dp[i] = min(dp[i-1] + (i - 1) * marks_above[i], 
                sum(x + y for x, y in zip(dp[:i], [j*marks_above[i] for j in range(i)])))

print(min(dp))
