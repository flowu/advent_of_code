def a(q):
    w = ''.join(q)
    #invert
    e = ''.join('1' if x == '0' else '0' for x in w)
    return int(w,2) * int(e,2)

def b(r):
    f1 = lambda x, i, dig: x[i] == dig or (dig == 'eq' and x[i] == '1')
    f2 = lambda x, i, dig: (x[i] != dig and x[i] in '01' and dig in '01') or (dig == 'eq' and x[i] == '0')
    o = solve(r, f1)
    p = solve(r, f2)
    return o * p

def solve(r, f):
    t = r
    i = 0
    while(len(t) > 1):
        s = most_common_bits(t)
        dig = s[i]
        t = [x for x in t if f(x, i, dig)]
        i += 1
    return int(''.join(t),2)

def most_common_bits(input):
    r = [line for line in zip(*input)]
    s = len(r[0])
    return ['1' if 2*x.count('1') > s else '0' if 2*x.count('1') < s else 'eq' for x in r]

def main():
    with open('/Users/claudia/Desktop/aoc/input3.txt','r') as file:
        r = file.read()
        raw = r.split()

    print('example b',b(['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']))
    
    print('a', a(most_common_bits(raw)))
    print('b', b(raw))

if  __name__ == '__main__':
  main()