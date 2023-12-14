from math import lcm

def part_one(instructions, direction_map, start):

    zzz_not_found = True

    i = 0
    index = 0

    current = direction_map[start]
    current_name = ''

    while zzz_not_found:
        
        i += 1
        
        if instructions[index] == 'L':
            current_name = current[0]
            current = direction_map[current[0]] # A, Z
        elif instructions[index] == 'R':
            current_name = current[1]
            current = direction_map[current[1]]
        
        index += 1

        if current_name == 'ZZZ':
            zzz_not_found = False
            print(f"ZZZ found at {i} steps")

        if index == len(instructions):
            index = 0

    return

def part_two(instructions, direction_map, starting_nodes):

    all_zzz_not_found = True
    
    i = 0
    index = 0

    current_nodes = [direction_map[start] for start in starting_nodes]
    current_multiples = [[] for i in range(len(starting_nodes))]

    while all_zzz_not_found:

        i += 1

        for n in range(len(current_nodes)):
            if instructions[index] == 'L':
                current_name = current_nodes[n][0]
                current_nodes[n] = direction_map[current_nodes[n][0]]
            elif instructions[index] == 'R':
                current_name = current_nodes[n][1]
                current_nodes[n] = direction_map[current_nodes[n][1]]

            if current_name[-1] == 'Z':
                current_multiples[n].append(i)

        index += 1

        if index == len(instructions):
            index = 0

        if i > 100000:
            all_zzz_not_found = False

    print(f"All ZZZ fount at {lcm(*[m[0] for m in current_multiples])} steps")
    return


#f = open('./sample_input.txt', 'r')
f = open('./puzzle_input.txt','r')

instructions = ''
direction_map = {}
starting_nodes = []
for line in f:
    if instructions == '':
        instructions = line.strip('\n')
    
    split_line = line.strip('\n').split('=')
    if len(split_line) == 2:
        
        l = split_line[1][2:5]
        r = split_line[1][7:10]
        p = split_line[0].strip()
        direction_map[p] = [l, r]

        if p[-1] == 'A':
            starting_nodes.append(p)
f.close()

part_one(instructions, direction_map, 'AAA')
part_two(instructions, direction_map, starting_nodes)
