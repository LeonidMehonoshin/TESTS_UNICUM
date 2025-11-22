import time, random, re
from datetime import datetime
import asyncio

def pizza_types_get():
    return {
        'types': [
            'Неаполитанская',
            'Кальцоне',
            'Римская',
            'В нарезке',
            'Сицилийская',
            '\n    Кастомная:'
        ],
        'pizza_list': {
            'size1': (
                '\nНазвание и цена:\n'
                '0) Неаполитанская(1$)\n'
                '1) Кальцоне(2$)\n'
                '2) Римская(3$)\n'
                '3) В нарезке(4$)\n'
                '4) Сицилийская(5$)\n'
                '5) Кастомная!(999$)\n: '
            ),
            'size2': (
                '\nНазвание и цена:\n'
                '0) Неаполитанская(2$)\n'
                '1) Кальцоне(4$)\n'
                '2) Римская(6$)\n'
                '3) В нарезке(8$)\n'
                '4) Сицилийская(10$)\n'
                '5) Кастомная!(1998$)\n: '
            ),
        }
    }
def tale_print():
    print(
        '\n############\n'
        '# Грустн   ###########\n'
        '#       ая    Пиц    #\n'
        '###########      ца  #\n'
        '           ###########\n'
        '\n#########################\n'
        '#       ПИЦЦА>> ____    #\n'
        '#           O  |    |   #\n'
        '#          ||\\ |.   |   #\n'
        '#          ,,  |____|   #\n'
        '#########################\n'
        'вы шли по улице, увидели вывеску\n'
        'и решили зайти туда\n'
    )
    time.sleep(2)
    print(
        '\n#########################\n'
        '#               ____    #\n'
        '# Здрасьте! <- / _ _\\   #\n'
        '#              |  ()|   #\n'
        '#               \\__/    #\n'
        '#########################\n'
    )

def custom_night(number_error):
    custom_options = {
        'meat':
            number_error({
                'text': '\n\nСколько добавить жидкого мяса?(в попугаях 1-10)\n: ',
                'min': 1, 'max': 10
            }),
        'green':
            number_error({
                'text': '\nСколько добавить зелёнки?(в волчьих ягодах 1-10)\n: ',
                'min': 1, 'max': 10
            }),
        'ketchnnaise':
            number_error({
                'text': '\nСколько добавить ketchnnaise?(в Ʞетчунезахъ 1-10)\n: ',
                'min': 1, 'max': 10
            }),
        'cheese':
            number_error({
                'text': '\nСколько добавить сырочка?(в крысах 1-10)\n: ',
                'min': 1, 'max': 10
            }),
        'mushroom':
            number_error({
                'text': '\nСколько добавить грибочков?(в мухоморах 1-10)\n: ',
                'min': 1, 'max': 10
            })
    }
    return [
        '        жидкое мясо: ' + str(custom_options['meat']),
        '\n        зеленёнка: ' + str(custom_options['green']),
        '\n        ketchnnaise' + str(custom_options['ketchnnaise']),
        '\n        сырочек: ' + str(custom_options['cheese']),
        '\n        грибочки: ' + str(custom_options['mushroom'])
    ]

def year_and_size_get(number_error, year):
    years = number_error({
        'text': 'Год рождения\n: ',
        'min': year - 2000, 'max': year - 3
    })

    if years <= year - 18:
        size = number_error({
            'text': ('\nРазмер(в километрах 1-2)\n: '),
            'min': 1, 'max': 2
        })
        return f'\nРазмер: {size}', years
    else: return '', years
def id_get():
    tale_print()
    phone_num = email = ''

    while (
        not re.search(r'\D+.\D+', email)
        and not re.search(r'\D+.\d+', email)
        and not re.search(r'\d+.\D+', email)
        and not re.search(r'\D+.\D', email)
        and not re.search(r'\D+.\d', email)
        and not re.search(r'\d+.\D', email)
    ): email = input('Email: ')

    while (
            not re.search(r'\D\d+\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
            and not re.search(r'\d+\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
            and not re.search(r'\d+\d\d\d\d\d\d\d\d\d\d', phone_num)
            and not re.search(r'\D\d\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
            and not re.search(r'\d\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
            and not re.search(r'\d\d\d\d\d\d\d\d\d\d\d', phone_num)
    ): phone_num = input('Номер телефона: ')

    return phone_num, email
def please_check(day, month, year, custom_options, size, years, email, phone_num, total, pizza_type_text):
    print(
        f'            {day}.{month}.{year}'
        f'\n.........Кассовый чек №{random.randint(0,2000)}........'
        f'\nНазвание: {pizza_type_text}',
        *custom_options,
        size,
        f'\nГод рождения: {years}'
        f'\nEmail: {email}'
        f'\nНомер телефона: {phone_num}'
        f'\nИТОГО: {total}$'
        '\n|| ||| ||||| ||||| ||| ||'
        f'\n........СПАСИБО ЗА ПОКУПКУ!.......'
        '\n  сеть пиццерий "Грустная пицца"'
    )

def choice_pizza(number_error):
    pizza_types = pizza_types_get()['types']
    pizza_list = pizza_types_get()['pizza_list']

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year

    phone_num, email = id_get()
    size, years = year_and_size_get(number_error, year)

    if size == 'Размер: 2':
        pizza_type = number_error({
            'text': pizza_list['size2'],
            'min': 0, 'max': 5
        })
    else:
        pizza_type = number_error({
            'text': pizza_list['size1'],
            'min': 0, 'max': 5
        })

    custom_options = ''
    if pizza_type == 5: custom_options = custom_night(number_error)

    total_types = [1, 2, 3, 4, 5, 999]
    if size == 2: total_types = [2, 4, 6, 8, 10, 1998]

    total = total_types[pizza_type]
    pizza_type_text = pizza_types[pizza_type]

    please_check(
        day, month, year,
        custom_options, size,
        years, email, phone_num,
        total, pizza_type_text
    )

@choice_pizza
def number_error(options):
    while True:
        try:
            num = int(input(options['text']))
            if num <= options['max'] and num >= options['min']: break
            else: print('\nПроверьте условие ввода числа!\n')
        except ValueError: print('\nНеверный формат данных\n')
    return num

async def goodbye_print():
    await asyncio.sleep(3)
    print(
        '\n############################\n'
        '#                  ____    #\n'
        '# До свидания! <- / _ _\\   #\n'
        '#                 |  ()|   #\n'
        '#                  \\__/    #\n'
        '############################\n'
    )
async def thank_you():
    await asyncio.sleep(3)
    print(
        '\n####################################\n'
        '#                          ____    #\n'
        '#  Спасибо за покупку! <- / _ _\\   #\n'
        '#                         |  ()|   #\n'
        '#                          \\__/    #\n'
        '####################################\n'
    )
loop = asyncio.get_event_loop()
task1 = loop.create_task(goodbye_print())
task2 = loop.create_task(thank_you())
loop.run_until_complete(asyncio.wait([task1, task2]))
