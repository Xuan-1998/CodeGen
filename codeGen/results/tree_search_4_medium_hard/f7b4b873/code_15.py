from collections import defaultdict

def partition(s):
    memo = defaultdict(list)
    def dfs(s, p):
        if s == '':
            return [p]
        result = []
        for i in range(len(s)):
            if s[i] == s[-1-i]:
                result.extend(dfs(s[1:-1*i], p + [s[:i+1]]))
            else:
                result.extend([p + [s[:i+1]]] + dfs(s[i:], p + [s[:i+1]]))
        return result
    return dfs(s, [])

def main():
    s = input()
    partitions = partition(s)
    for p in partitions:
        print(' '.join(p))

if __name__ == "__main__":
    main()
