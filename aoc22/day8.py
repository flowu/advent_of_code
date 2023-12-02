def a(input):
    size = len(input)
    grid = [[0] * size for _ in range(size)]
    #sweep a look from left view, mark tree as viewed if visible
    grid = help_fun(grid, input)
    
    #rotate grids
    input_top = rotate(input)
    grid_top = rotate(grid)
    grid_top2 = [list(x) for x in grid_top]
    #top view
    grid = help_fun(grid_top2, input_top)

    #rotate grids
    input_right = rotate(input_top)
    grid_right = rotate(grid)
    grid_right2 = [list(x) for x in grid_right]
    #bottom view
    grid = help_fun(grid_right2, input_right)

    #rotate grids
    input_bottom = rotate(input_right)
    grid_bottom = rotate(grid)
    grid_bottom2 = [list(x) for x in grid_bottom]
    #bottom view
    grid = help_fun(grid_bottom2, input_bottom)

    return sum([sum(x) for x in grid])

def b(input):
    size = len(input)
    grid = [[1] * size for _ in range(size)]
    for idx,row in enumerate(input):
        row_i = list(row)
        for idy,tree in enumerate(row_i[1:-1], 1):
            left_trees = row_i[:idy]
            right_trees = row_i[idy+1:]
            left_inv = left_trees[::-1]
            c_left = count_trees(left_inv, tree)
            c_right = count_trees(right_trees, tree)
            grid[idx][idy] *= c_left * c_right

    grid1 = rotate(grid)
    grid = [list(x) for x in grid1]
    input = rotate(input)
    for idx,row in enumerate(input):
        row_i = list(row)
        for idy,tree in enumerate(row_i[1:-1], 1):
            left_trees = row_i[:idy]
            right_trees = row_i[idy+1:]
            left_inv = left_trees[::-1]
            c_left = count_trees(left_inv, tree)
            c_right = count_trees(right_trees, tree)
            grid[idx][idy] *= c_left * c_right

    return max(map(max, grid))

def count_trees(li, tree):
    count_visible = 0
    for tree_list in li:
        count_visible += 1
        if tree <= tree_list:
            break
    return count_visible

def rotate(grid):
    return list(zip(*grid[::-1]))

def help_fun(grid, input):
    for idx,row in enumerate(input):
        row_i = list(row)
        grid[idx][0] = 1
        height = row_i[0]
        for idy,tree in enumerate(row_i[1:], 1):
            if tree > height:
                height = tree
                grid[idx][idy] = 1
    return grid

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day8.txt','r')
    txt = txt_file.read()
    rows = txt.split("\n")

    print('a', a(rows))
    print('b', b(rows))

if  __name__ == '__main__':
    main()
