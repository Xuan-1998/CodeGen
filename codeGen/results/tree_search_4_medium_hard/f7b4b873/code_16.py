def partition(s):
    dp = [[[] for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    memo = {}

    def dfs(i, p):
        if (i, tuple(p)) in memo:
            return memo[(i, tuple(p))]
        
        result = []
        
        if i < len(s):
            for j in range(i+1, len(s)+1):
                t = s[i:j]
                if t == t[::-1]:
                    result.extend(dfs(j, p + [t]))
                    break
            else:
                result.append([p])
        else:
            result.append([p])

        memo[(i, tuple(p))] = result
        return result

    return dfs(0, [])

# test your function
s = input()
print(partition(s))
