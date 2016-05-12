import os
Files = []
numbers_of_files = 10
f1 = open('SyntaxErrors.txt', 'w')
for i in range(numbers_of_files):
    Files.append(str(i) + ".rb")
print(Files)
for i in range(numbers_of_files):
      os.system("ruby " + str(i) + ".rb 2>> Errors.txt")
      os.system("ruby " + str(i) + ".rb >> Success.txt")
f = open('Errors.txt', 'r')
for line in f:
    if "syntax" in line:
        f1.write(line[0] + '\n')


