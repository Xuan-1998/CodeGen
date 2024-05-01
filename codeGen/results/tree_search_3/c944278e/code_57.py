from collections import defaultdict

def winning_teams(n):
    s = input()  # read binary string from stdin
    dp = defaultdict(int)  # initialize memoization dictionary

    for i in range(1, n+1):
        for k in range(2**i):  # iterate over all possible results for phase i
            if s[k] == '0':  # losing team
                dp[(i+1, '0')] += sum(dp[(i, j)] for j in range(2**i) if bin(j)[2:].count('0') == k)
            else:  # winning team
                dp[(i+1, '1')] += sum(dp[(i, j)] for j in range(2**i) if bin(j)[2:].count('1') == k)

    winners = [str(i) for i in range(2**(n-1)) if dp[(n, '1')] > 0 and bin(i)[2:].count('1') == n]
    print('\n'.join(sorted(winners)))  # print all winning teams in ascending order

# Example usage:
winning_teams(3)  # input: 111 (all winning)
