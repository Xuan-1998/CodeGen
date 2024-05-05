python
import heapq

def max_total_joy():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Create two heaps: one for hungry hares and one for full hares
    hunger_heap = []
    fullness_heap = []
    total_joy = 0

    # Add the first hare to the hungry heap and calculate its joy value
    heapq.heappush(hunger_heap, (-a[0], 0))  # Store as negative because Python's heapq is min-heap
    total_joy += -a[0]

    for i in range(1, n):
        # Calculate the joy values of the current hare based on its adjacent hares
        if hunger_heap and fullness_heap:
            prev_hunger = -hunger_heap[0][0]
            next_fullness = -fullness_heap[0][0]
            a_val = max(a[i-1] + prev_hunger, b[i-1] + prev_hungry, c[i-1] + next_fullness)
        elif hunger_heap:
            prev_hunger = -hunger_heap[0][0]
            a_val = a[i-1] + prev_hunger
        else:
            next_fullness = -fullness_heap[0][0]
            a_val = b[i-1] + next_fullness

        # Update the total joy and update the heaps accordingly
        total_joy += a_val
        if len(hunger_heap) > 1 or (len(hunger_heap) == 1 and fullness_heap):
            heapq.heappush(fullness_heap, (-c[i], i))
        else:
            heapq.heappush(hunger_heap, (-a[i], i))

    return total_joy

print(max_total_joy())
