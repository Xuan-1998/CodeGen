def count_ones(n):
    memo = {0: 0}
    for i in range(1, n+1):
        if i & 1:  # If i is odd
            memo[i] = memo[i//2] + 1
        else:  # If i is even
            memo[i] = memo[i//2]
    return memo[n]

def main():
    n = int(input())
    print(count_ones(n))

if __name__ == "__main__":
    main()
