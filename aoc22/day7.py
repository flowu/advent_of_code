def a(memory_mem):
    return sum(v for _, v in memory_mem.items() if v <= 100000)

def b(memory_mem):
    space_needed = memory_mem['/'] - 40000000
    filt = {k: v for k, v in memory_mem.items() if v >= space_needed}
    mini = min(filt.items(), key=lambda x: x[1])
    return mini[1]

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day7.txt','r')
    txt = txt_file.read()
    rows = txt.split("\n")

    stack_dir = [] #folders, fifo
    memory_mem = {} #{folder:size}
    for row in rows: #parse input
        row_sp = row.split()
        if '$ cd ..' in row:
            stack_dir = stack_dir[:-1]
        elif '$ cd' in row:
            dir_curr = row_sp[2]
            if len(stack_dir) == 0:
                dir = dir_curr
            elif len(stack_dir) == 1:
                dir = stack_dir[0] + dir_curr
            else:
                dir = stack_dir[-1] + '/' + dir_curr
            stack_dir.append(dir)
        elif row_sp[0].isnumeric():
            size = int(row_sp[0])
            for folder in stack_dir:
                if folder in memory_mem:
                    memory_mem[folder] += size
                else:
                    memory_mem[folder] = size
        #print(stack_dir)
        #print(memory_mem)
    
    print('a', a(memory_mem))
    print('b', b(memory_mem))

if  __name__ == '__main__':
    main()