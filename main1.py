import random

print('----------------------------------------Задание №2. Создание героя-----------------------------------------')

stats_sum = 30

klass = int(input('Выберите класс персонажа:\n1 - Воин\n2 - Лучник\n3 - Маг\n'))
race = int(input('Выберите расу персонажа:\n1 - Эльф\n2 - Орк\n3 - Человек\n'))
name = input('Дайте персонажу имя:\n')
stats_type = int(input('Выберите тип распределения характеристик:\n'
                       '1 - Случайное (больше шанса, что будут выражены основные характеристики класса в ущерб другим)\n'
                       '2 - Нормальное распределение (больше шанса на более равномерное распределение)\n'))

hero = {'klass': '', 'race': '', 'name': name,
        'stats': {'сила': 0, 'выносливость': 0, 'ловкость': 0, 'харизма': 0, 'интеллект': 0, 'удача': 0}}

match race:
    case 1: hero['race'] = 'Эльф'
    case 2: hero['race'] = 'Орк'
    case 3: hero['race'] = 'Человек'
    case _: hero['race'] = 'Нежить'


# Создаём массив со значениями статов
# Заполняем его случайными значениями,
# либо рандом от 1 до 9
# либо нормально распределёнными с матожиданием 5 и среднеквадратичным отклонением 5/3
stats = []
for i in range(6):
    if stats_type == 1:
        stats.append(random.randint(1, 10))
    else:
        stats.append(abs(round(random.gauss(5, 5/3))))

# сортируем получившийся массив, чтобы максимальные значения оказались в конце (элементы [4] и [5])
stats = sorted(stats)

# считаем сумму статов в массиве
stats_cur_sum = 0
for i in stats:
    stats_cur_sum += i

# если сумма меньше заданной (30),
# то прибавляем 1 к предпоследнему максимальному значению,
# увеличиваем сумму и снова сортируем
# пока сумма не станет 30
while stats_cur_sum < stats_sum:
    stats[4] += 1
    stats_cur_sum += 1
    stats = sorted(stats)

# если сумма больше заданной (30),
# то вычитаем 1 из пред-предпоследнего максимального,
# уменьшаем сумму и снова сортируем
# пока сумма не станет 30
while stats_cur_sum > stats_sum:
    stats[3] -= 1
    stats_cur_sum -= 1
    stats = sorted(stats)

# если пред-предпоследнее и предпоследнее максимальные равны
# меняем между ними единицу, чтобы было отличие между двумя максимальными и четырьмя минимальными
# сортируем и проверяем заново
while stats[3] == stats[4]:
    stats[3] -= 1
    stats[4] += 1
    stats = sorted(stats)

# вычленяем 4 минимальных и 2 максимальных значений массива статов
# перемешиваем два получившихся массива
stats_low = stats[:4]
stats_high = stats[4:]
random.shuffle(stats_low)
random.shuffle(stats_high)

# в зависимости от класса вписываем название в характеристики героя
# и переформируем массив статов в нужном порядке
match klass:
    case 1:
        hero['klass'] = 'Воин'
        stats = stats_high + stats_low
    case 2:
        hero['klass'] = 'Лучник'
        stats = stats_low[:2] + stats_high + stats_low[2:]
    case 3:
        hero['klass'] = 'Маг'
        stats = stats_low + stats_high
    case _:
        hero['klass'] = 'Уникальный'
        random.shuffle(stats)

# выводим информацию о персонаже
print('Ваш персонаж:', hero['name'], hero['klass'], hero['race'])

# вписываем статы из массива в словарь характеристик героя и выводим характеристики
i = 0
for st in hero['stats']:
    hero['stats'][st] = stats[i]
    i += 1
    print(st.ljust(15), hero['stats'][st])

