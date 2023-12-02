filename = 'source/../input/day3.txt'

def readFile():
    with open(filename) as f:
        wires = [line.rstrip('\n') for line in f]
        return wires

def calculate(wires):
    visited = []
    for wire in wires:
        visit = {}
        x, y = 0, 0
        steps = 0
        for elem in wire.split(","):
            direction = elem[0]
            distance = int (elem[1:])
            for i in range(distance):
                if direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                elif direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                steps += 1
                if (x, y) not in visit:
                    visit[(x, y)] = steps
        visited.append(visit)
    intersects = set(visited[0].keys()).intersection(set(visited[1].keys()))
    return min(abs(x)+abs(y) for (x,y) in intersects), min(visited[0][k] + visited[1][k] for k in intersects)

wires = readFile()
short = calculate(wires)
print(short)
