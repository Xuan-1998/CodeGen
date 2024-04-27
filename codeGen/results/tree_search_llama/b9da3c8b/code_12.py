import sys

n = int(sys.stdin.readline())
officers_hired = 0
crimes_uninvestigated = 0

for _ in range(n):
    event = int(sys.stdin.readline())
    
    if event == -1:
        # Crime occurred, check if there are enough officers to investigate it
        if officers_hired >= 1:
            officers_hired -= 1
        else:
            crimes_uninvestigated += 1
    else:
        # Officers were hired, increment the total police force
        officers_hired += event

print(crimes_uninvestigated)
