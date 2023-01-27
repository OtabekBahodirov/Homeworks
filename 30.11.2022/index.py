# with open('./data.txt', 'r', encoding='utf-8') as rf:
#     data = rf.readlines()
#     users = []
#     for line in data:
#         line = line.strip().split(';')
#         if len(line) == 5:
#             name, lastname = line[0].split(' ')
#             user = {
#                 'name': name,
#                 'lastname': lastname,
#                 'login': line[1],
#                 'pass': line[2],
#                 'tel': f'+{line[3]}',
#                 'accounts': []
#             }
#             users.append(user)
#         else:
#             account = {
#                 'num': int(line[0]),
#                 'balance': int(line[1]),
#                 'currency': ''
#             }

#             if line[0].startswith('8600'):
#                 account['currency'] = 'UZS'
#             elif line[0].startswith('4560'):
#                 account['currency'] = 'USD'
#             elif line[0].startswith('1234'):
#                 account['currency'] = 'EUR'

#             users[-1]['accounts'].append(account)
#     print(users)


with open('./error-data.txt', 'r', encoding='utf-8') as rf:
    with open('./error-log.txt', 'w', encoding='utf-8') as wf:
        data = rf.readlines()
        for i, line in enumerate(data, 1):
            line = line.split(';')
            if line[0].isalpha():
                try:
                    assert line[0].split(' ') == 2
                except AssertionError:
                    wf.write(f"{i}-qatorda ism yoki familiya belgilanmagan\n")

                    #  Hisob haqidagi ma'lumot  to'liq emas
            elif line[0].isnumeric():
                try:
                      assert len(line) < 2
                except AssertionError:
                    wf.write(f"{i}-qatorda hisob haqida ma'lumot to'liq emas\n")

                #  Xato hisob raqami
            elif line[0].isnumeric():
                try:
                       assert len(line[0]) == 16
                except AssertionError:
                     wf.write(f"{i}-qatorda hisob raqami 16 ta raqamdan iborat bo'lishi kerak\n !!")

            # Hisob raqami manfiy yoxud minusda
            elif line[0].isnumeric():
                try:
                     assert float(line[1]) > 0
                except AssertionError:
                     wf.write(f"{i}-qatorda hisob raqami manfiy yoxud minusda\n")


                # Hisobda telefon raqami xato berilgan
            elif len(line) == 5:
                try:
                      assert len(line[3]) >= 12 and line[3].startswith('99888') or line[3].startswith('99899') or line[3].startswith('99895') or line[3].startswith('99894') or line[3].startswith('99893') or line[3].startswith('99891') or line[3].startswith('99890')
                except AssertionError:
                     wf.write(f"{i}-qatorda telefon raqami xato kiritilgan\n")

            #  Qatorlardagi ma'lumot to'liq eas yoki ortiqcha
            elif line[0].isalpha() or line[0].isnumeric():
                try:
                    assert len(line) == 2 or len(line) == 5
                except AssertionError:
                     wf.write(f"{i}-qatorda ma'lumot to'liq emas yoki ortiqcha\n")

            #    Parol xatoligi
            elif len(line) == 5:
                try: 
                      assert len(line[2]) > 8
                except AssertionError:
                     wf.write(f"{i}-qatorda kiritilgan paraol kamida 8 belgi yoki harfdan iborat bo'lishi kerak\n")
                #  Hisob raqam xatoligi
            elif line[0].isalnum():
                try: 
                     assert line[0].startswith('8600') or line[0].startswith('4500') or line[0].startswith('1234')
                except AssertionError:
                     wf.write(f"{i}-qatorda hisob raqami xato berilgan\n")

            
          
        # users = [b 
        #     {
        #         'name': 'Elbek',
        #         'lastname': 'Xakimbekov',
        #         'login': 'ekhakimbekov',
        #         'pass': 'password1',
        #         'tel': '+998998887766',
        #         'accounts': [
        #             {
        #                 'num': 8600789045671234,
        #                 'balance': 3120000,
        #                 'currency': 'UZS'
        #             }, {
        #                 'num': 4560334598762345,
        #                 'balance': 1000,
        #                 'currency': 'USD'
        #             }
        #         ]
        #     },
        # ]

        # print(users[0]['accounts'][0]['currency'])