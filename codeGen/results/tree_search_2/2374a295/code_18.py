def is_divisible(n, k):
    return k % n == 0

def count_good_sequences(n, k):
    memo = {(0, k): 1}
    for i in range(1, n+1):
        for j in range(1, min(i+1, k+1)):
            if (i-1, k-j) not in memo:
                memo[(i-1, k-j)] = 0
            memo[(i, k)] = (memo.get((i-1, k-j), 0) + 
                             is_divisible(n, j)*memo[(i-1, k-j-j)])
    return sum(1 for i in range(k+1) if memo[(n, i)] % 100000007 == 1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_good_sequences(n, k))
