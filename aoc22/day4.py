def a(lines):
    # example
    # 23..
    # ..45
    # line[0] 2 <= 4 line[2]
    # line[1] 3 >= 5 line[3]
    # line[0] 2 >= 4 line[2]
    # line[1] 3 <= 5 line[3]
    # (True and False) or (False and True)
    return sum(True if (line[0] <= line[2] and line[1] >= line[3]) or (line[0] >= line[2] and line[1] <= line[3])
                    else False
                    for line in lines)

def b(lines):
    return sum(True if set(range(line[0], line[1] + 1)) & set(range(line[2], line[3] + 1))
                    else False
                    for line in lines)

def main():
    with open(r"/Users/claudia/Desktop/aoc/day4.txt") as file:
        lines = [line.strip().replace('-', ',') for line in file]
        lines1 = [line.split(',') for line in lines]
        lines2 = [[int(i) for i in line] for line in lines1]

    print('a', a(lines2))
    print('b', b(lines2))

if  __name__ == '__main__':
    main()