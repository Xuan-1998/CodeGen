def generate_fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fib_sequence = [1, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

def main():
    n = int(input().strip())
    fib_sequence = generate_fibonacci(n)
    print(' '.join(map(str, fib_sequence)))

if __name__ == "__main__":
    main()
