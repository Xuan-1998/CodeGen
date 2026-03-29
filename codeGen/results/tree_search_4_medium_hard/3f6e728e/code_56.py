import sys
from collections import defaultdict

def main():
    read_int = lambda: int(next(open('input.txt')).strip())
    N, M, C = read_int(), read_int(), read_int()
    upper_hemispheres = list(map(int, next(open('input.txt')).split()))
    lower_hemispheres = list(map(int, next(open('input.txt')).split()))

    dp = defaultdict(int)
    dp[0] = 1
    for i in range(1, C+1):
        total_upper_hemispheres = sum((upper_hemisphere <= i) for upper_hemisphere in upper_hemispheres)
        total_lower_hemispheres = sum((lower_hemisphere <= i) for lower_hemisphere in lower_hemispheres)
        dp[i] = (dp[i-1] + sum(dp[total_upper_hemispheres - j] * dp[total_lower_hemispheres - k] for j in range(total_upper_hemispheres+1) for k in range(total_lower_hemispheres+1))) % 10**9 + 7

    print(*dp.values(), sep=' ')

if __name__ == '__main__':
    main()
