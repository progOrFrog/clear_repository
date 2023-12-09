import datetime, random, math
#
#=================Приклади використання функцій закоментовані=================
#
#====================================01=======================================
def operator(str_num:str):
    '''Оператор друку, який виводить змішаний дріб, як число флоат'''
    split_str = str_num.split()
    int_part = int(split_str[0])
    float_part = float(list(split_str[1])[0]) / float(list(split_str[1])[2])
    print(int_part)
    print(float_part)
    print(int_part + float_part)

#operator('3 5/8')
#====================================02=======================================
def convert_to_fahrenheit(celsius):
    """Переводить температуру із Цельсія у Фарангейта.
    Args:
    celsius: Температура за Цельсієм.
    Returns:
    Повертає температуру за Фарангейтом."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    """Переводить температуру із Фарангейта у Цельсія.
    Args:
    fahrenheit: Температура за Фарангейтом.
    Returns:
    Температура за Цельсієм.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# print(f"{convert_to_fahrenheit(50)} °F")
# print(f"{convert_to_celsius(5)} °C")
#====================================03=======================================
def list_func(lst:list):
    """Функція виводить: \nостанній елемент списку, \nсписок у зворотньому
    порядку, \nТак, якщо 5 є в списку і Ні в інакшому випадку, \nкількість
    5 в списку, \nвідсортований список, \nкількість цілих чисел,
    менших за 5"""
    print(f'Останній елемент списку: {lst[-1]}')
    print(f'Список у зворотньому порядку: {lst[::-1]}')
    print('Так') if 5 in lst else print('Ні')
    print(f"Кількість п'ятірок у списку: {lst.count(5)}")
    lst = lst[1:-1]
    lst.sort()
    print(f'Відсортований список у зворотньому порядку: {lst}')
    print(f'Кількість цілих чисел у списку, менших за 5: '
          f'{sum(1 for num in lst if num < 5 and isinstance(num, int))}')

#list_func([1, 3, 2, 5, 1, 0.5, 9])
#====================================04=======================================
def calculate_area(radius):
    """Обчислює площу круга.
    Args:
    radius: Радіус круга.
    Returns:
    Площу круга.
    """
    pi = math.pi
    area = pi * radius * radius
    return area

def main1():
    """Запитує користувача радіус кола, а потім друкує площу кола."""
    radius = float(input("Введіть радіус круга: "))
    area = calculate_area(radius)

    print("Площа круга:", area)


# if __name__ == "__main__":
#     main1()
#====================================05=======================================
def ask_a_name():
    """ім'я і прізвище в зворотньому порядку"""
    n = input("Введіть ім'я: ")
    s = input("Введіть прізвище: ")
    print(s, n)
#ask_a_name()

#====================================06=======================================
def n(n:int):
    return n + n**2 + n**3

#print(n(2))
#====================================07=======================================
def calculate_tip(bill_amount, tip_percentage):
    """Розраховує суму чайових для заданої суми рахунку та відсотка чайових.
    Args:
    bill_amount: Загальна сума рахунку.\n
    tip_percentage: Відсоток чайових.
    Returns:
    Сума чайових.
    """

    tip_amount = bill_amount * tip_percentage
    return tip_amount

def main2():
    """Запитує в користувача ціну їжі та відсоток чайових, який він хоче
    залишити,
    а потім друкує суму чайових і загальну суму рахунку разом із чайовими."""

    bill_amount = float(input("Введіть ціну страви: "))
    tip_percentage = float(input("Введіть відсоток чайових (як десятковий дроб, наприклад, 0.2 для 20% чайових): "))

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_bill = bill_amount + tip_amount

    print("Ціна страви", bill_amount)
    print("Сума чайових становить:", tip_amount)
    print("Загальна сума рахунку з чайовими становить:", total_bill)

# if __name__ == "__main__":
#     main2()
#====================================08=======================================

def calculate_days_from_birth(day, month, year):
    """Обчислює загальну кількість днів від народження.

    Args:
    day: День народження.\n
    month: Місяць народження \
    year: Рік народження.

    Returns:
    Загальна кількість днів від народження.
    """

    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    days_from_birth = (today - birth_date).days
    return days_from_birth

def main3():
    """Запитує користувача день народження, місяць народження та рік народження, а потім друкує загальну кількість днів від народження."""
    day = int(input("Введіть день народження: "))
    month = int(input("Введіть місяць народження: "))
    year = int(input("Введіть рік народження: "))

    days_from_birth = calculate_days_from_birth(day, month, year)

    print("Загальна кількість днів від народження становить:", days_from_birth)

#if __name__ == "__main__":
#   main3()
#====================================09=======================================
def convert_angle_to_0_360(angle):
    """Перетворює кут від -180° до 180° на його еквівалент від 0° до 360°.

    Args:
    angle:  кут у градусах.

    Returns:
    Кут у градусах від 0° до 360°.
    """

    remainder = angle % 360

    if remainder < 0:
        remainder += 360

    return remainder

def main4():
    """Запитує користувача кут між -180° та 180° та друкує еквівалентний кут між 0° та 360°."""

    angle = float(input("Введіть кут між -180° і 180°: "))
    converted_angle = convert_angle_to_0_360(angle)
    print("Еквівалентний кут між 0° і 360° дорівнює:", converted_angle)

#if __name__ == "__main__":
#   main4()
#====================================10=======================================
import random

def generate_random_decimal_number():
    """Генерує випадкове десяткове число від 1 до 10 з двома десятковими знаками точності.
    Returns :
    Випадкове десяткове число від 1 до 10 із двома десятковими знаками точності.
    """

    random_number = random.randint(100, 1000)
    decimal_number = random_number / 100
    return round(decimal_number, 2)

random_decimal_number = generate_random_decimal_number()
print(f"Випадкове число: {random_decimal_number}")
#====================================11=======================================
def to_pow():
    while True:
        power = int(input("Введіть додатнє  ціле число степіня: "))
        if power >= 0:
            break
        else:
            print("Ви ввели не додатнє ціле число")

    res = str(2 ** power)
    last_two_digits = res[-2:]

    print(f"Останні дві цифри 2^{power}: {last_two_digits}")

#to_pow()
#====================================12=======================================
def you_level():
    c = int(input("Введи кількість кредитів: "))
    if c not in range(1,100):
        print('Введи правильну кількість')
        return

    if c <= 23:
        print("Ти першокурсник")
    elif 24 <= c <= 53:
        print("Ти другокурсник")
    elif 54 <= c <= 83:
        print("Молодший курс")
    else:
        print("Старший курс")

#you_level()
#====================================13=======================================
def convert_cen_to_inch():
    c = float(input("Введіть довжину в сантиметрах: "))
    if c < 0:
        print("Неправильно, довжина не повинна бути від'ємною")
    else:
        i = c / 2.54
        print(f"{c} сантиметрів дорівнюють {round(i, 2)} дюймам")

#convert_cen_to_inch()
#====================================14=======================================
def get_comp():
    c = ['камінь', 'папір', 'ножиці']
    return random.choice(c)

def get_user():
    while True:
        u_c = input('Введіть ваш вибір: камінь або ножиці або папір: ')
        if u_c in ['камінь', 'папір', 'ножиці']:
            return u_c
        else:
            print('Неправильний вибір')

def winner(user, comp):
        if user == comp:
            return 'нічия'
        elif (user == 'камінь' and comp == 'ножиці') or \
         (user == 'папір' and comp == 'камінь') or \
         (user == 'ножиці' and comp == 'папір'):
            return 'перемога'
        else:
            return 'поразка'

def game():
    '''Гра в камінь-ножиці-папір. Використовує модуль random.
    це мейн-функція, також були написані ще функції get_comp, get_user,
    winner/

    Гра відбувається до 3 спроб'''
    score = 0

    for round in range(1, 4):
        print(f'Раунд номер {round}')

        user = get_user()
        comp = get_comp()

        print(f'Ваш вибір: {user}')
        print(f"Вибір комп'ютера: {comp}")

        res = winner(user, comp)
        print(res)

        if res == 'перемога':
            score += 1

    print('гра завершена')
    if score in [2, 3]:
        print('ви виграли)')
    else:
        print('ви програли(')

# game()
#====================================15=======================================
def calculate_total_cost(i):
    if i < 10:
        total_cost = i * 12
    elif 10 <= i <= 99:
        total_cost = i * 10
    else:
        total_cost = i * 7
    return total_cost

# i = int(input('Скільки товарів ви хочете купити? '))
# print(calculate_total_cost(i))
#====================================16=======================================
def j_calc(N:int):
    s_b = 300
    m_s = 100
    a = 500

    return (s_b + N * m_s + (N // 6) * a)

#print(j_calc(6))
#====================================17=======================================
def count_business_days(s_date, e_date):
    '''Використовує модуль datetime. Функція дозволяє дізнатись кількість
    робочих днів на проміжку часу'''
    business_days = set([0, 1, 2, 3, 4])
    current_date = s_date
    business_day_count = 0

    while current_date <= e_date:
        if current_date.weekday() in business_days:
            business_day_count += 1
        current_date += datetime.timedelta(days=1)

    return business_day_count

s_date = datetime.date(2023, 1, 1)
e_date = datetime.date(2023, 1, 15)

#print(count_business_days(s_date, e_date))
#====================================18=======================================
def reverse_tuple(t:tuple):
    '''Просто перевернутий кортеж'''
    return t[::-1]

#print(reverse_tuple(('a', 'b', 'c', 'd', 'e')))
#====================================19=======================================
def sorted_tuple_for_2_elem(t:tuple(tuple())):
    '''Просто сортуємо кортеж по другому елементу'''
    return sorted(t, key=lambda x: x[1])
#print(sorted_tuple_for_2_elem((('a', 23),('b', 37),('c', 11), ('d',29))))

#====================================20=======================================
def remove_empty_strings(s:list):
    '''Просто повертаємо список без порожніх рядків'''
    res = [string for string in s if string != "" and string != '']
    return res
#print(remove_empty_strings(["яблуко", "", "банан", " ", "полуниця", "", '']))

#====================================21=======================================
def calc_uniq(s:str):
    '''Рахуємо кількість унікальних символів в рядку'''
    l = []
    for c in s:
        l.append(c)
    set_l = set(l)
    return len(set_l)

#====================================22=======================================
def profit_price(l:list):
    if l == sorted(l, reverse=True):
        return 0
    profit = 0
    while len(l) > 0:
        min_ = min(l)
        n = l.index(min_)
        max_ = max(l[n:])
        l.pop(n)
        if max_ - min_ > profit:
            profit = max_ - min_
    return profit

#====================================23=======================================
def find_maxkey(d:dict):
    '''Шукаємо ключ з максимальним значенням.
    Спочатку сортуємо словник, який отримуємо на вході.
    Далі отримуємо максимальне значення, як останній елемент відсортованого
    сорвника. В кінці просто додаємо значення, які співпали в список і
    повертаємо його'''
    sorted_d = sorted(d.items(), key=lambda x:x[1])
    max_v = sorted_d[-1][-1]
    max_key_list = []
    for k, v in d.items():
        if v == max_v:
            max_key_list.append(k)
    return max_key_list

d = {'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90, 'q':1}
print(find_maxkey(d))
#====================================24=======================================
def encrypt():
    '''Цікаве шифрування. Простіше словами пояснити, ніж писати'''
    s = list(input('Введіть рядок для шифрування: '))
    even_l = []
    odd_l = []
    for i in range(len(s)):
        if i % 2 == 0:
            even_l.append(s[i])
        else:
            odd_l.append(s[i])
    print(''.join(even_l + odd_l))
#encrypt()

def decrypt():
    '''Цікаве дешифрування. Тут так само)'''
    s = list(input('Введіть рядок для дешифрування: '))
    h = len(s)//2
    pair = s[0:h+1]
    odd = s[-h:]
    res = []
    for i in range(h):
        res.append(pair[i])
        res.append(odd[i])
    if len(s) % 2 == 1:
        res.append(pair[-1])
    print(''.join(res))
#decrypt()
#====================================25=======================================
def find_keys(d1:dict, d2:dict):
    k1 = set(d1.keys())
    k2 = set(d2.keys())
    c_k = k1.intersection(k2)
    return c_k

# d1 = {'q': 1, 'w': 2, 'e': 3}
# d2 = {'e': 4, 'w': 5, 'z': 6}
# c_k = find_keys(d1, d2)
# print("Спільні ключі: ", c_k)
#====================================26=======================================
def is_anagram(s:str, t:str):
    '''Функцiя перевiряє, чи є два рядка анаграмами один одного.
    Приймає два рядки: s i t, далi створює списки на основi цих
    рядкiв.
    Вже пiсля цього порiвнює множини цих спискiв

    Повертає False, якщо довжина цих рядкiв рiзна
    Також повертає False, якщо рядки не є анаграмами один одного'''
    if len(s) != len(t):
        return False

    l_s = []
    l_t = []
    for c in s:
        l_s.append(c)
    for c in t:
        l_t.append(c)

    return set(l_s) == set(l_t)

# print(is_anagram('qwerty', 'ewqrty'))
#====================================27=======================================
def twoSum(nums:list[int], target:int):
    res = []
    for i, v1 in enumerate(nums):
        for j, v2 in enumerate(nums):
            if v1 + v2 == target and v1 != v2:
                res.append(i)
                res.append(j)
                return res

#print(twoSum([1,8,12,5], 13))
#====================================28=======================================
def freq_elem(nums:list[int], k:int):
    if len(set(nums)) < k:
        return []

    c = {}
    for i, v in enumerate(nums):
        if v in c:
            c[v] += 1
        else:
            c[v] = 1

    sorted_c = sorted(c.items(), key=lambda x:x[1])
    res = []

    for i in range(k):
        res.append(sorted_c[i][0])
    return res

#print(freq_elem([1,1,1,2,2,3, 4, 4], 3))
#====================================29=======================================
def threeSum(nums: list[int]):
    '''Простіше на словах пояснити'''
    if len(nums) < 3:
        return []

    results = {}
    vals = {}

    for i, v in enumerate(nums):
        if v in vals:
            vals[v] += 1
        else:
            vals[v] = 1

    for i, num in enumerate(vals.keys()):
        for j in list(vals.keys())[i:]:

            if num == j and vals[num] < 2:
                continue

            target_val = -(num+j)
            if target_val in vals:
                valid = False
                if vals[target_val] > 2:
                    valid = True
                else:
                    if num != target_val and j != target_val:
                        valid = True

                if valid and tuple(sorted((num, j, target_val))) not in results:
                    results[tuple(sorted((num, j, target_val)))] = True

    return [list(r) for r in results.keys()]

#print(threeSum([-1,0,1,2,-1,-4, 0, 4]))
#====================================30=======================================
def is_in_matrix(matrix, target):
    '''Цікаве і корисне завдання)
    Тут в нас як би бінарний пошук, але для матриці.
    Пошук цілі в матриці виконується за O(log(n*m)), що сильно пришвидшує
    його роботу, порівняно з більш простими варіантами з двома циклами, які
    мають складність O(n*m). Оскільки значно зменшує кількість операцій в
    найгіршому випадку'''
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

target = 11

# if is_in_matrix(matrix, target):
#     print(f"{target} знайдено в матриці.")
# else:
#     print(f"{target} не знайдено в матриці.")
