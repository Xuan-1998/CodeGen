def solve():
    n = int(input())
    
    # Initialize dp array
    dp = [[0] * (n + 1) for _ in range(10)]
    
    # Initialize hashmap to store frequency of each digit
    freq = [0] * 10
    
    # Count the number of blocks ending at each digit position
    for i in range(10 ** n):
        digit = int(str(i)[0])
        
        if digit == 0:
            dp[digit][1] += 1
        else:
            dp[digit][1] += freq[digit - 1]
            
        freq[digit] += 1
        
        for k in range(2, n + 1):
            if i % (10 ** k) == digit * (10 ** (k - 1)):
                dp[digit][k] = dp[digit][k - 1]
            else:
                dp[digit][k] = 0
        
    # Calculate the sum of block counts for each position
    answer = 0
    for i in range(10 ** n):
        digit = int(str(i)[0])
        for k in range(n + 1):
            if i % (10 ** k) == digit * (10 ** (k - 1)):
                answer += dp[digit][k]
    
    print(answer % 998244353)

if __name__ == "__main__":
    solve()
