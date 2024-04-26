def read_ints():
    return list(map(int, input().split()))

def main():
    n = int(input())
    a = read_ints()
    
    max_val = max(a)
    freq = [0] * (max_val + 1)
    
    # Fill the frequency array
    for num in a:
        freq[num] += 1
    
    # Initialize dp array
    dp = [0] * (max_val + 1)
    dp[1] = freq[1]
    
    # Fill the dp array using the recurrence relation
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])
    
    # The answer is the last element in the dp array
    print(dp[max_val])

if __name__ == "__main__":
    main()
