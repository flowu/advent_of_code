def main():
  with open("/Users/macbook/Desktop/AoC/input/day9.txt","r") as file:
    input = [int(line) for line in file.readlines()]
  print(input)

  #task 1
  preample = 25
  invalidNr = 0
  breakFlag = False
  for idx,line in enumerate(input[preample:]):
    flag = False
    for idy,x in enumerate(input[idx:preample+idx]):
      for y in input[idx+idy+1:preample+idx]:
        if (line == x + y):
          flag = True
    if not flag:
      print(line)
      breakFlag = True
      invalidNr = line
    if breakFlag:
      break
  
  #task 2
  for lineIndex in range(len(input)):
    test = [input[lineIndex]]
    tmpIndex = lineIndex + 1
    while sum(test) <= invalidNr:
      test.append(input[tmpIndex])
      if sum(test) == invalidNr:
        print(min(test) + max(test))
        break
      tmpIndex += 1
    else:
      continue
    break

if __name__ == '__main__':
  main()