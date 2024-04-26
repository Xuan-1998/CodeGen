from collections import deque

def main():
    n = int(input().strip())
    initial_queue = list(map(int, input().strip().split()))
    k = int(input().strip())
    final_queue = list(map(int, input().strip().split()))
    
    initial_deque = deque(initial_queue)
    actions = []
    
    for final_monster in final_queue:
        current_sum = 0
        while initial_deque and current_sum < final_monster:
            current_sum += initial_deque[0]
            initial_deque.popleft()
        
        if current_sum != final_monster:
            print("NO")
            return
        
        # Simulate the eating process
        for _ in range(len(initial_deque), 1, -1):
            if initial_deque[0] < initial_deque[-1]:
                actions.append(f"{len(initial_deque)} L")
                initial_deque.popleft()
            else:
                actions.append("1 R")
                initial_deque.pop()
    
    # Check if we have successfully processed all monsters
    if not initial_deque:
        print("YES")
        print("\n".join(actions))
    else:
        print("NO")

if __name__ == "__main__":
    main()
