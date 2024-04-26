from collections import Counter

def max_points(sequence):
    frequency = Counter(sequence)
    max_num = max(sequence)
    dp = [0] * (max_num + 1)
    
    dp[1] = frequency[1]
    
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * frequency[i])
    
    return dp[max_num]

def main():
    n = int(input().strip())
    sequence = list(map(int, input().strip().split()))
    print(max_points(sequence))

if __name__ == "__main__":
    main()
