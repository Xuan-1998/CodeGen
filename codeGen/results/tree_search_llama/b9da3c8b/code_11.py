from collections import deque

n = int(input())
events = list(map(int, input().split()))

available_officers = deque()

crime_count = 0

for event in events:
    if event == -1:  # crime occurred
        if available_officers:  # if there are available officers
            available_officers.pop()  # decrement the count of an available officer
        else:  # no available officers, so crime goes untreated
            crime_count += 1
    else:  # officers recruited
        available_officers.extend([event] * event)  # add the new officers to the end of the queue

print(crime_count)
