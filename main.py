import random

print('----------------------------------------Задание №1. Расписание уроков-----------------------------------------')

subjects = {'young': ['чтение', 'пение', 'рисование', 'математика'],
            'middle': ['математика', 'физика', 'литература', 'русский язык', 'история', 'биология', 'география', 'иностранный язык'],
            'senior': ['математика', 'физика', 'литература', 'русский язык', 'история', 'биология', 'география', 'иностранный язык', 'химия', 'астрономия', 'обществознание', 'информатика']}

num_subj_per_day = {'young': 3, 'middle': 4, 'senior': 5}

week = {'Понедельник': [], 'Вторник': [], 'Среда': [], 'Четверг': [], 'Пятница': []}

schedule = {'young': week.copy(), 'middle': week.copy(), 'senior': week.copy()}


for cls in schedule:  # проходим по всем классам: младший, средний, старший
    for day in schedule[cls]:  # проходим по дням недели в словаре нужного класса
        subj = subjects[cls].copy()  # копируем список предметов нужного класса
        random.shuffle(subj)  # перемешиваем предметы в копии списка предметов
        subj = subj[:num_subj_per_day[cls]]  # выбираем из перемешанного списка столько предметов, сколько уроков у класса в день
        schedule[cls][day] = subj  # получившийся массив вписываем в расписание

# функция вывода расписания для одного класса
def print_schedule(name):
    print(''.ljust(15), end='')
    for day in week:
        print(day.ljust(20), sep='', end='')
    print()
    for i in range(num_subj_per_day[name]):
        print(i + 1, '-й урок'.ljust(14), sep='', end='')
        for day in week:
            print(schedule[name][day][i].ljust(20), end='')
        print()

print('************************************************Младшие классы************************************************')
print_schedule('young')
print('************************************************Средние классы************************************************')
print_schedule('middle')
print('************************************************Старшие классы************************************************')
print_schedule('senior')


