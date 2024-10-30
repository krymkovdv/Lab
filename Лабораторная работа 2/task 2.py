salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
sum_spend = 0
total_salary = 0
for i in range(months):
    sum_spend += spend
    spend = spend * (1+increase)
    total_salary = (i+1)*salary
    money_capital = sum_spend - total_salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
