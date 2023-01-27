txt = open('notes.txt', 'r', encoding='utf-8')
# print(txt.read().upper)

# txt.seek(17)

# for i, line in  enumerate(txt, 1):
#     print(f'{i}. {line.strip()}')


for i, line in  enumerate(txt, 1):
    data =line.strip().split(' ')
    # print(f'{i}.  Name: {data[0]}, age: {data[1]}')
    print(f'{i}. Reverse Name: {data[0] [::-1].lower().title()}, Reverse age: {str(data[1]) [::-1]}')
