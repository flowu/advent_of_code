def a(lines):
    sum = 4
    for idx,ch in enumerate(lines[:-3]):
        print(idx)
        four = lines[idx:idx+4]
        print(list(four))
        print(set(four))
        if len(set(four)) == len(four):
            break
        sum += 1
    return sum

def b(lines):
    sum = 14
    for idx,ch in enumerate(lines[:-13]):
        print(idx)
        four = lines[idx:idx+14]
        print(list(four))
        print(set(four))
        if len(set(four)) == len(four):
            break
        sum += 1
    return sum

def main():
    with open(r"/Users/claudia/Desktop/aoc/day6.txt") as file:
        lines = ''.join([line for line in file])
    print('a', a(lines))
    print('b', b(lines))

if  __name__ == '__main__':
    main()