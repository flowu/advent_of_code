def fun(input):
    return sum(ord(ch) - 96 if ch.islower() else ord(ch) - 38 for ch in input)

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day3.txt','r')
    txt = txt_file.read()
    backpacks = txt.split("\n")

    tmp_a = [list(set(compartments[:len(compartments)//2]) & set(compartments[len(compartments)//2:]))[0] for compartments in backpacks]
    tmp_b = [list(set(fst) & set(snd) & set(thrd))[0] for (fst, snd, thrd) in zip(*[iter(backpacks)]*3)]

    print('a', fun(tmp_a))
    print('b', fun(tmp_b))

if  __name__ == '__main__':
    main()
