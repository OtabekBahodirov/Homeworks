# # students = [
# #     'Said', 'Dilnavoz', 'Dildora'
# # ]
# # print(len(students))
# # students.append('Dilmurod')
# # students.pop()

# # print(students)

# class Stack:
#     def __init__(self, data):
#         self.stack = data
#         self.lenght = len(data)

#     def add(self, value):
#         self.stack.append(value)
#         self.lenght += 1

#     def remove(self):
#         self.stack.pop()
#         self.lenght -= 1

#     def __str__(self):
#         return str(self.stack)

# students_stack = Stack(['Said', 'Dilnavoz', 'Dildora'])

# students_stack.add('Dilmurod')
# students_stack.remove()
# students_stack.remove()
# print(students_stack)
# print(students_stack.lenght)



# class Queue:
#     def __init__(self, data):
#         self.stack = data
#         self.lenght = len(data)

#     def add(self, value):
#         self.stack.append(value)
#         self.lenght += 1

#     def remove(self):
#         self.stack.pop(0 )
#         self.lenght -= 1

#     def __str__(self):
#         return str(self.stack)


# from collections import deque


class Vehicle:
    color = 'white'
    engine = 1.6
    model = 'Spark'


    def __init__(self, wheels = 4):
        self.wheels_num = wheels

    def change_color(self, value):
        self.color = value

    def change_model(self, model):
        self.model = model

        if model == 'Malibu':
            self.engine = 2.5

chevrolet = Vehicle()
print(Vehicle().wheels_num)
print(chevrolet.color)
chevrolet.change_color('black')
print(chevrolet.color)
chevrolet.change_model('Malibu')
print(chevrolet.model)
print(chevrolet.engine)