user_input = int(input("Enter numbers: "))

number1 = user_input // 10000 % 10
number2 = user_input // 1000 % 10
number3 = user_input // 100 % 10
number4 = user_input // 10 % 10
number5 = user_input // 1 % 10
print(number1," ",number2," ",number3," ",number4," ",number5," " )