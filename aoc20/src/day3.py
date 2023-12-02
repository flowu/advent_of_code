from functools import reduce

def main(right, flag): #right: skip elements every row, flag: skip every other row
  with open("/Users/macbook/Desktop/AoC/day3.txt","r") as file:
    lines = [line.strip() for line in file] #read input from file

  res = 0
  elem = 0
  for row in range(len(lines)): #iterate over row number
    if flag and row % 2 == 1: #skip rows 1,3,5,...
      continue
    if lines[row][elem] == '#': #check if character is a tree
      res += 1
    elem = (elem+right)%len(lines[row]) #turn around when row end reached
    
  return res

if  __name__ == '__main__':
  lst = [main(x, False) for x in range(1,8,2)]
  lst.append(main(1, True))
  print(reduce(lambda x,y: x*y, lst)) #multiply items within list