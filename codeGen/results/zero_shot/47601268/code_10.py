def count_numbers_without_consecutive_ones(n):
    return n // 2 + (1 if n % 2 == 0 else 0)

if __name__ == "__main__":
    n = int(input())
    print(count_numbers_without_consecutive_ones(n))
