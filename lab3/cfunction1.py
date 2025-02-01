#3
def puzzle(head, legs):
    for i in range(1,head):
        if i*2 + (head-i)*4==legs:
            return f"chicken {i}, rabbits {head-i} "
print(puzzle(35,94))