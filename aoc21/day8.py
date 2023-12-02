def a(input):
    acc = 0
    for line in input:
        digs = line[1].split()
        acc += sum([len(dig) in [2, 3, 4, 7] for dig in digs])
    return acc

def b(input):
    sum = 0
    for line in input:
        digs = line[0].split()
        [one] = filter(lambda x: len(x)==2, digs)
        [seven] = filter(lambda x: len(x)==3, digs)
        [four] = filter(lambda x: len(x)==4, digs)
        [eight] = filter(lambda x: len(x)==7, digs)

        len_five = list(filter(lambda x: len(x)==5, digs))
        [three] = [num for num in len_five if contains_all(one, num)]
        len_five.remove(three)
        five = get_five(len_five, four)
        len_five.remove(five)
        [two] = len_five

        len_six = list(filter(lambda x: len(x)==6, digs))
        [six] = [num for num in len_six if not contains_all(seven, num)]
        len_six.remove(six)
        [nine] = [num for num in len_six if contains_all(four, num)]
        len_six.remove(nine)
        [zero] = len_six
        tran = {''.join(sorted(zero)):0, ''.join(sorted(one)):1, ''.join(sorted(two)):2, ''.join(sorted(three)):3, ''.join(sorted(four)):4,
                ''.join(sorted(five)):5, ''.join(sorted(six)):6, ''.join(sorted(seven)):7, ''.join(sorted(eight)):8, ''.join(sorted(nine)):9}
        num = translate(line[1].split(), tran)
        sum += num
    return sum

def contains_all(set, str):
    return 0 not in [c in str for c in set]

def get_five(lst, four):
    count_matches = [y in four for y in lst[0]].count(True)
    return lst[0] if (count_matches == 3) else lst[1]

def translate(digs, tran):
    num = [str(tran[''.join(sorted(dig))]) for dig in digs]
    return int(''.join(num))

def main():
    with open('/Users/claudia/Desktop/aoc/input8.txt','r') as file:
        all = file.read()
        lines = all.split('\n')
        input = [line.split(' | ') for line in lines]
    
    print('a', a(input))
    print('b', b(input))

if  __name__ == '__main__':
  main()