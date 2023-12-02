def main():
  with open("/Users/macbook/Desktop/AoC/input/day7.txt","r") as file:
    input = file.read().split('\n')
  dic = {}
  for line in input:
    indices = [idx for idx,bokst in enumerate(line.split()) if bokst.isdigit()]
    dic[' '.join(line.split()[:2])] = [(line.split()[item],' '.join(line.split()[item+1:item+3])) for item in indices]
  
  #Task 1
  keys = set()
  for key, value in dic.items():
    for pair in value:
      if 'shiny gold' in pair[1]:
        keys.add(key)

  snd = -1
  lst = 0
  while lst != snd:
    keys2 = set()
    for key, value in dic.items():
      for pair in value:
        if pair[1] in keys:
          keys2.add(key)
    snd = len(keys)
    keys = keys2.union(keys)
    lst = len(keys)
    print(lst)

  #Task 2: bfs
  task2 = 0
  queue = []
  for key, value in dic.items(): #find children to shiny gold bag to initialize queue
    if 'shiny gold' == key:
      queue.append(value)
  while len(queue) > 0:
    items = queue.pop(0)
    for item in items: #iterate over each bag type of parent
      nr = int(item[0]) #number of bags of given type
      task2 += nr
      kind = item[1]
      while nr > 0: #find and place all (nr) bag's children in queue
        for key, value in dic.items():
          if kind == key:
            queue.append(value)
            break
        nr -= 1
  print(task2)

if __name__ == '__main__':
  main()