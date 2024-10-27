salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
sum_spend = 0
for i in range(months):
    sum_spend += spend
    spend = spend * (1+increase)
money_capital = sum_spend - salary * months
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
