__author__ = 'ipostolaki'


days_forms = ['день', 'дня', 'дней']
hours_forms = ['час', 'часа', 'часов']

def plur(digits, plurals):

    sd = str(digits)

    if sd.endswith('1') and sd[-2:] != '11':
        return sd + ' ' + plurals[0]
    elif sd[-1:] in '234' and sd[-2:] not in ['12','13','14']:
        return sd + ' ' + plurals[1]
    else:
        return sd + ' ' + plurals[2]

# 1 день 21 день
# 2 дня 3 4 22 23 24 дня
# 5 дней 6 7 8 9 10 11 12 13 14 1 15 16 17 18 19 20 25 дней


dates = range(1,300)

for i in dates:
    r = plur(i,hours_forms)
    if r:
        pass
        print(r)


