def partition(s):
    n = len(s)
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        if i == 0:
            dp[0][i] = [[]]
        elif i == 1:
            dp[i][1] = [[s[:i]]]
        else:
            for j in range(i):
                if s[j:i].endswith(s[j:i][::-1]):
                    for p in dp[j][j]:
                        for q in partition(s[j+1:i]):
                            dp[i][i].append([*p, s[j:i]])
                elif i - 2 >= 0:
                    for p in dp[j][j] + dp[i-2][i-2]:
                        for q in partition(s[j+1:i-1]):
                            dp[i][i].append([*p, s[j:i-1], s[i-1]])

    return dp[n][n]

def main():
    S = input()
    print(partition(S))

if __name__ == "__main__":
    main()

