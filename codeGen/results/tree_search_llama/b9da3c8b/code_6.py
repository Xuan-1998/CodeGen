import heapq

def number_of_untreated_crimes():
    n = int(input())
    crimes = list(map(int, input().split()))
    
    # Initialize priority queue with all 0s (representing available officers)
    officers = []
    for i in range(crimes[0], 0, -1):
        heapq.heappush(officers, i)
    
    untreated_crimes = 0
    for crime in crimes:
        if crime == -1:  # Crime occurred
            while officers and officers[0] <= crime:
                heapq.heappop(officers)  # Assign officer to crime
            if not officers:
                untreated_crimes += 1  # No available officers, increment counter

    print(untreated_crimes)

number_of_untreated_crimes()
