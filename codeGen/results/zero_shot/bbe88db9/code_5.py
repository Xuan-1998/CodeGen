Let's break down the problem step by step:

1. **Understand the problem**: The problem states that Vasya starts at room 1 and needs to get to room (n+1). He can use two one-way portals in each room. If the ceiling of a room contains an odd number of crosses, he uses the second portal; otherwise, he uses the first portal.

2. **Initialize variables**: We need to initialize a variable to store the total number of moves and another to store the current room number.

3. **Create a function to calculate the number of moves**: Create a recursive function that takes the current room number as an argument. This function will recursively call itself until it reaches the target room (n+1).

4. **Calculate the number of moves for each room**: In each room, we need to decide which portal to use based on whether the ceiling contains an odd or even number of crosses.

5. **Print the result**: Print the total number of moves calculated in step 3 modulo 1000000007 (10^9 + 7).

Here's a Python solution implementing these steps:

