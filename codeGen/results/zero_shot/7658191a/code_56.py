import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k, z = map(int, sys.stdin.readline().split())
        scores = list(map(int, sys.stdin.readline().split()))
        max_score = 0
        score = scores[0]
        for i in range(1, n - 1):
            new_score_right = score + scores[i + 1]
            new_score_left = score + scores[i - 1]
            if (k > 0 and z >= i) or (k <= 0 and i > 1):
                if max(new_score_right, new_score_left) > max_score:
                    max_score = max(new_score_right, new_score_left)
            score = new_score_right
        print(max_score)

solve()
