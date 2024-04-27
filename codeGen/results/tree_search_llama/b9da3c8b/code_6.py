available_officers = 0
untreated_crimes = 0

n = int(input())  # Read the number of events
for _ in range(n):
    event = int(input())
    if event == -1:  # Crime occurred
        available_officers += event
        if available_officers <= 0:
            untreated_crimes += 1
            available_officers = 0
    else:  # Officers recruited
        available_officers += event

print(untreated_crimes)
