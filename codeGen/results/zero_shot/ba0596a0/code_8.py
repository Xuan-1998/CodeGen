import sys

def main():
    stones = list(map(int, input().split()))
    if len(stones) < 2:
        print(False)
        return

    prev_jump_distance = 0
    for i in range(len(stones)):
        jump_distance = abs(stones[i] - stones[i-1])
        if (jump_distance != prev_jump_distance + 1 and 
            jump_distance != prev_jump_distance and 
            jump_distance != prev_jump_distance - 1):
            print(False)
            return
        prev_jump_distance = jump_distance

    print(True)

if __name__ == "__main__":
    main()
