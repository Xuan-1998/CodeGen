def find_digit_one(n):
    ones = [0] * (n + 1)
    
    for i in range(1, n + 1):
        ones[i] += ones[i // 10] if i // 10 >= 0 else 0
        ones[i] += i % 10 == 1
        
    return sum(ones[1:])

# Read input from stdin and print the answer to stdout
n = int(input())
print(find_digit_one(n))
