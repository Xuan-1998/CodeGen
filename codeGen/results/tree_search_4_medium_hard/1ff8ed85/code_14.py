n = int(input())
sequence_b = list(map(int, input().split()))
if len(set(sequence_b)) != n or min(sequence_b) == max(sequence_b):
    print('NO')
else:
    dp = {(0, prev_val): (False, [prev_val]) for prev_val in set(sequence_b)}
    for i, val in enumerate(sequence_b):
        if i > 0:
            for prev_val in set(sequence_b):
                if val <= prev_val and dp.get((i-1, prev_val)):
                    res, segs = dp[(i-1, prev_val)]
                    new_segs = segs + [str(len(segs)) + str(val)]
                    print('YES')
                    exit(0)
    print('NO')
