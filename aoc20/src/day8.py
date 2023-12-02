def main():
  with open("/Users/macbook/Desktop/AoC/input/day8.txt","r") as file:
    input = [(pair.split()[0],int(pair.split()[1])) for pair in file.read().split('\n')]
  print(input)

  acc, index, mem = solve(input) #task1
  print(acc)

  for idx in mem:  #task2
    tmp = input
    operation = tmp[idx][0]
    if operation == 'nop':
      tmp[idx] = ('jmp',tmp[idx][1])
      acc, index, mem = solve(tmp)
      if index == len(tmp) - 1:
        print('task2: ', acc)
        break
    elif operation == 'jmp':
      tmp[idx] = ('nop',tmp[idx][1])
      acc, index, mem = solve(tmp)
      if index == len(tmp) - 1:
        print('task2: ', acc)
        break
    else:
      continue
    tmp[idx] = (operation,tmp[idx][1]) #change back operation when failing
    
def solve(input):
  index = 0
  acc = 0
  mem = []
  while index not in mem:
    mem.append(index)
    pair = input[index]
    operation = pair[0]
    value = pair[1]
    if operation == 'nop':
      index += 1
    elif operation == 'acc':
      acc += value
      index += 1
    else:
      index += value
    if index == len(input) - 1: #for task 2: return if we are at last element
      return acc, index, mem
  return acc, index, mem

if __name__ == '__main__':
  main()