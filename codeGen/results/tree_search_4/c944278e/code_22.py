import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline().strip())
    skills = [int(x) for x in sys.stdin.readline().strip().split()]
    dp = defaultdict(lambda: defaultdict(bool))

    for i in range(1, n+1):
        threshold = 0
        for k in range(i):
            if not any(dp[i-1][j] for j in range(len(skills))):
                break
            threshold += 1
        dp[i][threshold] = True

    winning_teams = []
    for i in range(1, n+1):
        max_skill = max(x for x in skills[:i])
        if not any(dp[i-1][j] for j in range(len(skills))):
            continue
        if max_skill > threshold:
            winning_teams.append(max_skill)
        threshold += 1

    print(' '.join(map(str, sorted(winning_teams))))

if __name__ == '__main__':
    main()
