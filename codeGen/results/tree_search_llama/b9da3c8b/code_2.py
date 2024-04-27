import heapq

def untreated_crimes(n):
    # Read input and store it in a list
    events = [int(x) for x in input().split()]
    
    # Initialize priority queue (min-heap) with 0 available police officers
    available_officers = [0]
    heapq.heapify(available_officers)
    
    untreated_crimes = 0
    
    for event in events:
        if event == -1:  # Crime occurred
            if available_officers[0] < 1:
                untreated_crimes += 1
            else:
                heapq.heappop(available_officers)  # Assign a police officer to the crime
        else:  # Officers were recruited
            for _ in range(event):
                heapq.heappush(available_officers, 1)
    
    return untreated_crimes

if __name__ == "__main__":
    n = int(input())
    print(untreated_crimes(n))
