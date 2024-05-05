from sys import stdin

n = int(stdin.readline())
mood = list(map(int, stdin.readline().split()))

memo = {}

def solve(i):
    if (i, False) in memo:
        return memo[(i, False)]
    
    if i >= n or not mood[i]:
        result = not any(mood[j] for j in range(max(0, i - n + 1), i))
    else:
        result = solve(i - 1) and mood[i]

    memo[(i, False)] = result
    return result

print('YES' if solve(n) else 'NO')
