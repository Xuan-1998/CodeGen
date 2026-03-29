def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        # Read edges...
        if solve(n, k, values) == "YES":
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
