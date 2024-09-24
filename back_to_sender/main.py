def logistic(rider):
    base_pay = 5000
    if 70 >= rider <= 100:
        rider * 500 + base_pay
    elif 60 >= rider < 70:
        rider * 250 + base_pay
    elif 50 >= rider < 60:
        rider * 200 + base_pay
    elif rider < 50 :
        rider * 160 + base_pay
    return rider

print(logistic(99))