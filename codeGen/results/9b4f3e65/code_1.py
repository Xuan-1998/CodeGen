def generate_fibonacci(N):
    if N == 1:
        return [1]
    fib = [1, 1]
    for i in range(2, N):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    N = int(input().strip())
    fibonacci_numbers = generate_fibonacci(N)
    print(fibonacci_numbers)

if __name__ == "__main__":
    main()
