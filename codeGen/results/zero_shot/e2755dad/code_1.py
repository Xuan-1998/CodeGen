def can_be_expressed(n):
    # Check if n can be expressed as a sum of 2020s and at most one 2021
    for i in range(n // 2020 + 1):
        if (n - i * 2020) % 2021 == 0:
            return "YES"
    return "NO"

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = can_be_expressed(n)
        print(result)

if __name__ == "__main__":
    main()
