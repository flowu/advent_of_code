def a(input):
    return 1

def b(input):
    return 1

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day11.txt','r')
    txt = txt_file.read()
    input = txt.split("\n")

    print('a', a(input))
    print('b', b(input))

if  __name__ == '__main__':
    main()