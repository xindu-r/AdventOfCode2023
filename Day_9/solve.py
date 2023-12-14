
def part_one(history):

    sum = 0

    for h in history:
        child_diffs = [h]
        current = h
        while set(current) != {0}:
            temp_list = []
            for i in range(1, len(current)):
                temp_list.append(current[i] - current[i - 1])
            
            child_diffs.append(temp_list)
            current = temp_list

        for i in range(len(child_diffs) - 3, -1, -1):
            extra_val = child_diffs[i][-1] + child_diffs[i + 1][-1]
            child_diffs[i].append(extra_val)

        sum += child_diffs[0][-1]

    print(f"part one sum is {sum}")
    return

def part_two(history):
    sum = 0

    for h in history:
        child_diffs = [h]
        current = h
        while set(current) != {0}:
            temp_list = []
            for i in range(1, len(current)):
                temp_list.append(current[i] - current[i - 1])
            
            child_diffs.append(temp_list)
            current = temp_list

        for i in range(len(child_diffs) - 3, -1, -1):
            extra_val = child_diffs[i][0] - child_diffs[i + 1][0]
            child_diffs[i].insert(0, extra_val)

        sum += child_diffs[0][0]

    print(f"part two sum is {sum}")

    return

#f = open('./sample_input.txt', 'r')
f = open('./puzzle_input.txt', 'r')

history = []

for line in f:
    history.append([int(i) for i in line.strip().split(' ')])

f.close()


part_one(history)
part_two(history)
