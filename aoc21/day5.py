def a(grid, input):
    #filter, keep horizontal and vertical lines
    for pair in input:
        if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]:
            fix = pair[0][0] if pair[0][0] == pair[1][0] else pair[0][1]
            mov = 0 if pair[0][0] != pair[1][0] else 1
            low = pair[0][mov] if pair[0][mov] < pair[1][mov] else pair[1][mov]
            high = pair[1][mov] if low == pair[0][mov] else pair[0][mov]
            new = [(fix,mov) if pair[0][0] == pair[1][0] else (mov,fix) for mov in range(low, high+1)]
            for x in new:
                grid[x[1]][x[0]] = grid[x[1]][x[0]] + 1

    overlaps = [True if elem > 1 else False for row in grid for elem in row].count(True)
    return (overlaps, grid)

def b(grid, input):
    for pair in input:
        if pair[0][0] != pair[1][0] and pair[0][1] != pair[1][1]:
            1
    return 0

def main():
    with open('/Users/claudia/Desktop/aoc/input5.txt','r') as file:
        r = file.read()
        raw = r.split('\n')

    lines = [x.split(' -> ') for x in raw]

    lines_tuple = []

    for line in lines:
        start = tuple(map(int, line[0].split(',')))
        end = tuple(map(int, line[1].split(',')))
        lines_tuple.append([start, end])

    #print(lines_tuple)

    #print('example a',a(parsed))
    #print('example b',b(0))

    grid = [[0]*1000 for _ in range(1000)]
    #print(grid)
    
    (overlaps, grid_a) = a(grid, lines_tuple)
    print('a', overlaps)
    print('b', b(grid_a, lines_tuple))

if  __name__ == '__main__':
  main()