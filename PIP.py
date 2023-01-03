import re
n =input("num\n")
numbers = re.findall('\d', n)
print(sum(map(int,numbers)))