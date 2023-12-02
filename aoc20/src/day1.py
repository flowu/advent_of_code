def main():
  with open("/Users/macbook/Desktop/AoC/day1.txt","r") as file:
    lines = [int(line) for line in file] #read file
    
  for idx,x in enumerate(lines): #exhaustive search: find 3 elements x,y,z
    for idy,y in enumerate(lines[idx+1:]):
      for z in lines[idx+idy+1:]:
        if x + y + z == 2020:
          return x * y * z

if  __name__ == '__main__':
  print(main())