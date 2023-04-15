# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
sum = 0
if number < 100 or number > 999:
    print('Введено не трехзначное число')
else:
    while number > 0:
        sum = sum + number%10
        number = number // 10
    print(sum) 