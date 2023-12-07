
def part_one(times, distances):

    win_count_total = 1
    for i in range(len(times)):
        win_count = 0
        for j in range(times[i]):
            speed = j

            elasped_time = j

            time_left = times[i] - elasped_time

            distance_travelled = speed * time_left

            #print(f"speed {speed} and distance travelled {distance_travelled}")

            if distance_travelled > distances[i]:
                win_count += 1

        win_count_total *= win_count

    print(win_count_total)
    return


times = [7, 15, 30]
distances = [9, 40, 200]

#part 1
times = [60, 80, 86, 76]
distances = [601, 1163, 1559, 1300]

part_one(times, distances)

#part 2
# not sure about efficiency 
# works with part one code
times = [60808676]
distances = [601116315591300]

part_one(times, distances)