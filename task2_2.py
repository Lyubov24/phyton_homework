# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('Введите первое натуральное число '))
p = int(input('Введите второе натуральное число '))
y = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
x = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
print(x, y)