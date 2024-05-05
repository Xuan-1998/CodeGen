python
Let's start by breaking down the problem:

1. Vasya starts at room 1, so we can keep track of his current position.

2. For each step, he either stays in the same room or moves to another room through a portal.

3. The choice of which portal to use is based on whether there's an odd number of crosses painted on the ceiling. We can use a boolean variable to represent this (odd_crosses).

4. When Vasya reaches room n+1, he's done, so we'll keep track of how many steps it takes him.

Here's some sample Python code to get us started:
