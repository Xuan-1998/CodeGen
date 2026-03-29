import sys

def solve():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        roads.append((si-1, ti-1))
    
    # Step 1: Find the node with the most children (most outgoing edges)
    capital = max(set([road[0] for road in roads]) | set([road[1] for road in roads]), key=lambda x: sum(1 for road in roads if road[0] == x or road[1] == x))
    
    # Step 2: Count the number of nodes reachable from the capital
    reachable_nodes = {capital}
    queue = [capital]
    while queue:
        node = queue.pop(0)
        for road in roads:
            if road[0] == node and road[1] not in reachable_nodes:
                reachable_nodes.add(road[1])
                queue.append(road[1])
            elif road[1] == node and road[0] not in reachable_nodes:
                reachable_nodes.add(road[0])
                queue.append(road[0])
    
    # Step 3: Calculate the minimum number of roads to be reversed
    min_reversals = n - len(reachable_nodes) - 1
    
    # Step 4: Generate all possible capital choices
    capital_choices = list(range(n))
    capital_choices.remove(capital)
    for road in roads:
        if road[0] == capital:
            capital_choices.remove(road[1])
        elif road[1] == capital:
            capital_choices.remove(road[0])
    
    print(min_reversals)
    print(' '.join(map(str, [capital]+capital_choices)))
