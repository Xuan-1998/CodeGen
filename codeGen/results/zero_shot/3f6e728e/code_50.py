Let's start by breaking down the problem:

1. **Understand the problem**: We are given N upper hemispheres and M lower hemispheres, each with a radius between 1 and C. Our task is to find the number of different X-sequences that can be built.

2. **Identify the key components**: The two main components in this problem are:
    - Upper hemispheres (N)
    - Lower hemispheres (M)

3. **Understand the X-sequence constraint**: An X-sequence is a sequence of nested concentric spheres, and the number of different X-sequences is determined by the number of spheres of different radii available.

4. **Recognize the dynamic programming nature**: This problem can be solved using dynamic programming, as we need to keep track of the count of X-sequences for each radius from 1 to C.

5. **Create a state transition diagram**: Let's define dp[i] as the number of different X-sequences that can be built with radii up to i.
    - If there are no upper hemispheres (N=0), then dp[i] = dp[i-1].
    - If there is only one upper hemisphere (U_1) with radius U_1, then dp[i] = 1 if and only if i >= U_1; otherwise, dp[i] = dp[i-1].
    - For N > 1, we need to consider all possible radii for the first upper hemisphere. If there are M lower hemispheres, we can build a sequence with the current upper hemisphere and then add it to the count of X-sequences for each radius from U_1+1 to i.

6. **Write the code**: Here's the Python code that implements this dynamic programming approach:
