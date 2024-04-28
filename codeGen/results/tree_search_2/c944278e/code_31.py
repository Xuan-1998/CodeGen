from collections import defaultdict

def winning_teams(n):
    dp = defaultdict(list)
    dp[0] = [0]

    for i in range(n):
        next_dp = defaultdict(list)
        current_score = 2**i - 1
        for prev_score, teams in dp.items():
            if s[i] == '1':
                next_dp[current_score + 1].extend(teams)
            elif prev_score > 0:
                next_dp[prev_score].extend(teams)

        dp = next_dp

    max_score = 2**n - 1
    return sorted([team for score, teams in dp.items() if score == max_score])

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(*winning_teams(n), sep='\n')
