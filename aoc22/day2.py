def fun(rows, mapping):
    return sum([mapping[row] for row in rows])

def main():
    txt_file = open('C:/Users/joelpo/Desktop/aoc/day2.txt','r')
    txt = txt_file.read()
    rows = txt.split("\n")
    
    mapping_a = {'A Y':8, 'A X':4, 'A Z':3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
    mapping_b = {'A X':3, 'A Y':4, 'A Z':8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
    
    print('a', fun(rows, mapping_a))
    print('b', fun(rows, mapping_b))

if  __name__ == '__main__':
  main()

#OPPONENT
#A 1 ROCK
#B 2 PAPER
#C 3 SCISSOR

#ME
#X 1 ROCK
#Y 2 PAPER
#Z 3 SCISSOR

#OUTCOME
#X LOSE
#Y DRAW
#Z WIN
