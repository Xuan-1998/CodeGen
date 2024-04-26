def find_eating_order(initial_queue, final_queue):
    actions = []
    i, j = 0, 0
    current_sum = 0

    while j < len(final_queue):
        if i >= len(initial_queue):
            return "NO", []

        current_sum += initial_queue[i]
        i += 1

        if current_sum > final_queue[j]:
            return "NO", []

        if current_sum == final_queue[j]:
            right_pointer = i - 1
            left_pointer = right_pointer - 1
            while left_pointer >= (i - (right_pointer - left_pointer) - 1):
                actions.append(f"{left_pointer + 1} R")
                left_pointer -= 1
            j += 1
            current_sum = 0

    return "YES", actions

def main():
    n = int(input().strip())
    initial_queue = list(map(int, input().strip().split()))
    k = int(input().strip())
    final_queue = list(map(int, input().strip().split()))

    result, actions = find_eating_order(initial_queue, final_queue)
    if result == "NO":
        print(result)
    else:
        print(result)
        for action in actions:
            print(action)

if __name__ == "__main__":
    main()
