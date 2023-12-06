def part_one_for_small_numbers(data_map):

    expanded_map = {}
    for key in data_map:
        if key != 'seeds':
            expanded_map[key] = {}

            for m in data_map[key]:
                source = [i for i in range(m[1], m[1] + m[2])]
                destination = [i for i in range(m[0], m[0] + m[2])]

                expanded_map[key].update(dict(zip(source, destination)))

            expanded_map[key] = dict(sorted(expanded_map[key].items()))

    for seed in data_map['seeds']:

        soil = expanded_map['seed-to-soil'].get(seed, seed)
        fertilizer = expanded_map['soil-to-fertilizer'].get(soil, soil)
        water = expanded_map['fertilizer-to-water'].get(fertilizer, fertilizer)
        light = expanded_map['water-to-light'].get(water, water)
        temperature = expanded_map['light-to-temperature'].get(light, light)
        humidity = expanded_map['temperature-to-humidity'].get(temperature, temperature)
        location = expanded_map['humidity-to-location'].get(humidity, humidity)

        print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.")

    return

def part_one(data_map):

    #seed_to_location_list = []
    location_list = []
    for seed in data_map['seeds']:
        seed_to_location = [seed]
        current_key = seed

        for key in data_map:
            if key != 'seeds':
                for m in data_map[key]:
                    r = current_key - m[1]
                    if r >= 0 and r < m[2]:
                        current_key = m[0] + r
                        break
                seed_to_location.append(current_key)
        #seed_to_location_list.append(seed_to_location)
        location_list.append(current_key)

    print("minimum location is : ", min(location_list))
    return

def find_new_ranges(current_range, new_map):

    return_ranges = []
    r = current_range[0] - new_map[1]

    if r >= 0:
        if current_range[1] <= new_map[2]:
            return_ranges.append((new_map[0] + r, current_range[1]))
        else:
            return_ranges.append((new_map[0] + r, new_map[2]))
            return_ranges.append((current_range[0] + new_map[2], current_range[1] - new_map[2]))

    if len(return_ranges) > 0:
        return return_ranges

    return [current_range]

def part_two(data_map):

    #generate seeds

    seeds = data_map.pop('seeds')

    print(seeds)
    print(data_map)

    s = 0
    while s < len(seeds):
        current_range = (seeds[s], seeds[s + 1])

        print(current_range)
        s += 2
    return

f = open('./sample_input.txt', 'r')
#f = open('./puzzle_input.txt', 'r')

input_data = {}

current_map = ''
for line in f:
    if line.startswith('seeds:'):
        input_data['seeds'] = [int(i) for i in line.strip('\n').split(':')[1].split(' ') if i.isdigit()]
    elif line.startswith('seed-to-soil'):
        current_map = 'seed-to-soil'
        input_data['seed-to-soil'] = []
    elif line.startswith('soil-to-fertilizer'):
        current_map = 'soil-to-fertilizer'
        input_data['soil-to-fertilizer'] = []
    elif line.startswith('fertilizer-to-water'):
        current_map = 'fertilizer-to-water'
        input_data['fertilizer-to-water'] = []
    elif line.startswith('water-to-light'):
        current_map = 'water-to-light'
        input_data['water-to-light'] = []
    elif line.startswith('light-to-temperature'):
        current_map = 'light-to-temperature'
        input_data['light-to-temperature'] = []
    elif line.startswith('temperature-to-humidity'):
        current_map = 'temperature-to-humidity'
        input_data['temperature-to-humidity'] = []
    elif line.startswith('humidity-to-location'):
        current_map = 'humidity-to-location'
        input_data['humidity-to-location'] = []
    else:
        if line.strip('\n') != '':
            input_data[current_map].append([int(i) for i in line.strip('\n').split(' ') if i.isdigit()])

f.close()

#print(input_data)
#part_one_for_small_numbers(input_data)
part_one(input_data)
part_two(input_data)