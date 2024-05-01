import sys

def has_AB_and_BA(s):
    last_A = -1
    last_B = -1
    state = 'A'  # Initial state: no 'A' or 'B'

    for i, c in enumerate(s):
        if c == 'A':
            if state == 'A':  # Two consecutive 'A's; update state to 'BA'
                state = 'BA'
            elif state == 'B':  # 'A' after 'B'; update state to 'AB'
                state = 'AB'
            last_A = i
        elif c == 'B':
            if state in ['A', 'AB']:  # 'B' after 'A' or 'AB'; update state to 'BA'
                state = 'BA'
            elif state == 'B':  # Two consecutive 'B's; ignore
                pass
            last_B = i

    return state == 'AB'

s = input().strip()
print('YES' if has_AB_and_BA(s) else 'NO')
