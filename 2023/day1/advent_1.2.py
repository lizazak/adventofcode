numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def get_first(line):
  earliest_string = ''
  earliest_idx = len(line)
  for num in numbers.keys():
    curr_idx = line.find(num)
    if 0 <= curr_idx < earliest_idx:
      earliest_string = num
      earliest_idx = curr_idx

  for i, c in enumerate(line):
    if i > earliest_idx:
      break
    if c.isdigit():
      return int(c)
    
  return numbers[earliest_string]

def get_last(line):
  last_string = ''
  last_idx = 0
  for num in numbers.keys():
    curr_idx = line.rfind(num)
    if curr_idx > last_idx:
      last_string = num
      last_idx = curr_idx

  idx = len(line) - 1
  for c in reversed(line):
    if idx < last_idx:
      break
    if c.isdigit():
      return int(c)
    idx -= 1
    
  return numbers[last_string]

f = open("./input.txt", "r")

sum = 0

for line in f:
  sum += get_first(line) * 10 + get_last(line)

print(sum)