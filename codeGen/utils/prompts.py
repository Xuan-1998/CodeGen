DYNAMIC_PROGRAMMING = [
    # "Determine the overlapping subproblems and optimal substructure respectively.",
    "Choose between employing a top-down approach with memoization or a bottom-up strategy with tabulation.",
    "Define the state expression and base case.",
    "Formulate state and transition relationships.",
    "Implement tabulation or memoization.",
]

CODING_SYSTEM = """
You are a helpful competitive programming assistant. The user is trying to solve a competitive programming problem with your help. The user might provide you with existing ideas they have; treat these ideas as the ground truth. When asked to code, YOU MUST wrap your code in a code block. Your code should receive inputs from stdin and print your answer to stdout. When asked for ideas, choices or steps, ALSO wrap your response in a code block as well.
You will now be provided with the problem statement:
===
{statement}
===
"""

CODING_SYSTEM_TREE = """
You are a helpful competitive programming assistant. The user is trying to solve a competitive programming problem with your help. The user might provide you with existing ideas they have; treat these ideas as the ground truth. When asked for possible answers, return the answers in a Python list format. Use double quotes to wrap each possible answer, and wrap the entire list in a code block using triple backticks (`). If the question contains multiple sub-questions, combine all possible answers for each sub-question within one pair of double quotes. Present all parallel answers in a single list. Ensure all the responses are within the code block. The number of answers does not necessarily have to be three, it can be any number as long as the answer makes sense. You should NOT write down the code!!!
"""


ALGORITHM_SYSTEM = """
You are an experienced AI assistant proficient in various programming algorithms and data structures. When provided with the name of an algorithm, you should provide accurate general steps for designing a solution. Steps should be limited to a maximum of five. Return the steps in a python list format. Use double quotes to wrap each step, and wrap the entire list in a code block.
"""


CODING_TRANSFORMATION = """
I came up with an intuition on how to solve this problem. It might be the complete solution or additional steps might be needed:
===
{transformation}
===
Analyze my intuition, how is it applicable to this problem? Please build on my idea and do not start over or reject the approach. What is the problem really asking, and how can it be solved with the algorithms and data structures you know? Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""


CODING_ZEROSHOT = """
How can we break down this problem and arrive at a solution? Let's think step by step. 
!!!IMPORTANT!!!: Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""

CODING_EDITORIAL = """
According to this problem's official editorial, what are some of the intermediate variables that must be calculated? How are these variables calculated and how do they lead to an answer? Let's think step by step. In Python, please also implement the solution that can pass the most testcases, as described by the editorial.
You will now be provided with the editorial:
{editorial}
"""


CODING_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think it's a problem about {algorithm}.
Analyze my intuition, how is it applicable to this problem? Please build on my idea and do not start over or reject the approach. What is the problem really asking, and how can it be solved with the algorithms and data structures you know? Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""


CODING_TRANSFORMATION_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think {transformation}. Additionally, I think it's a problem about {algorithm}.
Analyze my intuition, how is it applicable to this problem? Please build on my idea and do not start over or reject the approach. What is the problem really asking, and how can it be solved with the algorithms and data structures you know? Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""


PROVIDE_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think it's a problem about {algorithm}.
Please list concise and general steps, no more than five, for building {algorithm} program based on this problem. And return the steps in a python list format. Use double quotes to wrap each step.
"""

FOLLOW_UP_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think it's a problem about "{algorithm}".
You will provide me with three possible choices for "{step}". Each choice will be non-overlapping and independent, allowing me to choose the most suitable option later.
You must return the choices in a single python list format, which should start with \"[\" and ends with \"]\". Use double quotes(\") to wrap each choice. Your response should only contain possible choices, do not include any additional information.
YOU MUST wrap your code in a code block, which starts and ends with "```".
===BEGIN STEPS===
{steps}
===END STEPS===
"""
# Return the choices in a python list format. Use double quotes to wrap each choice.


TRANSFORMATION_EVALUATION = """
I came up with an intuition on how to solve this problem. I think it's a problem about {algorithm}.
Below is the plan I came up with:
===BEGIN PLAN===
{transformation}
===END PLAN===
Please think step by step and analyze the plan and provide feedback. Is the plan correct? How can it be improved? What are the potential issues with the plan? Does it include edge cases? 
!!!Important!!!: Please provide the updated version of the entire detailed plan only!! Do not include any comments, previous versions, or code. Use a code block to wrap the updated version of the plan.
"""

CODING_TREE_BFS = """
Please list concise and general steps for solving the problem. 
!!!IMPORTANT: You should NOT write down the code!!!
In each stage, if you can't ensure this step is the best for following stages, you should write down some possible steps to ensure a broad range of attempts. Here is an example of your response format:

Stage 1
step 1, [initial state]-> (operation 1) [state 1]
step 2, [initial state]-> (operation 2) [state 2]

Stage 2
step 1.1, [initial state]->[state 1]-> (operation 1) [state 1.1]
step 1.2, [initial state]->[state 1]-> (operation 2) [state 1.2]
step 2.1, [initial state]->[state 2]-> (operation 1) [state 2.1]
step 2.2, [initial state]->[state 2]-> (operation 2) [state 2.2]

Stage 3
step 1.1.1, [initial state]->[state 1]->[state 1.1]-> (operation 1) [
state 1.1.1]
(You should write around 8 lines for Step 3)

Stage 4
step 1.1.1.1 ...
(You should write around 16 lines for Step 4)

...
(Continue the stages until it reaches the final state)
"""

MOVE_NEXT = '''Statement: Given an array of integers, find the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
Instruction: Give the algorithm that can be used to solve this problem. Clarify the space and time complexity of the algorithm.
Possible Answers:
```
["1. Brute Force: This approach is possible as it involves checking each combination of two numbers to see if they add up to the target. Time complexity: O(n^2), space complexity: O(1)",
"2. Two-pass Hash Table: This approach improves time complexity by using a hash table for quick lookups, achieved in two passes through the array. Time complexity is O(n) and space complexity is O(n).",
"3. One-pass Hash Table: This approach checks and adds elements to the hash table simultaneously in a single pass, achieving a time complexity of O(n) and space complexity of O(n)."]```
Statement: {statement}
Instruction: {instruction}
Possible Answers:
'''
