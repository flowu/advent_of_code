symbols = "*#+$=/-&@%"

def a(lines):
    max_idx = len(lines) - 1
    max_ind = len(lines[0]) - 1
    res = 0
    #find index for numbers
    for idx, line in enumerate(lines):
        digit_indices = [i for i, char in enumerate(line) if char.isdigit()]
        b = find_adjacent_groups(digit_indices)
        for group in b:
            for ind in group:
                #look around digit for symbol
                if any((ind - 1 >= 0 and line[ind - 1] in symbols,
                    ind + 1 <= max_ind and line[ind + 1] in symbols,
                    idx - 1 >= 0 and ind - 1 >= 0 and lines[idx - 1][ind - 1] in symbols,
                    idx - 1 >= 0 and lines[idx - 1][ind] in symbols,
                    idx - 1 >= 0 and ind + 1 <= max_ind and lines[idx - 1][ind + 1] in symbols,
                    idx + 1 <= max_idx and ind - 1 >= 0 and lines[idx + 1][ind - 1] in symbols,
                    idx + 1 <= max_idx and lines[idx + 1][ind] in symbols,
                    idx + 1 <= max_idx and ind + 1 <= max_ind and lines[idx + 1][ind + 1] in symbols)):
                    res += int(''.join([line[i] for i in group]))
                    break
    return res

def b(lines):
    max_idx = len(lines) - 1
    max_ind = len(lines[0]) - 1
    res = 0
    #find index for numbers
    for idx, line in enumerate(lines):
        star_indices = [i for i, char in enumerate(line) if char == "*"]
        for star_index in star_indices:
            num_lst = []
            #left
            i = star_index
            num = ""
            while True:
                if i-1 >= 0 and line[i-1].isdigit():
                    num = line[i-1] + num
                    i -= 1
                else:
                    break
            if len(num) > 0:
                num_lst.append(int(num))

            #right
            i = star_index
            num = ""
            while True:
                if i+1 <= max_idx and line[i+1].isdigit():
                    num += line[i+1]
                    i += 1
                else:
                    break
            if len(num) > 0:
                num_lst.append(int(num))

            #above
            digit_indices = [i for i, char in enumerate(lines[idx-1]) if idx-1 >= 0 and char.isdigit()]
            b = find_adjacent_groups(digit_indices)
            for group in b:
                if any(digit in group for digit in [star_index-1, star_index, star_index+1]):
                    ad = int(''.join([lines[idx-1][i] for i in group]))
                    num_lst.append(ad)

            #under
            digit_indices = [i for i, char in enumerate(lines[idx+1]) if idx+1 <= len(lines)-1 and char.isdigit()]
            c = find_adjacent_groups(digit_indices)
            for group in c:
                if any(digit in group for digit in [star_index-1, star_index, star_index+1]):
                    af = int(''.join([lines[idx+1][i] for i in group]))
                    num_lst.append(af)

            if len(num_lst) == 2:
                res += num_lst[0] * num_lst[1]
    return res

def find_adjacent_groups(numbers):
    if not numbers:  # Check if the list is empty
        return []

    numbers = sorted(numbers)  # Sort the list to ensure it's in order
    groups = []
    current_group = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1] + 1:  # Check if the current number is adjacent to the previous one
            current_group.append(numbers[i])
        else:
            groups.append(current_group)
            current_group = [numbers[i]]

    groups.append(current_group)
    return groups

def process_file(file_path, process_function, line_format_function):
    with open(file_path, "r") as f:
        lines = [line_format_function(line) for line in f.readlines()]
        return process_function(lines)

def format_a(line):
    line = ''.join(line.strip().split())
    return line

def format_b(line):
    return line.strip()

if __name__ == "__main__":
    ab_example = "data/day3/day3_example.txt"
    main_puzzle = "data/day3/day3.txt"

    res_a_example = process_file(
        ab_example, a, format_a
    )
    print("Example a:", res_a_example)

    res_a = process_file(
        main_puzzle, a, format_a
    )
    print("a:", res_a)

    res_b_example = process_file(
        ab_example, b, format_b
    )
    print("Example b:", res_b_example)

    res_b = process_file(
        main_puzzle, b, format_b
    )
    print("b:", res_b)
