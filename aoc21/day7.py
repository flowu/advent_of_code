def a(input):
    fuels = []
    for goal in range(1400):
        fuel = sum([abs(pos - goal) for pos in input])
        fuels.append(fuel)
    return min(fuels)

def b(input):
    fuels = []
    #fuel for each x position
    for goal in range(2000):
        fuel = []
        #fuel for each crabonaut
        for crabonaut in input:
            crab_fuel = abs(crabonaut-goal)*(abs(crabonaut-goal)+1)/2
            fuel.append(crab_fuel)
        fuels.append(sum(fuel))
    return min(fuels)

def main():
    with open('/Users/claudia/Desktop/aoc/input7.txt','r') as file:
        r = file.read()
        raw = list(map(int,r.split(',')))
    
    print('a', a(raw))
    print('b', b(raw))

if  __name__ == '__main__':
  main()