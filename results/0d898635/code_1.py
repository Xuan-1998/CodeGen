def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def main():
    n = int(input("Enter the Fibonacci number to calculate: "))
    memo = {}
    print(fib(n, memo))

if __name__ == "__main__":
    main()
