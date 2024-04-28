import sys

def main():
    n = int(input())
    s = input().strip()

    dp = [0] * (1 << n)
    
    for i in range(len(s) - 1, -1, -1):
        mask = (1 << i)
        for j in range(2**n):
            if ((j & mask) > 0) == (s[i] == '1'):
                dp[j | mask] = max(dp[j | mask], dp[j] + 1)

    winning_teams = []
    for i in range(2**n):
        if dp[i] >= 2**n - 1:
            winning_teams.append(bin(i)[2:].zfill(n))

    print('\n'.join(sorted(winning_teams)))

if __name__ == "__main__":
    main()
