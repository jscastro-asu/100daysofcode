with open("file1.txt", encoding = 'utf-8') as f:
  a = f.readlines()

with open("file2.txt", encoding = 'utf-8') as f2:
  b = f2.readlines()

result = [int(num) for num in b if num in a]
print(result)