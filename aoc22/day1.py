def a(cals):
    return max([sum(map(int, elf)) for elf in cals])

def b(cals):
    return sum(sorted([sum(map(int, elf)) for elf in cals])[-3:])

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day1.txt','r')
    txt = txt_file.read()
    rows = txt.split("\n\n")
    cals = [elf.split('\n') for elf in rows]
    
    print('a', a(cals))
    print('b', b(cals))

if  __name__ == '__main__':
  main()