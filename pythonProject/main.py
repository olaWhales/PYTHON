#number = list(range(1, 10))
#print(number)

#result = [num for num in number if num % 5 == 0]
#print(result)

#number = [[0 for _ in range(4)] for _ in range (5)]
#print(number)
#
# number = [0] * 4
# numbers = [number] * 5
# #result = [number for _ in range (5)]
# print(numbers)
#
#
# # total_number = [0]
# # for number in range(5):
# #     for number2 in range(4):
# #         # total_number[number][numbers] = 2
# # print(total_number)
#
# # x = [4]
# # n = [] * 4
# # for _ in range(5):
# #     n.append(x)
# # print(x)
#
# #we can change list to turple and turple to list by conversion or cast e.g
#
# # this is list example
# # semicolon = [1,2,3,5,"school"]
# # print(semicolon)
# # semicolon[3] = "semicolon"
# # print(semicolon)
# # print(len(semicolon))
# #
# # # this is turple example
# # semi = (1,2,3,"semicolon")
# # print(semi)
# # semi = list(semi)
# # semi[2] = 100
# # print(semi)
# # print(len(semi))
#
#
# # turple2 = ("Orange", [10,20,30],(5,15,25))
# # print(turple2)
# # turple_result = turple2[1][1]
# # turple_result2 = turple2[2][2]
# # print(((turple_result),(turple_result2)))
#
# # in function
# # turple2 = ("Orange", [10,20,30],(5,15,25))
# # def turple_variable(tuple):
# #     turple_result = turple2[1][1]
# #     turple_result2 = turple2[2][2]
# #     return (((turple_result),(turple_result2)))
# # print(turple_variable(tuple))
#
from decimal import Decimal

class Akant:
    #this is instance variable in java code
    def __init__(self, name: str, pin: str, balance: float =0.00): # i put a datatype here
        #this is like access modifier in java code
        self.name = name
        self.pin = pin
        self.balance = balance
     #we have a method called depositl
    def deposit(self, amount):
        if amount > Decimal(0.00):
            raise ValueError(f" is an Invalid amount")
        self.balance += amount
#this is a contructor we declare it a  class name
#this is like in

