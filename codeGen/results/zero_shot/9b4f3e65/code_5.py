def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
        return fib

def main():
    n = int(input().strip())
    fibonacci_numbers = generate_fibonacci(n)
    print(fibonacci_numbers)

if __name__ == "__main__":
    main()
