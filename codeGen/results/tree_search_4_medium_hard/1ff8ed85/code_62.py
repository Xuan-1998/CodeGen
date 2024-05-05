from itertools import accumulate

def check_even_odd(lengths):
    if all(length % 2 == 0 for length in lengths):
        return 'even'
    elif all(length % 2 != 0 for length in lengths):
        return 'odd'
    else:
        return None

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = [True]
    for i in range(1, n):
        if dp[i-1]:
            lengths = list(accumulate(b[:i]))
            parity = check_even_odd(lengths)
            if parity == 'even' or parity == 'odd':
                dp.append(True)
            else:
                dp.append(False)
        else:
            dp.append(False)
    
    print('YES' if any(dp) else 'NO')
