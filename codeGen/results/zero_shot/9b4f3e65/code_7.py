def generate_fibonacci(n):
    # Base cases for n=1 and n=2
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize the list with the first two Fibonacci numbers
    fib_numbers = [1, 1]
    
    # Calculate the rest of the Fibonacci numbers up to n
    for i in range(2, n):
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)
    
    return fib_numbers

def main():
    # Read the integer N from standard input
    n = int(input().strip())
    
    # Generate and print the first N Fibonacci numbers
    fib_numbers = generate_fibonacci(n)
    for num in fib_numbers:
        print(num, end=' ')
    print()

if __name__ == "__main__":
    main()
