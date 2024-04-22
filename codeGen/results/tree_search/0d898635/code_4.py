def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def main():
    n = int(input("Enter the Fibonacci index: "))
    result = fib(n)
    print(f"The {n}-th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()
