def count_uninvestigated_crimes(crimes_and_hires):
    available_police_force = 0
    uninvestigated_crimes = 0
    
    for event in crimes_and_hires:
        if event == -1:  # Crime occurrence
            if available_police_force >= 1:
                available_police_force -= 1
            else:
                uninvestigated_crimes += 1
        else:  # Officer hiring
            available_police_force += event
    
    return uninvestigated_crimes

# Read input from stdin
n = int(input())
crimes_and_hires = list(map(int, input().split()))

result = count_uninvestigated_crimes(crimes_and_hires)
print(result)
