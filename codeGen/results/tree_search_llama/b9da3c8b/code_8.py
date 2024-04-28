n = int(input())
officers = 0
untreated_crimes = 0

for _ in range(n):
    event = int(input())
    
    if event == -1:
        if officers < 1:
            untreated_crimes += 1
        else:
            officers -= 1
    else:
        officers += event

print(untreated_crimes)
