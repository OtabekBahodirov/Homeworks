#                                                  1- Misol
# def find_season (season) :
# 	list1 = [[12 , 1 , 2], [3 , 4 , 5],
# 			[6 , 7 , 8], [9 , 10 , 11]]
# 	if season in list1[0] :
# 		print ( "WINTER" )
# 	elif season in list1[1] :
# 		print ( "SPRING" )
# 	elif season in list1[2] :
# 		print ( "SUMMER" )
# 	elif season in list1[3] :
# 		print ( "AUTUMN" )
# 	else :
# 		print ( "Invalid Month Number" )
# print(find_season(9))


#                                                   2 -  MISOL

# def calc_deposit(a, years):
#     ci = a * (pow((1 + 10 / 100), years)) 
#     return ci
# a = int(input("Kiritmoqchi bo'lgan summangiz : "))
# years = int(input("Necha yilga kiritmoqchisiz : "))
# ci = calc_deposit(a, years) 
# print(years, "Yilga Foiz oshishi: {}".format(ci),"ni tashkil etadi")


#                                                      3 - MISOL





#                                    4 - Misol
# def calc(num):
#     a = num
#     b = int(str(num)* 2)
#     c = int(str(num)* 3)
#     return a + b + c

# print(calc(2))





# param = 10
# def outer(param = 200):
#     param = 30

#     def func1():
#         nonlocal param
#         param = 4

#         def inner():
#             global param
#             param += 1
#             return param

#         param = inner()
#     func1()
    
#     return param
    
# print(outer(100 and param))