def main():
  with open("/Users/macbook/Desktop/AoC/day2.txt","r") as file:
    lines = [line for line in file] #read file
  
  nCorrectPasswords = 0
  nCorrestPosition = 0
  for line in lines: #parse input
    li = line.split()
    lowerBound = int(li[0][:li[0].index('-')])
    upperBound = int(li[0][li[0].index('-')+1:])
    char = li[1][0]
    string = li[2]
    countChars = len([line for line in string if char == line]) #count given char in string
    if countChars >= lowerBound and countChars <= upperBound: #how many validated pw, task 1
      nCorrectPasswords += 1
    if (string[lowerBound-1] == char) ^ (string[upperBound-1] == char): #task 2, XOR
      nCorrestPosition += 1
  
  return ("Task 1: " + str(nCorrectPasswords), "Task 2: " + str(nCorrestPosition))

if  __name__ == '__main__':
  print(main())