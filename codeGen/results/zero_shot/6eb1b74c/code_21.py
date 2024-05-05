import sys

def min_steps_to_color_text(t, s):
    n = len(s)
    dp = [[False] * (len(t) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(len(t), -1, -1):
            if t[j:].startswith(s[i-1]):
                dp[i][j] = True
                for k in range(i-1, -1, -1):
                    if not dp[k][j]:
                        break
                else:
                    dp[i][j] = False

    min_steps = 0
    last_used_s = -1
    for j in range(len(t)):
        for i in range(n, 0, -1):
            if dp[i][j]:
                min_steps += 1
                last_used_s = i
                break
        else:
            continue
        break

    if min_steps == 0:
        return -1
    else:
        steps = []
        for j in range(min_steps):
            steps.append((last_used_s, j))
        return min_steps, steps

def main():
    while True:
        t = input().strip()
        n = int(input())
        s = [input().strip() for _ in range(n)]
        result = min_steps_to_color_text(t, s)
        if result == -1:
            print(-1)
        else:
            print(result[0])
            for step in result[1]:
                print(*step)

if __name__ == "__main__":
    main()
