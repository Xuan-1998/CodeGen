def calculate_brightness(stars, view):
    # Initialize total brightness for this view
    total_brightness = 0
    
    # Iterate over each star
    for star in stars:
        # Calculate if the star is within the current view
        if (star[0] >= view[0][0] and star[0] <= view[1][0] and 
            star[1] >= view[0][1] and star[1] <= view[1][1]):
            # Add the star's initial brightness to the total brightness
            total_brightness += star[2]
    
    return total_brightness


def main():
    n, q, c = map(int, input().split())
    
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))
    
    views = []
    for _ in range(q):
        t, x1, y1, x2, y2 = map(int, input().split())
        views.append(((x1, y1), (x2, y2)))
    
    # Calculate the total brightness for each view
    for view in views:
        print(calculate_brightness([star for star in stars if star[0] >= view[0][0] and star[0] <= view[1][0] and star[1] >= view[0][1] and star[1] <= view[1][1]], view))


if __name__ == "__main__":
    main()
