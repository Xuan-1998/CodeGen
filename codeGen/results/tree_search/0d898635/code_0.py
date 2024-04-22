def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def main():
    # Read the input from stdin
    n = int(input().strip())
    # Initialize the memoization dictionary
    memo = {}
    # Compute and print the nth Fibonacci number
    print(fib(n, memo))

if __name__ == "__main__":
    main()
