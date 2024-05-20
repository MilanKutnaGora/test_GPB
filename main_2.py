m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

total_numbers = sum(len(x) for x in m)
print(f"Общее количество чисел: {total_numbers}")

total_sum = sum(sum(x) for x in m)
print(f"Общая сумма чисел: {total_sum}")

average = total_sum / total_numbers
print(f"Среднее значение: {average}")

all_sets = tuple(frozenset(x) for x in m)
print(f"Все множества в один кортеж: {all_sets}")