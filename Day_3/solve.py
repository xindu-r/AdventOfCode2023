import numpy as np

#function used to verify if a number is a part number
def check_for_symbols(input_data, current_number, row, col):
    #check up
    temp_row = row - 1
    temp_col = col - len(current_number)

    if temp_row >= 0 and temp_row < input_data.shape[0]:
        for i in range(temp_col, col + 2):
            if i >= 0 and i < input_data.shape[1]:
                if input_data[temp_row][i] != '.' and not input_data[temp_row][i].isdigit():
                    return True

    #check left
    temp_col = col - len(current_number)
    if temp_col >= 0 and temp_col < input_data.shape[1]:
        if input_data[row][temp_col] != '.' and not input_data[row][temp_col].isdigit():
            return True
    #check right
    temp_col = col + 1
    if temp_col >= 0 and temp_col < input_data.shape[1]:
        if input_data[row][temp_col] != '.' and not input_data[row][temp_col].isdigit():
            return True
    #check down

    temp_row = row + 1
    temp_col = col - len(current_number)

    if temp_row >= 0 and temp_row < input_data.shape[0]:
        for i in range(temp_col, col + 2):
            if i >= 0 and i < input_data.shape[1]:
                if input_data[temp_row][i] != '.' and not input_data[temp_row][i].isdigit():
                    return True
    return False

# works by reading a number first then verifying if its a part number
def part_one(input_data):

    part_numbers = []
    sum_of_part_numbers = 0

    current_number = ''
    for row in range(input_data.shape[0]):
        for col in range(input_data.shape[1]):
            if input_data[row][col].isdigit():
                current_number += input_data[row][col]
            else:
                if current_number != '':
                    if col == 0:
                        if check_for_symbols(input_data, current_number, row - 1, input_data.shape[1] - 1):
                            part_numbers.append(current_number)
                            sum_of_part_numbers += int(current_number)
                    else:
                        if check_for_symbols(input_data, current_number, row, col - 1):
                            part_numbers.append(current_number)
                            sum_of_part_numbers += int(current_number)

                    current_number = ''

    print('part one sum:', sum_of_part_numbers)
    return

# finds stars adjacent to the current number
# returns an array with all the adjacent star position recorded in 'xxxyyy' format
def find_nearby_stars(input_data, current_number, row, col):
    
    stars = []

    #up

    temp_row = row - 1
    temp_col = col - len(current_number)

    if temp_row >= 0 and temp_row < input_data.shape[0]:
        for i in range(temp_col, col + 2):
            if i >= 0 and i < input_data.shape[1]:
                if input_data[temp_row][i] == '*':
                    stars.append(f"{temp_row:03}{i:03}")

    #down
    
    temp_row = row + 1
    temp_col = col - len(current_number)

    if temp_row >= 0 and temp_row < input_data.shape[0]:
        for i in range(temp_col, col + 2):
            if i >= 0 and i < input_data.shape[1]:
                if input_data[temp_row][i] == '*':
                    stars.append(f"{temp_row:03}{i:03}")
    #left

    temp_col = col - len(current_number)

    if temp_col >= 0 and temp_col < input_data.shape[1]:
        if input_data[row][temp_col] == '*':
            stars.append(f"{row:03}{temp_col:03}")

    #right

    temp_col = col + 1

    if temp_col >= 0 and temp_col < input_data.shape[1]:
        if input_data[row][temp_col] == '*':
            stars.append(f"{row:03}{temp_col:03}")
    
    
    return stars

# works by finding a number first then finding its adjacent stars
# keeps track of stars and its adjacent part numbers
# if a star has exactly two adjacent part numbers then adds their product to sun 
def part_two(input_data):

    current_number = ''
    star_data = {}
    for row in range(input_data.shape[0]):
        for col in range(input_data.shape[1]):
            if input_data[row][col].isdigit():
                current_number += input_data[row][col]
            else:
                if current_number != '':
                    if col == 0:
                        stars_found = find_nearby_stars(input_data, current_number, row - 1, input_data.shape[1] - 1)
                    else:
                        stars_found = find_nearby_stars(input_data, current_number, row, col - 1)

                    for s in stars_found:
                        if star_data.get(s):
                            star_data[s].append(current_number)
                        else:
                            star_data[s] = [current_number]
                    current_number = ''

    part_two_sum = 0
    for star in star_data:
        if len(star_data[star]) == 2:
            part_two_sum += int(star_data[star][0]) * int(star_data[star][1])

    print('part two sum:', part_two_sum)
    return


y = []

#f = open('./sample_input.txt', 'r')
f = open('./puzzle_input.txt', 'r')

for line in f:
    x = []
    for letter in line:
        if letter != '\n':
            x.append(letter)
    
    y.append(x)

f.close()

data = np.array(y)

part_one(data)
part_two(data)