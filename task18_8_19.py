number_tickets = int(input('Введите количество приобретаемых билетов: '))
sum = 0
for i in range(1, number_tickets + 1):
    age = int(input(f'Билет № {i}, введите возраст посетителя: '))
    if 18 <= age < 25:
        sum += 990
    elif age >= 25:
        sum += 1390
if number_tickets <= 3 or sum == 0:
    print('Сумма к оплате -', sum, 'руб.') # если билетов меньше трех или все билеты бесплатные
else:
    print('Сумма к оплате, со скидкой 10% -', int(sum/10*9), 'руб.') # если билетов больше трех и сумма не ноль