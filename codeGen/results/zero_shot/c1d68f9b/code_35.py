import sys

def can_form_polygon(moods):
    for i in range(len(moods) - 2):  # check for three consecutive knights
        if (moods[i] == 0 and moods[i+1] == 1 and moods[i+2] == 0) or \
           (moods[i] == 1 and moods[i+1] == 0 and moods[i+2] == 1):
            return "NO"
    return "YES"

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

print(can_form_polygon(moods))
