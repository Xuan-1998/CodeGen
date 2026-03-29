def count_numbers(n):
    dp = [1] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i):
            if bin(j).count('1') == len(bin(j)) - 2 and dp[j] == 1:
                dp[i] = 0
                break
        if dp[i] == 1:
            count += 1
    
    return count

n = int(input())
print(count_numbers(n))
