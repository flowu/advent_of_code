numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
           "one", "two", "three", "four", "five", "six",
           "seven", "eight", "nine"]

trans = {"one": "1", "two": "2", "three": "3", "four": "4",
         "five": "5", "six": "6", "seven": "7", "eight": "8",
         "nine": "9"}

def a(lines):
    tot = 0
    for line in lines:
        nums = list(filter(str.isnumeric, line))
        tot += int(nums[0] + nums[-1])
    return tot

def b(lines):
    tot = 0
    for line in lines:
        left_most = find_first_last_number(line.find, min)
        right_most = find_first_last_number(line.rfind, max)

        tot += int(left_most + right_most)
    return tot

def find_first_last_number(find_fun, min_max_fun):
    # Find left/right most indices of each number
    left_res = {}
    for num in numbers:
        index = find_fun(num)
        if index >= 0:
            left_res[index] = num

    # Find most left/right most number
    lowest_index = min_max_fun(left_res.keys())
    result_string = left_res[lowest_index]

    # Transform any text number to digit number
    if not str.isnumeric(result_string):
        result_string = trans[result_string]
    return result_string

def process_file(file_path, process_function, line_format_function):
    with open(file_path, "r") as f:
        lines = [line_format_function(line) for line in f.readlines()]
        return process_function(lines)

def format_a(line):
    return line.strip()

def format_b(line):
    return line.strip()

if __name__ == "__main__":
    a_example = "data/day1/day1a_example.txt"
    b_example = "data/day1/day1b_example.txt"
    main_puzzle = "data/day1/day1.txt"

    res_a_example = process_file(
        a_example, a, format_a
    )
    print("Example a:", res_a_example)

    res_a = process_file(
        main_puzzle, a, format_a
    )
    print("a:", res_a)

    res_b_example = process_file(
        b_example, b, format_b
    )
    print("Example b:", res_b_example)

    res_b = process_file(
        main_puzzle, b, format_b
    )
    print("b:", res_b)
