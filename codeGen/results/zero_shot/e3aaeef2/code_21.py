def solve(n, m):
    # Calculate the maximum possible value of a digit after m operations
    max_digit = 10 + m
    
    # Calculate the length of the resulting number (i.e., the number of digits)
    result_length = len(str(n))
    
    # The length of the resulting number cannot exceed the initial number n
    if max_digit >= n:
        result_length = 1
    
    # Return the length of the resulting number modulo 10^9+7
    return result_length % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
