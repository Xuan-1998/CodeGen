from heapq import heappush, heappop
from sys import stdin

MOD = 998244353

def main():
    n = int(stdin.readline())
    A = [stdin.readline().strip().split() for _ in range(n)]

    dp = [0] * (n + 1)  # dp[i] will hold the sum of f(B) for all subsequences ending at position i
    heap = []
    total_sum = 0

    for i in range(n):
        if A[i][0] == '+':
            x = int(A[i][1])
            # Update dp for the current position
            dp[i + 1] = (2 * dp[i] + x) % MOD
            heappush(heap, x)
        else:
            if heap:
                # Remove the smallest element from the heap
                smallest = heappop(heap)
                # Update dp for the current position
                dp[i + 1] = (2 * dp[i] - smallest + MOD) % MOD
            else:
                dp[i + 1] = 2 * dp[i] % MOD

        # Add the current dp value to the total sum
        total_sum = (total_sum + dp[i + 1]) % MOD

    # The answer is the total sum of f(B) for all subsequences
    print(total_sum)

if __name__ == "__main__":
    main()
