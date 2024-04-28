n = int(input())
s = input()

dp_table = [[[-1 for _ in range(3)] for _ in range(3)] for _ in range(n+1)]
for i in range(1, n+1):
    for prev_color in range(3):
        if s[i-1] == 'R' and prev_color == 0:
            dp_table[i][prev_color][curr_color] = min(dp_table[i][prev_color][curr_color], dp_table[i-1][prev_color][2-curr_color])
        elif s[i-1] == 'G' and prev_color == 1:
            dp_table[i][prev_color][curr_color] = min(dp_table[i][prev_color][curr_color], dp_table[i-1][prev_color][2-curr_color])
        elif s[i-1] == 'B' and prev_color == 2:
            dp_table[i][prev_color][curr_color] = min(dp_table[i][prev_color][curr_color], dp_table[i-1][prev_color][2-curr_color])

r = dp_table[n][0][1] + dp_table[n][0][2]
t = ''
curr_color = 1
for i in range(n):
    if s[i] == 'R' and curr_color != 0:
        t += 'R'
        curr_color = (curr_color + 1) % 3
    elif s[i] == 'G' and curr_color != 1:
        t += 'G'
        curr_color = (curr_color + 1) % 3
    elif s[i] == 'B' and curr_color != 2:
        t += 'B'
        curr_color = (curr_color + 1) % 3

print(r)
print(t)
