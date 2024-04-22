def fib(n, memo):
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo) if n > 1 else n
    return memo[n]

def main():
    n = int(input("Enter the Fibonacci number to calculate: "))
    memo = {}  # Initialize the memoization dictionary
    result = fib(n, memo)
    print(result)

if __name__ == "__main__":
    main()
