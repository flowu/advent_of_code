def a(stack, procedure):
    for proc in procedure:
        move, fromm, to = int(proc[0]), int(proc[1]), int(proc[2])
        stack[to-1] += stack[fromm-1][-move:][::-1]
        stack[fromm-1] = stack[fromm-1][:-move]
        #print(stack)
    return ''.join([x[-1:] for x in stack])

def b(stack, procedure):
    for proc in procedure:
        move, fromm, to = int(proc[0]), int(proc[1]), int(proc[2])
        stack[to-1] += stack[fromm-1][-move:]
        stack[fromm-1] = stack[fromm-1][:-move]
        #print(stack)
    return ''.join([x[-1:] for x in stack])

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day5.txt','r')
    txt = txt_file.read()
    input = txt.split("\n\n")
    stack = input[0]
    #print(txt)
    stack2 = stack.split('\n')
    mod = list(zip(*stack2))[1::4]
    #print(mod)
    stack3 = [''.join(reversed(row)).rstrip() for row in mod]
    #print(stack3)
    procedure1 = input[1].split('\n')
    #print(procedure1)
    procedure = [list(filter(lambda z : z.isdigit(), x.split())) for x in procedure1]
    #print(procedure)

    tmp = stack3.copy()
    print('a', a(stack3, procedure))
    #print(stack3)
    print('b', b(tmp, procedure))

if  __name__ == '__main__':
    main()
