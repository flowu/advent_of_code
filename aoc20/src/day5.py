def main():
  with open("/Users/macbook/Desktop/AoC/input/day5.txt","r") as file:
    input = [line.strip() for line in file]
  
  #task 1
  seatsTaken = []
  for seat in input:
    rowSeq = seat[:-3]
    colSeq = seat[-3:]
    row = seqToNum(rowSeq)
    col = seqToNum(colSeq)
    seatsTaken.append(row * 8 + col)
  print('Highest seat number: ' + str(max(seatsTaken)))
  
  #task 2
  sort = sorted(seatsTaken)
  mySeat = [seat+1 for idx,seat in enumerate(sort[:-1]) if sort[idx+1] - seat != 1]
  print('My seat number: ' + str(mySeat[0]))

def seqToNum(st):
  lower = 0
  upper = int(2**len(st))-1
  for x in st:
    if x == 'F' or x == 'L':
      res = upper // 2
      upper = upper - (upper-lower) // 2 - 1
    elif x == 'B' or x == 'R':
      res = upper
      lower = upper - (upper-lower) // 2
  return lower if st[-1] == ('F' or 'L') else upper

if __name__ == '__main__':
  main()