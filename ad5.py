with open('ad5.txt') as f:
    input_list = [line.strip() for line in f]

crate_stacks = [['G','T','R','W'],['G','C','H','P','M','S','V','W'],['C','L','T','S','G','M'],
               ['J','H','D','M','W','R','F'],['P','Q','L','H','S','W','F','J'],
               ['P','J','D','N','F','M','S'],['Z','B','D','F','G','C','S','J'],['R','T','B'],['H','N','W','L','C']]
move_list = [x.split(' ') for x in input_list]
crate_mover = 9001

for x in move_list:
    amount_to_move = int(x[1])
    from_stack_index = int(x[3])
    to_stack_index = int(x[5])
    move_stack = crate_stacks[from_stack_index-1][-1*amount_to_move:]
    if crate_mover == 9000:
        move_stack.reverse()
    crate_stacks[to_stack_index - 1] = crate_stacks[to_stack_index - 1] + move_stack
    del crate_stacks[from_stack_index-1][len(crate_stacks[from_stack_index-1]) - amount_to_move:]

print(''.join([y[-1] for y in crate_stacks]))
