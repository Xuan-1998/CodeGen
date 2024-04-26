import sys

n = int(sys.stdin.readline())
officers_queue = []
untreated_crimes = 0

for _ in range(n):
    event = int(sys.stdin.readline())
    
    if event == -1:  # Crime occurrence
        while officers_queue and officers_queue[0] <= len(officers_queue):
            officers_queue.pop(0)
        
        if not officers_queue:
            untreated_crimes += 1
    else:  # Officer recruitment
        for _ in range(event):
            officers_queue.append(len(officers_queue) + 1)

print(untreated_crimes)
