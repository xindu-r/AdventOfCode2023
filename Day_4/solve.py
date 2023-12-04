
def part_one(games_data):

    points  = 0
    for game in games_data:
        winning_data, playing_data = game.split('|')

        winning_numbers = [int(i) for i in winning_data.split(' ') if i.isdigit()]
        playing_numbers = [int(i) for i in playing_data.split(' ') if i.isdigit()]

        number_of_matches = 0
        for number in winning_numbers:
            if number in playing_numbers:
                number_of_matches += 1
        
        if number_of_matches == 0:
            points += 0
        else:
            points += 2 ** (number_of_matches - 1)
        
        
    print('total points:', points)
    return

def part_two(games_data):

    # card number, number of instances
    game_dict = { i: 1 for i in range(1, len(games_data) + 1)}
    game_counter = 1
    for game in games_data:
        winning_data, playing_data = game.split('|')

        winning_numbers = [int(i) for i in winning_data.split(' ') if i.isdigit()]
        playing_numbers = [int(i) for i in playing_data.split(' ') if i.isdigit()]

        number_of_matches = 0
        for number in winning_numbers:
            if number in playing_numbers:
                number_of_matches += 1
        
        for match in range(1, number_of_matches + 1):
            game_dict[game_counter + match] += 1 * game_dict[game_counter]
     
        game_counter += 1

    number_game_cards = 0
    for g in game_dict:
        number_game_cards += game_dict[g]

    print('total number of scratchcards:', number_game_cards)

    return

#f = open('./sample_input.txt','r')
f = open('./puzzle_input.txt','r')

#parse input
games = []
for line in f:
    games.append(line.strip('\n').split(':')[1])

f.close()

part_one(games)
part_two(games)