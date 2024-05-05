def apply_operations(n, m):
    for _ in range(m):
        new_n = ''
        for digit in str(n):
            new_n += str(int(digit) + 1)
        n = int(new_n)

    return len(str(n)) % (10**9 + 7)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(apply_operations(n, m))
