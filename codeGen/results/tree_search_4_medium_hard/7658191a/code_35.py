def max_score(n, k, z, scores):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 1 and j == 0:
            return scores[0]

        if j < 0:
            return dp(i - 1, j + z)

        max_score = 0
        for move_type in range(2):
            if move_type == 0:  # move to the right
                new_j = min(j + 1, k)
            else:  # move to the left
                new_j = max(j - 1, 0)

            score = dp(i - 1, new_j) + scores[i - 1]
            if score > max_score:
                max_score = score

        memo[(i, j)] = max_score
        return max_score

    total_score = 0
    for i in range(1, n + 1):
        total_score += dp(i, k)

    return total_score


def main():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        scores = list(map(int, input().split()))
        print(max_score(n, k, z, scores))

if __name__ == "__main__":
    main()
