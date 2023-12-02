def a(rows):
    cycle, res_tmp, res = 0, 1, 0
    add_operation = False
    while cycle < 227:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            res += cycle * res_tmp
        if add_operation:
            res_tmp += row_i
            add_operation = False
            continue
        row = rows.pop(0)
        if row.lstrip('-').isnumeric():
            row_i = int(row)
            add_operation = True
    return res

def b(rows):
    cycle, sprite, res = 0, [0,1,2], ''
    add_operation = False
    while cycle < 240:
        if cycle % 40 in sprite:
            res += '#'
        else:
            res += '.'
        cycle += 1
        if add_operation:
            row_i = int(row)
            mid = sprite[1]
            sprite = [row_i+mid-1, row_i+mid, row_i+mid+1]
            add_operation = False
            continue
        row = rows.pop(0)
        if row.lstrip('-').isnumeric():
            add_operation = True
    return '\n'.join([res[i:i+40] for i in range(0, len(res), 40)])

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day10.txt','r')
    txt = txt_file.read()
    rows_mod = [row.split()[1] if len(row.split()) == 2 else row for row in txt.split('\n')]
    rows_mod2 = rows_mod.copy()

    print('a', a(rows_mod))
    print('b\n', b(rows_mod2))

if  __name__ == '__main__':
    main()