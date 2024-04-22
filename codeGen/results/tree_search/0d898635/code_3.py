import sys

def fib(n, memo):
    if n in memo:
        return memo[n]
    else:
        if n > 1:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
        else:
            memo[n] = n
        return memo[n]

def main():
    # Read the input from stdin
    n = int(sys.stdin.readline().strip())
    
    # Initialize the memoization dictionary
    memo = {}
    
    # Calculate and print the nth Fibonacci number
    print(fib(n, memo))

if __name__ == "__main__":
    main()
