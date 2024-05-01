def solve(s):
    memo = {}
    def dfs(start, state):
        if (start, state) in memo:
            return memo[(start, state)]
        if start >= len(s):
            return False
        res = False
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == "AB" or sub == "BA":
                if (end - start) % 2 != 0:
                    res = True
                    break
                else:
                    res = dfs(end, state ^ 1)
                    if not res:
                        return False
        memo[(start, state)] = res
        return res

    for i in range(len(s)):
        if s[i:i+2] == "AB":
            if i % 2 != 0 and (not dfs(i+2, 1) or s[i-1] != "B"):
                print("NO")
                return
        elif s[i:i+2] == "BA":
            if i % 2 != 1 and (not dfs(i+2, 0) or s[i-1] != "A"):
                print("NO")
                return

    print("YES")

# Read the input from standard input.
input()
s = input().strip()

# Solve the problem
solve(s)
