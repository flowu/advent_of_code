def f(karta, input, h, ts):
    dirs = {'R': (0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    tail = {(-2,2): (-1,1), (2,-2): (1,-1), (-2,-2): (-1,-1), (2,2): (1,1), (0,2): (0,1), (0,-2): (0,-1), (2,0): (1,0), (-2,0): (-1,0), (-2,1): (-1,1), (-1,2): (-1,1), (-1,-2): (-1,-1), (-2,-1): (-1,-1), (2,-1): (1,-1), (1,-2): (1,-1), (1,2): (1,1), (2,1): (1,1)}
    for row in input:
        (dir, steps) = row.split()
        for _ in range(int(steps)):
            #move head
            h = tuple(map(sum, zip(h, dirs[dir])))
            #move first tail
            dif = tuple(h1 - t1 for h1, t1 in zip(h, ts[0]))
            if dif in tail:
                ts[0] = tuple(map(sum, zip(ts[0], tail[dif])))

            for idx,t in enumerate(ts[1:]): # move every other tail
                dif = tuple(t0 - t1 for t0, t1 in zip(ts[idx], t))
                if dif in tail:
                    ts[idx+1] = tuple(map(sum, zip(t, tail[dif])))
            #Add mark in map where last tail has been
            karta[ts[-1][0]] = karta[ts[-1][0]][:ts[-1][1]] + '#' + karta[ts[-1][0]][ts[-1][1]+1:]

            #debug printouts
            #print('\n'.join(karta) + '\n')
            #kar = ['.' * 30 for y in range(24)]
            #for i in range(9):
                #a = 8-i
                #kar[ts[a][0]] = kar[ts[a][0]][:ts[a][1]] + str(a) + kar[ts[a][0]][ts[a][1]+1:]
            #kar[h[0]] = kar[h[0]][:h[1]] + 'H' + kar[h[0]][h[1]+1:]
            #print('\n'.join(kar))
    res = sum([x.count('#') for x in karta])
    return res

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day9.txt','r')
    txt = txt_file.read()
    input = txt.split("\n")

    karta = ['.' * 1000 for _ in range(1000)]
    h = ((len(karta)-1)//2,(len(karta[0])-1)//2)
    ts = [((len(karta)-1)//2,(len(karta[0])-1)//2) for _ in range(9)]
    karta[ts[-1][0]] = karta[ts[-1][0]][:ts[-1][1]] + '#' + karta[ts[-1][0]][ts[-1][1]+1:]

    print('a', f(karta, input, h, ts[:1]))
    karta = ['.' * 1000 for _ in range(1000)]
    karta[ts[-1][0]] = karta[ts[-1][0]][:ts[-1][1]] + '#' + karta[ts[-1][0]][ts[-1][1]+1:]
    print('b', f(karta, input, h, ts))

if  __name__ == '__main__':
    main()