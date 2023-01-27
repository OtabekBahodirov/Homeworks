PI = 3.1415
E = 2.71
SQRT_2 = 1.41
SQRT_3 = 1.71
SQRT_1_2 = 0.707

#                                 Tubson topish

# def is_prime(x: int)-> bool:
#     START  = 2
#     for i in range(START,x):
#         if not(x % i):
#             return False
#     else:
#         return True  

# #                                          Range qilish
# def generate_primes_range(start, stop):
#     prime_nums = []
#     for i in range(start, stop + 1):
#         if is_prime(i):
#             prime_nums.append(i)
#     else:
#         return prime_nums


# print(generate_primes_range(2, 100))          


#  EKUB (10, 20) = 10
# def gcd(x: int, y: int):
#     min = x if x < y else y 
#     gcd_num = 1
#     for i in range(2, min  +1):
#         if x % i == 0 and y % i == 0:
#             gcd_num = i
#     else:
#         return gcd_num
# print(gcd(40, 12))
# EKUK (6, 12) = 12
# def lct(x, y):
#     pass


# def calc_hypotenuse(a, b):
#     return (a * a + b * b) **0.5

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))


# c = calc_hypotenuse(a, b)
# print(c)


# def calc_taxi_price(km):
#     BASE = 4
#     PRICE_PER_140_M = 1.75
#     BASE_DIST_M = 140
#     return BASE + (km * 1000) * ( PRICE_PER_140_M  / BASE_DIST_M)

# print(calc_taxi_price(1.4))