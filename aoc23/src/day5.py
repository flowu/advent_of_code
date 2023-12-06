def a(lines):
    pass

def b(lines):
    pass

def process_file(file_path, process_function, line_format_function):
    with open(file_path, "r") as f:
        lines = [line_format_function(line) for line in f.readlines()]
        return process_function(lines)

def format_a(line):
    pass

def format_b(line):
    pass

if __name__ == "__main__":
    ab_example = "data/day5/day5_example.txt"
    main_puzzle = "data/day5/day5.txt"

    res_a_example = process_file(
        ab_example, a, format_a
    )
    print("Example a:", res_a_example)

    #res_a = process_file(
    #    main_puzzle, a, format_a
    #)
    #print("a:", res_a)

    #res_b_example = process_file(
    #    ab_example, b, format_a
    #)
    #print("Example b:", res_b_example)

    #res_b = process_file(
    #    main_puzzle, b, format_a
    #)
    #print("b:", res_b)
