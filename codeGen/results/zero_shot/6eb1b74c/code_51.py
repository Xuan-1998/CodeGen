import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

string_info = [(len(s), [i]) for i, s in enumerate(strings)]

for s in strings:
    start = 0
    while start < len(text):
        pos = text.find(s, start)
        if pos == -1:
            break
        string_info[strings.index(s)].append(pos)
        start = pos + 1

dp = [0]
for i in range(1, len(text) + 1):
    dp.append(min((dp[j - 1] + 1 for j, s_info in enumerate(string_info) if any(pos < i and pos >= j - len(s) for pos in s_info[1])) or [-1], default=[-1][0]))

print(dp[-1])

for i in range(len(text)):
    if dp[i] == -1:
        print(-1)
        break
    max_step = 0
    best_string = None
    for s_info in string_info:
        pos = next((pos for pos in s_info[1] if pos >= i), None)
        if pos is not None and len(s_info[1]) - (i - pos) > max_step:
            max_step = len(s_info[1]) - (i - pos)
            best_string = strings[string_info.index(s_info)]
    print(i, text.find(best_string, i))
