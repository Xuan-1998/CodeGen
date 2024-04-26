n = int(input())
recruitments = []
for event in input().split():
    if event == '-1':
        recruitments.append((len(recruitments), 0))
    else:
        recruitments.append((len(recruitments), int(event)))

recruitments.sort()

untreated_crimes = 0
officers_recruited = 0
for event in recruitments:
    if event[1] > 0:
        officers_recruited += event[1]
    else:
        if officers_recruited < 1:
            untreated_crimes += 1
        officers_recruited = 0

print(untreated_crimes)
