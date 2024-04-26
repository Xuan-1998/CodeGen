from collections import deque

def main():
    n = int(input().strip())
    initial_queue = list(map(int, input().strip().split()))
    k = int(input().strip())
    final_queue = list(map(int, input().strip().split()))

    initial_deque = deque(initial_queue)
    actions = []
    j = 0
    while j < k:
        if not initial_deque:
            print("NO")
            return

        current_weight = 0
        while initial_deque and current_weight < final_queue[j]:
            if initial_deque[0] < initial_deque[-1]:
                current_weight += initial_deque[0]
                actions.append((len(initial_deque), 'L'))
                initial_deque.popleft()
            else:
                current_weight += initial_deque[-1]
                actions.append((1, 'R'))
                initial_deque.pop()

        if current_weight != final_queue[j]:
            print("NO")
            return

        j += 1

    print("YES")
    for action in actions:
        print(*action)


if __name__ == "__main__":
    main()
