def count_digit_ones(n):
    total = 0
    for d in range(1, n.bit_length() + 2):
        total += d + (n // 10**(d-1)) * (10**d - 10**(d-1))
    return total

if __name__ == "__main__":
    n = int(input())
    print(count_digit_ones(n))
