def process_digits(n, m):
    memo = {(i, 0): i for i in range(1, n+1)}
    
    for length in range(m+1):
        if length > 0:
            new_length = (length + len(str(length))) % (10**9 + 7)
            next_length_values = set()
            for prev_length, value in list(memo.items()):
                if prev_length[1] == length and prev_length[0] <= n:
                    for digit in str(value):
                        next_value = int(digit) + 1
                        new_value = int(str(value).replace(digit, str(next_value)))
                        next_length_values.add((new_length, new_value))
            memo.update({k: v for k, v in next_length_values})
    
    return min(k[0] for k in memo if k[1] <= n)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(process_digits(n, m) % (10**9 + 7))
