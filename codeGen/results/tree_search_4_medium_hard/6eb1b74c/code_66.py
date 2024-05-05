def min_steps_to_color_red(text, strings):
    n = len(strings)
    dp = [[-1 for _ in range(len(text) + 1)] for _ in range(n + 1)]
    dp[0] = list(range(len(text) + 1))

    for i in range(1, n + 1):
        for j in range(len(text) + 1):
            if j == 0:
                dp[i][j] = -1
            elif strings[i-1].startswith(text[j-1:j+len(strings[i-1])]):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-len(strings[i-1])]) + 1
            else:
                dp[i][j] = dp[i][j-1]

    steps = []
    j = len(text)
    for i in range(n, -1, -1):
        if dp[i][j] != dp[i-1][j]:
            steps.append((i+1, j-len(strings[i]) + 1))
            j -= len(strings[i])
    steps.reverse()

    return dp[n][len(text)], steps

def main():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    result_steps, result_strings = min_steps_to_color_red(t, strings)
    if result_steps == -1:
        print(-1)
    else:
        print(result_steps)
        for step, position in result_strings:
            print(f"{step} {position}")

if __name__ == "__main__":
    main()
