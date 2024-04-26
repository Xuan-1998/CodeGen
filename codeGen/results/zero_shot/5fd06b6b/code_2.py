# Read the number of days
n = int(input())

# Read the marks above the water level for each day
marks_above = list(map(int, input().split()))

# Initialize variables
waterLevel = 0
totalMarksBelow = 0

# Iterate through each day
for i in range(n):
    # Calculate the current water level
    currentWaterLevel = i - marks_above[i]
    
    # Update the water level if the current is higher
    waterLevel = max(waterLevel, currentWaterLevel)
    
    # Calculate marks below the water level for the day and add to total
    totalMarksBelow += (i - waterLevel)

# Print the result
print(totalMarksBelow)
