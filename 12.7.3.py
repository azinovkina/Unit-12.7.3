money = int(input('Введите сумму вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('Проценты по вкладам в представленных банках', str(per_cent).strip('{}'))
tkb_deposit = int((money / 100) * 5.6)
skb_deposit = int((money / 100) * 5.9)
vtb_deposit = int((money / 100) * 4.28)
sber_deposit = int((money / 100) * 4.0)
deposit = [tkb_deposit, skb_deposit, vtb_deposit, sber_deposit]
print('Ваш годовой доход в представленных банках составят:', str(deposit).strip('[]'), 'соответственно.')
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать', deposit_max)
