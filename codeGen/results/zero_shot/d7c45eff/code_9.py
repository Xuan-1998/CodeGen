code
while True:
    n, k = map(int, input().split())
    s = input()
    
    if k <= n:
        print(s[:k])
    else:
        duplicated_s = ""
        for _ in range((k - n) // len(s) + 1):
            duplicated_s += s
        remaining_chars = "a" * (k % len(s))
        duplicated_s += remaining_chars
        sorted_duplicated_s = "".join(sorted(duplicated_s))
        print(sorted_duplicated_s)
