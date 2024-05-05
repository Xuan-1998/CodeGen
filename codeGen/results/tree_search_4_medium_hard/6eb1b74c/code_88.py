from collections import deque

def color_text():
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]

    memo = {}
    queue = deque([(t, 0)])

    while queue:
        text, steps = queue.popleft()

        if not text:
            return str(steps), []

        if (text, steps) in memo:
            continue

        min_steps = float('inf')
        used_strings = []

        for i, string in enumerate(s):
            if text.startswith(string):
                new_text = text[len(string):]
                queue.append((new_text, steps + 1))
                if len(new_text) < len(text):
                    min_steps = min(min_steps, steps + 1)
                    used_strings = [(i + 1, len(string))] + used_strings

        memo[(text, steps)] = (min_steps, used_strings)

    return '-1', []

result, strings_used = color_text()
print(result)

if result != '-1':
    print(*strings_used, sep='\n')
