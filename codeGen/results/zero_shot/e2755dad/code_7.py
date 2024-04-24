def can_be_expressed(n):
    for y in range(2021):
        if (n - y) % 2020 == 0:
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
