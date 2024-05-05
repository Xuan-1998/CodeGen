import heapq

def min_prime_divisor(n):
    # This function returns the minimum prime divisor of n
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

def is_bad_prime(p):
    # This function checks if a prime number p is bad or not
    pass  # Implement this function based on the problem constraints

def beauty(arr, bad_primes):
    # Your plan's main logic goes here
    dp = [[0] * (len(arr) + 1) for _ in range(len(arr) + 1)]
    max_beauty = 0
    
    for i in range(1, len(arr) + 1):
        min_prime = min_prime_divisor(arr[i - 1])
        is_bad = is_bad_prime(min_prime)
        
        for j in range(i):
            prev_min_prime = dp[j][i]
            if arr[j] % min_prime == 0:
                new_beauty = dp[j][i - 1] + arr[i - 1]
                dp[j][i] = max(dp[j][i], new_beauty) if not is_bad else -1
            else:
                dp[j][i] = dp[j][i - 1]
        
        max_beauty = max(max_beauty, dp[-1][i])
    
    return max_beauty

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(beauty(arr, bad_primes))

if __name__ == "__main__":
    main()
