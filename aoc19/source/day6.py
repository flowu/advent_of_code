from collections import defaultdict

def readData():
    filename = 'source/../input/day6.txt'
    dic = defaultdict(list)
    with open(filename) as file_object:
        lines = file_object.readlines()
    for line in lines:
        spl = line.rstrip().split(")")
        # ABC)DEF: DEF:'ABC' - DEF orbits around ABC
        dic[spl[1]].append(spl[0])
    return dic

def solve(dic):
    result = 0
    for key, value in dic.items():
        result = getOrbits(key, value, dic, result)
    return result

def getOrbits(key, value, dic, result):
    #Direct orbit
    result += 1
    #Indirect orbits
    while (value[0] != "COM"):
        for k, v in dic.items():
            if value[0] == k:
                key = k
                value = v
                result += 1
    return result

def solvePart2(dic):
    key = None
    value = None
    # Find YOU with its value
    for k, v in dic.items():
        if k == 'YOU':
            key = k
            value = v
    steps = searchParent(dic, key, value, 0)
    return steps

# Find parent to a given key-value pair
def searchParent(dic, key, value, steps):
    sndLastKey = None
    sndLastValue = None
    for k, v in dic.items():
        if value[0] == k:
            sndLastKey = key
            sndLastValue = value
            key = k
            value = v
            steps += 1
            # Find keys children except sndLastKey (child we found its parent (this node))
            children = searchSubTree(sndLastKey, sndLastValue, dic)
        
    if value[0] != "COM":
        searchParent(dic, key, value, steps)
    return steps

def searchSubTree(sndLastKey, sndLastValue, dic):
    children = {}
    for k, v in dic.items():
        if v[0] == sndLastValue[0] and not k == sndLastKey:
            #searchSubTree()
            print(k)
            print(v[0])
            
dic = readData()
res = solve(dic)
shortestPath = solvePart2(dic)
print("Part 1: " + str(res))
print("Part 2: " + str(shortestPath))
