# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:

#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐       
# │------5-│        
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │     
# BANG!────┘  ├─────► OK! 
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘
# Input
# Start and finish shelf numbers (always positive integers, finish no smaller than start)

# Task
# Find the minimum number of jumps to go from start to finish

# Example
# Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

# O(n)
def solution(start, end):
    jumps = 0
    current_step = start
    while current_step + 3 <= end:
        current_step += 3
        jumps += 1
    while current_step < end:
        current_step += 1
        jumps += 1
    return jumps

# O(1)
def solution(start, end):
    total_steps = end - start
    three_step_jumps = total_steps // 3
    one_step_jumps = total_steps % 3
    return three_step_jumps + one_step_jumps

