input = sys.stdin.read

def max_points(n, sequence):
    if n == 0:
        return 0
    
    max_val = max(sequence)
    freq = [0] * (max_val + 1)
    
    for num in sequence:
        freq[num] += 1
    
    dp = [0] * (max_val + 1)
    dp[1] = freq[1] * 1
    
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i] * i)
    
    return dp[max_val]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

