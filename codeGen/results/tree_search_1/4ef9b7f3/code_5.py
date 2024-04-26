from collections import deque

def main():
    n = int(input())
    initial_queue = list(map(int, input().split()))
    k = int(input())
    final_queue = list(map(int, input().split()))

    actions = []
    i, j = 0, 0
    current_sum = 0

    while i < n and j < k:
        current_sum += initial_queue[i]
        i += 1

        # When the current sum matches the weight in the final queue
        if current_sum == final_queue[j]:
            # Record actions
            while i > 0:
                i -= 1
                if i == 0 or initial_queue[i - 1] < initial_queue[i]:
                    actions.append((i + 1, 'L'))
                    current_sum -= initial_queue[i]
                else:
                    actions.append((i, 'R'))
                    current_sum -= initial_queue[i - 1]

            # Move to the next weight in the final queue
            j += 1
            current_sum = 0
        elif current_sum > final_queue[j]:
            # Impossible to achieve the final queue
            print("NO")
            return

    if j == k:
        # All weights in the final queue matched
        print("YES")
        for action in actions:
            print(action[0], action[1])
    else:
        # Not all weights in the final queue were matched
        print("NO")

if __name__ == "__main__":
    main()
