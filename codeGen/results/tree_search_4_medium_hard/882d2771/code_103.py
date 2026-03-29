def beautiful_participants():
    t, l, r = map(int, input().split())
    
    memo = {1: 0}
    
    for m in range(l, r + 1):
        memo[m] = float('inf')
        for split_at in range(1, m // 2 + 1):
            left, right = split_at, m - split_at
            if left not in memo:
                memo[left] = beautiful_participants(left)
            if right not in memo:
                memo[right] = beautiful_participants(right)
            memo[m] = min(memo[m], left * memo[left] + right * memo[right])
    
    return sum(ti * (memo[li + i] - li) for i, (ti, li) in enumerate(zip(map(int, input().split()), [l + i for i in range(r - l + 1)]))) % (10**9 + 7)
