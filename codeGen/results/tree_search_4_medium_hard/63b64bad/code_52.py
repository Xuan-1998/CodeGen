def final_value_after_operations(operations):
    n = len(operations) + 1
    memo = {0: 0}

    for a in operations:
        new_memo = {}
        for x, y in memo.items():
            new_x = (x + a) % n
            new_y = (y + a) % n
            if new_x <= 0 or new_x > n:
                return -1
            new_memo[new_x] = max(new_memo.get(new_x, 0), new_y)
        memo = new_memo

    return list(memo.values())[-1]
