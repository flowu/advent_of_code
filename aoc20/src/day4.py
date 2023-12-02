import re

def main():
  with open("/Users/macbook/Desktop/AoC/input/day4.txt","r") as file:
    input = file.read().replace(' ', '\n').split('\n\n')
  passports = [elem.split() for elem in input]

  out = 0
  for passport in passports:
    cid = False
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    nFields = len(passport)
    for field in passport:
      b = field.split(':') #b: list of [key,value]
      if b[0] == 'cid': #find cid in password
        cid = True
      if b[0] == 'byr' and int(b[1]) >= 1920 and int(b[1]) <= 2002:
        byr = True
      if b[0] == 'iyr' and int(b[1]) >= 2010 and int(b[1]) <= 2020:
        iyr = True
      if b[0] == 'eyr' and int(b[1]) >= 2020 and int(b[1]) <= 2030:
        eyr = True
      if b[0] == 'hgt':
        st = re.split('(\d+)', b[1])
        if len(st[-1]) == 2 and st[-1] == 'cm' and int(st[1]) >= 150 and int(st[1]) <= 193:
          hgt = True
        elif len(st[-1]) == 2 and st[-1] == 'in' and int(st[1]) >= 59 and int(st[1]) <= 76:
          hgt = True
      if b[0] == 'hcl' and b[1][0] == '#' and len(b[1]) == 7 and all([True for x in b[1] if x in ['0-9,a-z']]):
        hcl = True
      if b[0] == 'ecl' and b[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        ecl = True
      if b[0] == 'pid' and len(b[1]) == 9 and all([True for x in b[1] if x.isdigit()]):
        pid = True
    if nFields - cid == 7 and byr and iyr and eyr and hgt and hcl and ecl and pid:
      out += 1
  return out

if __name__ == '__main__':
  print(main())