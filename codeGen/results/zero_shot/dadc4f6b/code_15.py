import sys

def read_stars():
    n = int(sys.stdin.readline())
    stars = []
    for _ in range(n):
        x, y, s = map(int, sys.stdin.readline().split())
        stars.append((x, y, s))
    return stars

def calculate_brightness(star, t):
    # assume linear decrease
    initial_brightness = star[2]
    time_diff = abs(t - star[0])
    brightness = max(0, initial_brightness - time_diff)
    return brightness

def main():
    n, q, c = map(int, sys.stdin.readline().split())
    stars = read_stars()
    
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        visible_stars = []
        for star in stars:
            if x1 <= star[0] <= x2 and y1 <= star[1] <= y2:
                brightness = calculate_brightness(star, t)
                visible_stars.append(brightness)
        
        total_brightness = sum(visible_stars)
        print(total_brightness)

if __name__ == "__main__":
    main()
