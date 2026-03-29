code
import heapq

def find_min_destroyed_beacons():
    n = int(input())
    positions, powers = [], []
    
    for _ in range(n):
        position, power = map(int, input().split())
        positions.append(position)
        powers.append(power)

    positions.sort()
    powers.sort(reverse=True)  # sort in descending order of powers

    heap = [(power, position) for power, position in zip(powers, positions)]
    heapq.heapify(heap)  # convert list to a heap
    
    destroyed_beacons = 0
    while heap:
        max_power, max_position = heapq.heappop(heap)
        
        while heap and heap[0][1] <= max_position:  # destroy beacons in range
            _, _ = heapq.heappop(heap)
            destroyed_beacons += 1

    return destroyed_beacons


if __name__ == "__main__":
    print(find_min_destroyed_beacons())
