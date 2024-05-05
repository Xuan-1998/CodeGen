import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_beauty(arr, bad_primes):
    n = len(arr)
    dp = {i: 0 for i in range(n)}
    
    # Calculate the beauty for each number as the pivot
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                common_divisor = gcd(arr[i], arr[j])
                if common_divisor not in bad_primes:
                    dp[i] = max(dp.get(i-1, 0), dp.get(j, 0) - arr[i])

    return dp[0]

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    print(max_beauty(arr, bad_primes))

if __name__ == "__main__":
    main()
