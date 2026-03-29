def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, s, a[-1]))

if __name__ == "__main__":
    main()
