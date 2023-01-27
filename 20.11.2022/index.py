# with open('./text.txt', 'a', encoding='utf8') as file:
#     for i in range(10):
#         file.write(f'{i}zzz ')

# with open('./text.txt', 'r+', encoding='utf8') as file:
#     data = file.readline().split(';')
#     ints = [int(x) for x in data]
#     ints = sorted(ints)
#     file.seek(0)
#     for num in ints:
#         file.write(f'{num};')

# num = int(input("Son kiriting: "))
# with open('mult.txt', 'w', encoding='utf8') as f:
#     for i in range(1, 11):
#         f.write(f'{i}. {num} x {i} = {num * i}\n' )

#  with open('data_new.txt', 'w', encoding='utf8') as wf:
#       f.write(" {fname} is, {age} years old".format(fname = "Elbek", age = 26))
# from datetime import datetime
# with open('./data.txt', 'r', encoding='utf8') as rf:
#     with open('./data_new.txt', 'w', encoding='utf8') as wf:
#         for line in rf:
#             data = line.strip().split('-')
#             wf.write(
#                 f'{data[0]} is {datetime.now().year - int(data[1])} years old\n')

# import calendar

# calendar.prcal(2022)

from datetime import date

def get_difference(date1, date2):
    delta = date2 - date1
    return delta.days

d1 = date(2022,10,20)
d2 = date(2023, 7, 12 
)
days = get_difference(d1, d2)
print(f'Difference is {days} days')