
def part_one(line):

    start, end = 0, 0
    for letter in line:
        if letter.isdigit():
            start = letter
            break

    for letter in line[::-1]:
        if letter.isdigit():
            end = letter
            break

    return int(start + end)

def part_two(line):

    numbers = []
    i = 0
    while i < len(line):
        
        if line[i].isdigit():
            numbers.append(line[i])
        
        elif line[i] == 'o':
            if line[i : i + 3] == 'one':
                numbers.append('1')
                #i = i + 1
        
        elif line[i] == 't':
            if line[i : i + 3] == 'two':
                numbers.append('2')
                #i = i + 1
            elif line[i : i + 5] == 'three':
                numbers.append('3')
                #i = i + 3
        
        elif line[i] == 'f':
            if line[i : i + 4] == 'four':
                numbers.append('4')
                #i = i + 2
            elif line[i : i + 4] == 'five':
                numbers.append('5')
                #i = i + 2
        
        elif line[i] == 's':
            if line[i : i + 3] == 'six':
                numbers.append('6')
                #i = i + 1
            elif line[i : i + 5] == 'seven':
                numbers.append('7')
                #i = i + 3
        
        elif line[i] == 'e':
            if line[i : i + 5] == 'eight':
                numbers.append('8')
                #i = i + 3
        
        elif line[i] == 'n':
            if line[i : i + 4] == 'nine':
                numbers.append('9')
                #i = i + 2
        
        i = i  + 1
        
    #print(numbers)
    # e, f, n, o, s, t
    return int(numbers[0] + numbers[-1])



f = open('./puzzle_input.txt')

part_one_sum = 0
part_two_sum = 0

for line in f:
    part_one_sum += part_one(line)
    part_two_sum += part_two(line)

print('part one sum is :', part_one_sum)
print('part two sum is :', part_two_sum)

f.close()

