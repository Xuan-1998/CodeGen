import sys

# Initialize memo dictionary
memo = {}

def calc_expected_carries(n, m):
    # Base case: if either n or m is 0, there are no more carries
    if n == 0 or m == 0:
        return 0
    
    # Calculate the sum of the current digits
    total_sum = 0
    for i in range(min(n, m)):
        total_sum += (10 ** (n - 1)) * min(9, 9 - i) + (10 ** (m - 1)) * min(9, 9 - i)
    
    # Calculate the expected number of carries
    if (total_sum >= 10):
        return 1.0 + calc_expected_carries(n - 1, m - 1)
    else:
        return calc_expected_carries(n - 1, m - 1)

def main():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        # Initialize memo dictionary if not already done
        if N not in memo:
            memo[N] = {}
        
        total_carries = sum([calc_expected_carries(i, j) for i in range(N + 1) for j in range(N + 1)])
        
        print(total_carries / (N + 1) ** 2)

if __name__ == "__main__":
    main()
