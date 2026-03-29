import heapq

def color_text(t, s):
    n = len(s)
    heap = [(len(s[i]), i) for i in range(n)]
    heapq.heapify(heap)

    steps = 0
    uncovered_chars = set(range(len(t)))
    
    while heap:
        length, idx = heapq.heappop(heap)
        
        for i in range(len(t)):
            if t[i:i+length] == s[idx]:
                uncovered_chars -= set(range(i, i+length))
        
        if not uncovered_chars:
            break
        
        steps += 1

    if uncovered_chars:
        return -1
    else:
        return steps, [(heapq.heappop(heap)[1], i) for i in range(len(t)) if t[i:i+len(s[0])] == s[0]]
