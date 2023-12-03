f = open("./input.txt", "r")

sum = 0


def create_num(s):
  n = 0
  m = 0
  for c in s:
    if c.isnumeric():
      n = int(c)
      break

  for c in reversed(s):
    if c.isnumeric():
      m = int(c)
      break

  return n * 10 + m

for line in f:
  sum += create_num(line)

print(sum)