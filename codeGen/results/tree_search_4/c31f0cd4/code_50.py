from itertools import combinations

def solve(a):
    n = len(a)
    dp_state = [[[]], [0]]

    for i in range(1, n + 1):
        temp_dp_state = []
        for j in range(sum(a), -1, -1):
            temp_result = set()
            if j >= a[i]:
                for k in range(j, a[i] - 1, -1):
                    if not any(k in subset for subset in dp_state):
                        result = list(set(list(combinations(a[:i], k)) + list(combinations(a[i+1:], j-k))))
                        temp_result.update(result)
            temp_dp_state.append([j] + sorted(temp_result))
        dp_state.extend(temp_dp_state)

    return [str(x) for x in dp_state[0]][1:]

# Read input
n = int(input())
a = list(map(int, input().split()))

print(' '.join(solve(a)))
