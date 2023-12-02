def main():
  with open("/Users/macbook/Desktop/AoC/input/day6.txt","r") as file:
    input = [[set(x) for x in group.split()] for group in file.read().split('\n\n')]
  
  print(input)

  print(sum(len(set.union(*xs)) for xs in input))

  #task 1
  res = 0
  for group in input:
    answers = []
    persons = group.split()
    for person in persons:
      for answer in person:
        if answer not in answers:
          answers.append(answer)
    res += len(answers)
  print(res)

  #task 2
  res2 = 0
  for group in input:
    sameAnswers = []
    persons = group.split('\n')
    shortest = min(persons, key=len)
    for answer in shortest:       #l
      exists = []
      for person in persons:      #cedziyl
        if answer in person:  #
          exists.append(True)
        else:
          exists.append(False)
      if all(exists):
        sameAnswers.append(answer)
      #if all([True for person in persons if answer in person]):
      #  sameAnswers.append(answer)
    res2 += len(sameAnswers)
  print(res2)

if __name__ == '__main__':
  main()