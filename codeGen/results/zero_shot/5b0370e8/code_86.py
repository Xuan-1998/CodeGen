def solve(n, k):
    # Calculate the maximum possible value
    max_val = max_and_xor_value(k)

    count = 0
    for _ in range(n):
        x = int(input())
        if x <= max_val:
            count += 1

    print(count % (10**9 + 7))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        solve(n, k)
