# names =  ['Said', "Dildora", 'Dilnavoz']
# names_lenght_list = [len(name) for name in names]
# new_names = [i for i in zip(names,names_lenght_list)]
# print(new_names
# )

countries = [
    {
        'Country' : 'Uzbekistan',
        'code' : '+998'
    },
    {
        'Country' : 'Kazakhstan',
        'code' : '+7'
    }
    {
        'Country' : 'United States',
        'code' : '+1'
    },
]

c = {country['Country']: countries['code'] for country in countries}