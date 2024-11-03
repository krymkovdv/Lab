# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, a = ','):
    first_group = set(first_group.split(a))
    second_group = set(second_group.split(a))
    solution = list(first_group.intersection(second_group))
    solution.sort()
    return solution

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print('Общие участники',find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
