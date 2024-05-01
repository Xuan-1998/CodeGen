dp = dict()
def dp_func(N, i):
    if N < 0:
        return 0
    elif i == 0:
        return 1 if N == 0 else 0
    elif (N, i) in dp:
        return dp[(N, i)]

    total_ways = 0
    for k in range(1, i+2):
        if N-k >= 0:
            total_ways += dp_func(N-k, min(k-1, m-1))
    dp[(N, i)] = total_ways % (10**9 + 7)
    return dp[(N, i)]

def main():
    m, N = map(int, input().split())
    array = list(map(int, input().split()))
    print(dp_func(N, m))

if __name__ == "__main__":
    main()
