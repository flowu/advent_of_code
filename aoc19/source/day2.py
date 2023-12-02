def readData():
    filename = 'source/../input/day2.txt'
    with open(filename) as file_object:
        rawData = file_object.readline()
        data = rawData.split(",")
        data[1] = '12'
        data[2] = '2'
        data = [int(i) for i in data]
        return data

def main(data, currInstr, valone, valtwo):
    instr = data[currInstr]
    if instr == 1:
        val1 = data[currInstr+1]
        val2 = data[currInstr+2]
        summ = data[val1] + data[val2]
        placeToStore = data[currInstr+3]
        data[placeToStore] = summ
        main(data, currInstr + 4, valone, valtwo)
    elif instr == 2:
        val1 = data[currInstr+1]
        val2 = data[currInstr+2]
        fac = data[val1] * data[val2]
        placeToStore = data[currInstr+3]
        data[placeToStore] = fac
        main(data, currInstr + 4, valone, valtwo)
    elif instr == 99:
        result = data[0]
        if data[0] == 19690720:
            print(valone)
            print(valtwo)
        return result
    else:
        print("instruction not valid")

def manData(data):
    for i in range(0, 60):
        for j in range(0, i+1):
            data[1] = i
            data[2] = j
            result = main(data, 0, i, j)
            # reset input
            data = readData()

data = readData()
manData(data)
