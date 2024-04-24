def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print(f"The {n}th Fibonacci number is: {fib_memo(n)}")
