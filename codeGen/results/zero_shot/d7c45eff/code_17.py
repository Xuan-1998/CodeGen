def find_smallest_string(n, k, s):
    if k >= n:
        return s * (k // n) + s[:k % n]
    else:
        return s[:-1] * (k // (n - 1)) + s[-1] * (k % (n - 1))

def main():
    n, k = map(int, input().split())
    s = input()
    print(find_smallest_string(n, k, s))

if __name__ == "__main__":
    main()
