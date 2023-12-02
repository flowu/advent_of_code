def a(lines):
    pass

def b(lines):
    pass

def process_file(file_path, process_function, line_format_function):
    with open(file_path, "r") as f:
        lines = [line_format_function(line) for line in f.readlines()]
        return process_function(lines)

def format_a(line):
    line = line.strip().split(':')
    draws = line[1].split(";")
    draws = [draw.split(",") for draw in draws]
    draws = [[ball.strip() for ball in draw] for draw in draws]
    return draws

def format_b(line):
    return line.strip()

if __name__ == "__main__":
    a_example = "data/day3/day3a_example.txt"
    b_example = "data/day3/day3b_example.txt"
    main_puzzle = "data/day3/day3.txt"

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
