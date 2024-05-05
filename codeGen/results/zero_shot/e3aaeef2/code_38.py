def increment_digits(num):
    # Convert num to a string and iterate through each character (digit)
    for i in range(len(str(num))):
        digit = int(str(num)[i])
        num += 1 if digit < 9 else -10 + 1  # increment the digit, handling carry-over

    return num


def solve(t):
    for _ in range(t):
        n, m = map(int, input().split())
        result = n
        for _ in range(m):
            result = increment_digits(result)
        print(len(str(result)) % (10**9 + 7))


if __name__ == "__main__":
    t = int(input())
    solve(t)
