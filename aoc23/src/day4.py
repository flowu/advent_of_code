def a(cards):
    score = 0
    for card in cards:
        player_nums, winning_nums = card
        correct_count = sum([player_num in winning_nums for player_num in player_nums])
        if correct_count > 0:
            score += pow(2, correct_count - 1)
    return score

def b(cards):
    count_table = {card: 1 for card in range(1, 193)}
    for idx, card in enumerate(cards, 1):
        player_nums, winning_nums = card
        matching_nums = sum([player_num in winning_nums for player_num in player_nums])
        tmp = idx + 1
        for _ in range(matching_nums):
            count_table[tmp] += 1 * count_table[idx]
            tmp += 1
    return sum(count_table.values())

def process_file(file_path, process_function, line_format_function):
    with open(file_path, "r") as f:
        lines = [line_format_function(line) for line in f.readlines()]
        return process_function(lines)

def format_a(line):
    _, nums = line.split(":")
    player_nums, winning_nums = nums.split("|")
    player_nums_lst = player_nums.split()
    winning_nums_lst = winning_nums.split()
    return (player_nums_lst, winning_nums_lst)

def format_b(line):
    pass

if __name__ == "__main__":
    ab_example = "data/day4/day4_example.txt"
    main_puzzle = "data/day4/day4.txt"

    res_a_example = process_file(
        ab_example, a, format_a
    )
    print("Example a:", res_a_example)

    res_a = process_file(
        main_puzzle, a, format_a
    )
    print("a:", res_a)

    #res_b_example = process_file(
    #    ab_example, b, format_a
    #)
    #print("Example b:", res_b_example)

    res_b = process_file(
        main_puzzle, b, format_a
    )
    print("b:", res_b)
