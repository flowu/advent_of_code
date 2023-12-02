def a(lines):
    return 11

def b(lines):
    return 11

def main():
    f = open("/Users/claudia/Desktop/aoc/day11.txt", "r")
    e = f.read().split('\n\n')
    g = [x.split('\n') for x in e]
    
    print(g)

    print('a', a(f))
    print('b', b(f))

if  __name__ == '__main__':
    main()