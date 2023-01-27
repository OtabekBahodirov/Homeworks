# with open('./data.txt', mode='r', encoding='utf8') as rf:
#     for line in rf.readlines():
#             data = line.strip().split(';')
#             print(f'{data[0]} was born in {data[-1]}/ {data[-2]}/ {data[-3]}')

with open('./data.txt', mode='r', encoding='utf8') as rf:
    line = []
    for char in rf.read():
        line.append(char)

lines = ''.join(line).split('\n')

for line in lines:
    data = line.strip().split(';')
    print(f'{data[0])  was born in {data[-1]}/ {data[-2]}/ {data[-3]}')