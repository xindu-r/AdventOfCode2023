from functools import cmp_to_key

def compare_func(str1, str2):
    val = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    for i in range(5):
        if val.index(str2[i]) < val.index(str1[i]):
            return 1
        
        if val.index(str1[i]) < val.index(str2[i]):
            return -1
    return 0

def compare_func_part_2(str1, str2):
    val = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    for i in range(5):
        if val.index(str2[i]) < val.index(str1[i]):
            return 1
        
        if val.index(str1[i]) < val.index(str2[i]):
            return -1
    return 0

def part_one(input_data):

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for hand in input_data:
        count_dict = {}
        for letter in hand[0]:
            if count_dict.get(letter):
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

        hb = hand[0] + hand[1]
        
        count_dict_length = len(count_dict)

        if count_dict_length == 5:
            high_card.append(hb)
        elif count_dict_length == 4:
            one_pair.append(hb)
        elif count_dict_length == 3:
            if max(count_dict.values()) == 3:
                three_of_a_kind.append(hb)
            else:
                two_pair.append(hb)
        elif count_dict_length == 2:
            if max(count_dict.values()) == 4:
                four_of_a_kind.append(hb)
            else:
                full_house.append(hb)
        elif count_dict_length == 1:
            five_of_a_kind.append(hb)

    sorted_list = (sorted(high_card, key=cmp_to_key(compare_func))
                    + sorted(one_pair, key=cmp_to_key(compare_func))
                    + sorted(two_pair, key=cmp_to_key(compare_func))
                    + sorted(three_of_a_kind, key=cmp_to_key(compare_func))
                    + sorted(full_house, key=cmp_to_key(compare_func))
                    + sorted(four_of_a_kind, key=cmp_to_key(compare_func))
                    + sorted(five_of_a_kind, key=cmp_to_key(compare_func)) )
    

    rank = 1
    total_winning  = 0

    for i in range(len(sorted_list)):
        bet = int(sorted_list[i][5:])
        total_winning += rank * bet
        rank += 1

    print(f"part 1 total winnings: {total_winning}")
                    
    return

def part_two(input_data):

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    for hand in input_data:
        count_dict = {}
        for letter in hand[0]:
            if count_dict.get(letter):
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

        hb = hand[0] + hand[1]
        
        count_dict_length = len(count_dict)

        if count_dict_length == 5:
            if count_dict.get('J'):
                one_pair.append(hb)
            else:
                high_card.append(hb)
        elif count_dict_length == 4:
            if count_dict.get('J'):
                three_of_a_kind.append(hb)
            else:
                one_pair.append(hb)
        elif count_dict_length == 3:
            if count_dict.get('J') and count_dict['J'] == 1:
                if max(count_dict.values()) == 3:
                    four_of_a_kind.append(hb)
                else:
                    full_house.append(hb)
            elif count_dict.get('J') and count_dict['J'] >= 2:
                four_of_a_kind.append(hb)
            else:
                if max(count_dict.values()) == 3:
                    three_of_a_kind.append(hb)
                else:
                    two_pair.append(hb)
        elif count_dict_length == 2:
            if count_dict.get('J'):
                five_of_a_kind.append(hb)
            else:
                if max(count_dict.values()) == 4:
                    four_of_a_kind.append(hb)
                else:
                    full_house.append(hb)
        elif count_dict_length == 1:
            five_of_a_kind.append(hb)


    sorted_list = (sorted(high_card, key=cmp_to_key(compare_func_part_2))
                    + sorted(one_pair, key=cmp_to_key(compare_func_part_2))
                    + sorted(two_pair, key=cmp_to_key(compare_func_part_2))
                    + sorted(three_of_a_kind, key=cmp_to_key(compare_func_part_2))
                    + sorted(full_house, key=cmp_to_key(compare_func_part_2))
                    + sorted(four_of_a_kind, key=cmp_to_key(compare_func_part_2))
                    + sorted(five_of_a_kind, key=cmp_to_key(compare_func_part_2)) )
    

    rank = 1
    total_winning  = 0

    for i in range(len(sorted_list)):
        bet = int(sorted_list[i][5:])
        total_winning += rank * bet
        rank += 1

    print(f"part 2 total winnings: {total_winning}")
                    
    return

#f = open('sample_input.txt', 'r')
f = open('puzzle_input.txt', 'r')

hands_and_bets = []
for line in f:
    hands_and_bets.append(line.strip('\n').split(' '))

f.close()

part_one(hands_and_bets)
part_two(hands_and_bets)