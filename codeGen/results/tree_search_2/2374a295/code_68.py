def dp(i, j):
    if i == 1:
        return 1  # base case: only one sequence for i=1
    elif j % i == 0:
        if j // i < min(i, j//i):  # avoid unnecessary computation
            return sum(dp(k, j//k) for k in range(2, min(i, j//i)+1))
        else:
            return 0
    else:
        return 0

def main():
    n, k = map(int, input().split())
    print((dp(k, n) % 1000000007))  # output the count modulo 10000...7

if __name__ == "__main__":
    main()
