def a(input):
    tree = {} #folder: {size, folders} #keep track of each folders size
    res = [] #sum of all folders under 100k
    dirs = [] #in this folder
    curr_folder_stack = ['/'] #pointer, where we are
    for x in input[1:]:
        line = x.split()
        print(line)
        if line[0] == 'ls': #do nothing, just continue
            continue
        elif line[0] == 'dir': #dir discovered, add to stack
            dirs.append(line[1])
        elif line[1] == 'cd': #add or remove folder to curr_folder_stack
            if line[2] == '..':
                curr_folder_stack.remove()
        elif line[1] == 'ls':
            continue
        print(tree)
    return 1

def b(input):
    return 1

def f(line):
    #print('LINE', line)
    if '.' in line and line[-1] != '.':
        #print(line)
        return line
    return ''

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day6.txt','r')
    txt = txt_file.read()
    lines = txt.split("\n")
    #print(lines)

    print('a', a(lines))

    #a = [f(line) for line in lines]
    #b = [x for x in a if len(x) > 0]
    #c = sum([int(x.split(' ')[0]) for x in b])
    #print(c)
    #print('b', b(tmp_b))

if  __name__ == '__main__':
    main()

