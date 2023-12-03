def part_one(line):

    red_max, green_max, blue_max = 12, 13, 14

    game, cube_sets = line.split(':')

    game_number = int(game.split(' ')[-1])

    for cube_set in cube_sets.split(';'):

        for cube in cube_set.split(','):
            amount, color = cube.strip().split(' ')
            amount = int(amount)
            if color == 'red' and amount > red_max:
                return 0
            elif color == 'green' and amount > green_max:
                return 0
            elif color == 'blue' and amount > blue_max:
                return 0
    
    return game_number


def part_two(line):

    red_min, green_min, blue_min = 0, 0, 0

    game, cube_sets = line.split(':')

    for cube_set in cube_sets.split(';'):

        for cube in cube_set.split(','):
            amount, color = cube.strip().split(' ')
            amount = int(amount)
            if color == 'red' and amount > red_min:
                red_min = amount
            elif color == 'green' and amount > green_min:
                green_min = amount
            elif color == 'blue' and amount > blue_min:
                blue_min = amount
        
    return red_min * green_min * blue_min

f = open('./puzzle_input.txt')

part_one_sum = 0
part_two_sum = 0

for line in f:

    part_one_sum += part_one(line)
    part_two_sum += part_two(line)

f.close()

print(part_one_sum)
print(part_two_sum)
