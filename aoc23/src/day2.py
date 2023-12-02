class Limit:
    RED = 12
    GREEN = 13
    BLUE = 14

def a(lines):
    tot = 0
    for ind, line in enumerate(lines, 1):
        valid = True
        for draw in line:
            for ball in draw:
                num, color = ball.split()
                num = int(num)
                if color == "blue" and num > Limit.BLUE:
                    valid = False
                elif color == "red" and num > Limit.RED:
                    valid = False
                elif color == "green" and num > Limit.GREEN:
                    valid = False
        if valid:
            tot += ind
    return tot

def b(lines):
    powers = []
    for line in lines:
        mem = {"red": 0, "blue": 0, "green": 0}
        for draw in line:
            for ball in draw:
                num, color = ball.split()
                num = int(num)
                if color == "blue" and num > mem["blue"]:
                    mem["blue"] = num
                elif color == "green" and num > mem["green"]:
                    mem["green"] = num
                elif color == "red" and num > mem["red"]:
                    mem["red"] = num
        powers.append(mem["red"] * mem["blue"] * mem["green"]) 
    return sum(powers)

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
    pass

if __name__ == "__main__":
    a_example = "data/day2/day2a_example.txt"
    b_example = "data/day2/day2b_example.txt"
    main_puzzle = "data/day2/day2.txt"

    res_a_example = process_file(
        a_example, a, format_a
    )
    print("Example a:", res_a_example)

    res_a = process_file(
        main_puzzle, a, format_a
    )
    print("a:", res_a)

    res_b_example = process_file(
        b_example, b, format_a
    )
    print("Example b:", res_b_example)

    res_b = process_file(
        main_puzzle, b, format_a
    )
    print("b:", res_b)
