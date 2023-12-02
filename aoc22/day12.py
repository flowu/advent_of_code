def a(map, Sx, Sy, Ex, Ey): #possible improvement: iterate over directions to make it simpler
    weights = [[4200] * len(map[0])  for _ in range(len(map))]
    weights[Sx][Sy] = 0
    visited = []
    neighbors = [(Sx, Sy)]
    
    while neighbors:
        #add curr to visited
        curr = neighbors.pop(0)
        visited.append(curr)
        if curr == (Ex, Ey):
            break
        #add to neighbors and add to weights
        left, right, up, down = (curr[0], curr[1]-1), (curr[0], curr[1]+1), (curr[0]-1, curr[1]), (curr[0]+1, curr[1])
        
        if (left[1] >= 0 and left not in neighbors and left not in visited and ord(map[curr[0]][curr[1]]) + 2 > ord(map[left[0]][left[1]])) or map[curr[0]][curr[1]] == 'S':
            if left != (Ex, Ey) or map[curr[0]][curr[1]] in 'yz':
                neighbors.append(left)
                weights[left[0]][left[1]] = weights[curr[0]][curr[1]] + 1
        if (right[1] < len(map[0]) and right not in neighbors and right not in visited and ord(map[curr[0]][curr[1]]) + 2 > ord(map[right[0]][right[1]])) or map[curr[0]][curr[1]] == 'S':
            if right != (Ex, Ey) or map[curr[0]][curr[1]] in 'yz':
                neighbors.append(right)
                weights[right[0]][right[1]] = weights[curr[0]][curr[1]] + 1
        if (up[0] >= 0 and up not in neighbors and up not in visited and ord(map[curr[0]][curr[1]]) + 2 > ord(map[up[0]][up[1]])) or map[curr[0]][curr[1]] == 'S':
            if up != (Ex, Ey) or map[curr[0]][curr[1]] in 'yz':
                neighbors.append(up)
                weights[up[0]][up[1]] = weights[curr[0]][curr[1]] + 1
        if (down[0] < len(map) and down not in neighbors and down not in visited and ord(map[curr[0]][curr[1]]) + 2 > ord(map[down[0]][down[1]])) or map[curr[0]][curr[1]] == 'S':
            if down != (Ex, Ey) or map[curr[0]][curr[1]] in 'yz':
                neighbors.append(down)
                weights[down[0]][down[1]] = weights[curr[0]][curr[1]] + 1
    return weights[Ex][Ey]

def b(map, Ex, Ey):
    #find all starting positions
    a_and_S = []
    for idx,row in enumerate(map):
        for idy,col in enumerate(row):
            if map[idx][idy] in 'aS':
                a_and_S.append((idx,idy))
    #seed function a with all starting positions, return smallest
    return min([a(map, x[0], x[1], Ex, Ey) for x in a_and_S])

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day12.txt','r')
    txt = txt_file.read()
    map = txt.split()
    
    Sx, Sy = 0, 0
    Ex, Ey = 0, 0
    for idx,row in enumerate(map):
        for idy,ch in enumerate(row):
            if ch == 'S':
                Sx, Sy = idx, idy
            if ch == 'E':
                Ex, Ey = idx, idy

    print('a', a(map, Sx, Sy, Ex, Ey))
    print('b', b(map, Ex, Ey))

if  __name__ == '__main__':
    main()