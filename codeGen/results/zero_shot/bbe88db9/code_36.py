def portal_moves(n, p):
    if n == 0:
        return 0

    # Decide which portal to use based on the number of crosses
    crosses = sum(1 for _ in range(n))
    if crosses % 2 == 1:
        return 1 + portal_moves(p-1, [i for i in p if i < n][::-1])
    else:
        return 1 + portal_moves(n-1, p)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(portal_moves(n, p) % (10**9+7))

if __name__ == "__main__":
    main()
