def a(lines):
    x = sum([x[1] for x in lines if x[0] == 'forward'])
    y = sum([-x[1] if x[0] == 'up' else x[1] if x[0] == 'down' else 0 for x in lines])
    return x*y

def b(lines):
    aim, x, y = 0, 0, 0
    for elem in lines:
        (dir, val) = (elem[0], elem[1])
        if dir == 'down':
            aim += val
        elif dir == 'up':
            aim -= val
        else:
            x += val
            y += val*aim
    return x*y

def main():
    with open('C:/Users/Joel/Desktop/advent_of_code/input2.txt','r') as file:
        lines = [[line.split()[0], int(line.split()[1].strip())] for line in file]
    
    print('a', a(lines))
    print('b', b(lines))

if  __name__ == '__main__':
  main()