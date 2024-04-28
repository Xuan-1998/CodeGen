from collections import deque

def flip_to_palindrome(s):
    n = len(s)
    queue = deque([(s, False)])
    visited = set()

    while queue:
        s, flipped = queue.popleft()
        if s == s[::-1]:
            return True
        for i in range(n):
            if not flipped and (i == 0 or s[i-1] != s[i]) and (i == n-1 or s[i+1] != s[i]):
                new_s = s[:i] + '0' if s[i] == '1' else '1'
                new_s += s[i+1:]
                queue.append((new_s, True))
        visited.add(s)
    return False

while True:
    try:
        n = int(input())
        s = input().strip()
        print('YES' if flip_to_palindrome(s) else 'NO')
    except EOFError:
        break
