from math import log10, ceil

def find_digit_one(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n+1):
        last_digit = int(log10(i)) % 10
        if last_digit == 1:
            count = sum(int(ceil(log10(j))) % 10 == 1 for j in range(2*i))
            dp[i] = count + dp[dp.index(min(dp))]
        else:
            dp[i] = dp[-1]
    
    return sum(dp)

n = int(input())
print(find_digit_one(n))
