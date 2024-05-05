def can_form_polygon():
    n = int(input())  # read number of knights
    moods = list(map(int, input().split()))  # read moods of knights
    
    total_good_moods = sum(mood for mood in moods if mood == 1)  # count good moods
    
    if n < 3:  # check if there are at least 3 knights
        print("NO")  # return "NO" if not enough knights
    elif total_good_moods % (n - 2) != 0:  # check if the number of good moods is a multiple of n-2
        print("NO")  # return "NO" if it's not
    else:
        print("YES")  # return "YES" if it is
    
can_form_polygon()
