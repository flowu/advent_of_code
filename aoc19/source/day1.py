result = 0
filename = 'source/../input/day1.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    module = int(line)
    while module / 3 - 2 >= 0:
        fuelReq =  module / 3 - 2
        result = result + fuelReq
        module = fuelReq
print (result)