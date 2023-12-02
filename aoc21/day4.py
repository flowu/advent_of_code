def a(nums, boards):
    #print('before',boards)
    for draw in nums:
        for i,board in enumerate(boards):
            #print('board',board)
            board_noted_draw = ['x' if x == draw else x for x in board]
            boards[i] = board_noted_draw
            won = five_in_a_row(board_noted_draw)
            if won:
                #print(board_noted_draw)
                s = sum([int(x) for x in board_noted_draw if x != 'x'])
                return s * int(draw)
    return "no win"

def five_in_a_row(board):
    rows = [board[x:x+5] for x in range(0,len(board),5)]
    #print('rows',rows)
    cols = [board[x:len(board):5] for x in range(5)]
    #print('cols',cols)
    return True if ['x','x','x','x','x'] in rows or ['x','x','x','x','x'] in cols else False

def b(nums, boards):
    #print('before',boards)
    for draw in nums:
        if draw == '93':
            print(boards)
        for i,board in enumerate(boards):
            #print('board',board)
            board_noted_draw = ['x' if x == draw else x for x in board]
            won = five_in_a_row(board_noted_draw)
            if won and len(boards) == 1:
                #print(boards[0])
                #print(board_noted_draw)
                s = sum([int(x) for x in board_noted_draw if x != 'x'])
                #print(draw)
                return s * int(draw)
            elif won:
                boards.remove(board)
            else:
                boards[i] = board_noted_draw
    return "out of boards error"

def main():
    with open('/Users/claudia/Desktop/aoc/input4.txt','r') as file:
        r = file.read()
        raw = r.split('\n\n')

    numbers = raw[0].split(',')
    boards_string = raw[1:]
    boards_list = [board.split() for board in boards_string]

    #print('example a',a(0))
    #print('example b',b(0))
    
    print('a', a(numbers, boards_list))
    print('b', b(numbers, boards_list))

if  __name__ == '__main__':
  main()