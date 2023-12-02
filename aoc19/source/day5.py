def readData():
    filename = 'source/../input/day5.txt'
    with open(filename) as file_object:
        rawData = file_object.readline()
        data = rawData.split(",")
        data = [int(i) for i in data]
        return data

def main(data, instrIndex):
    index_inc = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4}
    instrPointerModified = False
    instr = data[instrIndex]

    if instr == 3:
        userInput = 5
        index = data[instrIndex+1]
        data[index] = userInput
    elif instr == 4:
        val1 = data[instrIndex+1]
        print(data[val1])
    elif instr == 99:
        return

    opCode = instr % 10
    fstParam = (instr // 100) % 10
    sndParam = (instr // 1000) % 10
    trdParam = (instr // 10000) % 10
    modeList = [fstParam, sndParam, trdParam]
    paramList = []

    for i in range(1, index_inc[opCode]):
        if modeList[i-1] == 0:
            paramList.append(data[data[instrIndex+i]])
        else:
            paramList.append(data[instrIndex+i])
    
    if opCode == 1:
        summ = paramList[0] + paramList[1]
        data[data[instrIndex+3]] = summ

    elif opCode == 2:
        fac = paramList[0] * paramList[1]
        data[data[instrIndex+3]] = fac

    elif opCode == 5:
        if paramList[0] != 0:
            instr = paramList[1]
            instrPointerModified = True
    elif opCode == 6:
        if paramList[0] == 0:
            instr = paramList[1]
            instrPointerModified = True
    elif opCode == 7:
        if paramList[0] < paramList[1]:
            data[data[instrIndex+3]] = 1
        else:
            data[data[instrIndex+3]] = 0
    elif opCode == 8:
        if paramList[0] == paramList[1]:
            data[data[instrIndex+3]] = 1
        else:
            data[data[instrIndex+3]] = 0
    
    if not instrPointerModified:
        instrIndex += index_inc[opCode]
        main(data, instrIndex)
    else:
        main(data, instr)    

data = readData()
main(data, 0)
