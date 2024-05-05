import sys

def get_beacons():
    n = int(sys.stdin.readline())
    beacons = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        beacons.append((a, b))
    return sorted(beacons)

def count_destroyed(beacons):
    destroyed = 0
    prev_end = float('inf')
    for (pos, power) in reversed(beacons):
        if pos < prev_end:
            destroyed += 1
        else:
            prev_end = min(prev_end, pos + power)
    return destroyed

def main():
    beacons = get_beacons()
    print(count_destroyed(beacons))

if __name__ == "__main__":
    main()
