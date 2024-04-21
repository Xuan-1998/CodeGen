def main():
    # Read the input from stdin
    N = int(input().strip())

    # Initialize the list with the first two Fibonacci numbers
    fib = [1, 1]

    # If N is 1, we only need the first Fibonacci number
    if N == 1:
        print(fib[:1])
        return

    # Compute the rest of the Fibonacci numbers up to N
    for i in range(2, N):
        fib.append(fib[i-1] + fib[i-2])

    # Print the first N Fibonacci numbers to stdout
    print(fib)

if __name__ == "__main__":
    main()
