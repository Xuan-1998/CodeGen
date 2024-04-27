def solve():
    n = int(input())
    events = list(map(int, input().split()))
    
    officers = 0
    crimes = 0
    
    for event in events:
        if event == -1:  # Crime occurrence
            crimes += 1
        else:  # Officer recruitment
            officers += event
            while crimes > officers and event > 0:
                event -= 1
                officers += 1
            crimes -= min(event, crimes)
    
    return crimes

print(solve())
