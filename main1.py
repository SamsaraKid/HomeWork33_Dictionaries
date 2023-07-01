import random

# klass = int(input('Выберите класс персонажа:\n1 - Воин\n2 - Лучник\n3 - Маг\n'))
# race = int(input('Выберите расу персонажа:\n1 - Эльф\n2 - Орк\n3 - Человек\n'))
# name = input('Дайте персонажу имя:\n')
#

klass = 3
name = ''
hero = {'klass': '', 'race': '', 'name': name,
        'stats': {'strength': 0, 'stamina': 0, 'agility': 0, 'charisma': 0, 'intelligence': 0, 'luck': 0}}
#
#
#
# match race:
#     case 1: hero['race'] = 'эльф'
#     case 2: hero['race'] = 'орк'
#     case 3: hero['race'] = 'человек'



stats = []
sum = 30
for i in range(6):
    stats.append(round(random.gauss(5, 5/3)))


print(stats)
print(sorted(stats))

stats = sorted(stats)
res = 0
for i in stats:
    res += i

while res < sum:
    stats[4] += 1
    res += 1
    stats = sorted(stats)

while res > sum:
    stats[3] -= 1
    res -= 1
    stats = sorted(stats)

if stats[3] == stats[4]:
    stats[3] -= 1
    stats[4] += 1



print(stats, res)

stats_low = stats[:4]
stats_high = stats[4:]
random.shuffle(stats_low)
random.shuffle(stats_high)



print(stats, res)
match klass:
    case 1:
        hero['klass'] = 'воин'
        stats = stats_high + stats_low
    case 2:
        hero['klass'] = 'лучник'
        stats = stats_low[:2] + stats_high + stats_low[2:]
    case 3:
        hero['klass'] = 'маг'
        stats = stats_low + stats_high

i = 0
for st in hero['stats']:
    hero['stats'][st] = stats[i]
    i += 1
    print(st.ljust(15), hero['stats'][st])