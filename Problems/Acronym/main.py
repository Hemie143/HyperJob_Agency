# read test.txt
with open('test.txt', 'r') as f:
    for line in f.readlines():
        print(line[0])
