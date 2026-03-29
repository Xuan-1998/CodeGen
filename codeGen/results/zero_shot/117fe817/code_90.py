def count_digit_ones(n):
    count = 0
    for i in range(1, n+1):
        if i % 10 == 0:  # multiple of 10?
            count += i // 10
        else:
            count += 0
    return count

# Read input from stdin and print the result to stdout
n = int(input())
print(count_digit_ones(n))
