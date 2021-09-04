# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

profit = float(input('Enter your profit: '))
costs = float(input('Enter your costs: '))

if profit > costs:
    print(f'Congratulations, your profit is greater than costs: {(profit - costs):0.2f}')
    employees = int(input('Enter your employees count: '))
    print(f'Profit per employee ~ {(profit / employees):0.2f}')
elif profit == costs:
    print('Profit equals costs')
else:
    print('Your costs are more than profit :(')
