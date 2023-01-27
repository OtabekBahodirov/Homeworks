# def find_distance(v1, v2, t):
#     return (v1 + v2) * t
# print(find_distance(100, 70, 2))
# print(find_distance(200, 80, 1))
# print(find_distance(70, 80, 5))

# def degre_num(n1, n2):
#     return n1 ** n2
# print(degre_num(2, 3))
# print(degre_num(3, 10))
# print(degre_num(5, 5))
# print(degre_num(10, 4))


# def acc(n1, n2):
#     return n1 + n2
# print(acc(10, 20))
# print(acc(20, 20))



# def calc(n1, n2, n3):
#     return (n1 + n2) - n3
# print(calc(10, 20, 30))
# print(calc(120, 20, 30))
# print(calc(12, 70, 30))


def multi_list(num, start, stop):
    for i in range(start, stop +1):
        expression = f'{num}  x  {i} = {num * i}'
        print(expression)


# 

# multi_list(num, start, stop)
multi_list(5, 2, 10)