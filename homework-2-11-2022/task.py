# key = '273'
# text = 'Assalomu aleykum'
# words = text.split(' ')
# key_list = list(key)
# phrase = ''.join(text.split(' '))
# key_list = list(map(lambda key: int(key), list(key)))

# for i, key in enumerate(key_list):
#     key_list.pop(i)
#     key_list.insert(i, int(key))
# phrase_cipher = ''
# for index, letter in enumerate(phrase):
#     key_index = index % len(key_list)
#     phrase_cipher += chr(ord(letter) + key_list[key_index])

# print(key_list)
# ciphered_phrase = f'{phrase_cipher[:8]} {phrase_cipher[8:]}'

# ciphered_text_list = []
# for word in words:
#     word_cipher = ''
#     for index, letter in enumerate(word):
#         key_index = index % len(key_list)
#         print(ord(letter), key_list[key_index])
#         word_cipher += chr(ord(letter) + key_list[key_index])
#     ciphered_text_list.append(word_cipher)
# # Czvcsro| dnl|m|p
# # ciphered_phrase = ''.join(ciphered_phrase.split(' '))
# # deciphered_phrase = ''
# # for index, letter in enumerate(ciphered_phrase):
# #     key_index = index % len(key_list)
# #     deciphered_phrase += chr(ord(letter) - key_list[key_index])

# print(' '.join(ciphered_text_list))
# # deciphered_phrase = f'{deciphered_phrase[:8]} {deciphered_phrase[8:]}'

# # print(deciphered_phrase) 
