import heapq

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    memo = {}

    for i in range(n):
        prime_divisor = 2
        while all(i % j != 0 for j in range(3, int(i ** 0.5) + 1)):
            prime_divisor += 1

        if i not in memo:
            memo[i] = {}
        current_beauty = 0
        for j in range(i):
            if arr[j] % prime_divisor == 0 and arr[j] in bad_primes:
                break
            elif arr[j] % prime_divisor != 0:
                continue
            else:
                current_beauty += 1
        memo[i][prime_divisor] = current_beauty

    max_beauty = 0
    for i in range(n):
        if i not in memo:
            continue
        for key, value in memo[i].items():
            max_beauty = max(max_beauty, value)

    print(max_beauty)


if __name__ == "__main__":
    solve()
