def main():
    n = int(input())
    q = int(input())
    c = int(input())

    # Initialize a dictionary to store the stars
    stars = {}

    for _ in range(n):
        x, y, s = map(int, input().split())
        if (x, y) not in stars:
            stars[(x, y)] = 0
        stars[(x, y)] += s

    # Initialize a variable to store the total brightness
    total_brightness = 0

    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        for star_x, star_y in stars:
            if min(x1, x2) <= star_x <= max(x1, x2) and min(y1, y2) <= star_y <= max(y1, y2):
                brightness = min(c, s + (t - 0) // 10)
                total_brightness += brightness

    print(total_brightness)

if __name__ == "__main__":
    main()
