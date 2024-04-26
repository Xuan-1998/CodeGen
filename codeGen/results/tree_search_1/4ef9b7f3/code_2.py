from collections import deque

def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))
    return n, a, k, b

def solve(n, a, k, b):
    a = deque(a)
    actions = []
    
    for target in b:
        sum_weights = 0
        while a and sum_weights < target:
            sum_weights += a[0]
            if sum_weights <= target:
                actions.append((len(a), 'L'))
                a.popleft()
            if sum_weights == target:
                break
            sum_weights += a[-1]
            if sum_weights <= target:
                actions.append((1, 'R'))
                a.pop()
            if sum_weights == target:
                break
        if sum_weights != target:
            return "NO", []
    
    if a:
        return "NO", []
    
    return "YES", actions

n, a, k, b = read_input()
result, actions = solve(n, a, k, b)

if result == "NO":
    print(result)
else:
    print(result)
    for action in actions:
        print(*action)
