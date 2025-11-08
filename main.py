import time, random, re
from datetime import datetime

def choice_pizza(number_error):
    size = 1

    pizza_types = [
        'Неаполитанская',
        'Кальцоне',
        'Римская',
        'В нарезке',
        'Сицилийская',
        'Кастомная'

    ]

    print(
        "\n############\n"
        "# Грустн   ###########\n"
        "#       ая    Пиц    #\n"
        "###########      ца  #\n"
        "           ###########\n"
        "вы видите вывеску...\n"
    )

    time.sleep(3)

    print(
        '\n#########################\n'
        '#       ПИЦЦА>> ____    #\n'
        '#           O  |    |   #\n'
        '#          ||\\ |.   |   #\n'
        '#          ,,  |____|   #\n'
        '#########################\n'
    )

    time.sleep(3)

    print(
        '\n#########################\n'
        '#               ____    #\n'
        '# Здрасьте! <- / _ _\\   #\n'
        '#              |  ()|   #\n'
        '#               \\__/    #\n'
        '#########################\n'
        '\nПицца на ваш выбор:\n'
    )
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year

    phone_num = email = ''
    email_code = str(random.randint(0, 10))
    phone_num_code = str(random.randint(0, 10))
    user_code = -1
    while (
        not re.search(r'\D+.\D+', email)
        and not re.search(r'\D+.\d+', email)
        and not re.search(r'\d+.\D+', email)
        and not re.search(r'\D+.\D', email)
        and not re.search(r'\D+.\d', email)
        and not re.search(r'\d+.\D', email)
    ): email = input('Email: ')
    while user_code != email_code: user_code = input('Введите код, отправленный на почту (от 0 до 10): ')
    while (
        not re.search(r'\D\d+\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d+\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d+\d\d\d\d\d\d\d\d\d\d', phone_num)
        and not re.search(r'\D\d\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d\D\d\d\d\D\d\d\d\D\d\d\D\d\d', phone_num)
        and not re.search(r'\d\d\d\d\d\d\d\d\d\d\d', phone_num)
    ): phone_num = input('Номер телефона: ')
    while user_code != phone_num_code: user_code = input('Введите код, отправленный на номер (от 0 до 10): ')

    years = number_error({
        'text': 'Год рождения\n: ',
        'min': year - 2000, 'max': year - 3
    })

    if years >= 18:
        size = number_error({
            'text': ('\nРазмер(в километрах 1-2)\n: '),
            'min': 1, 'max': 2
        })

    if size == 1:
        pizza_type = number_error({
            'text':(
                '\nНазвание и цена:\n'
                '0) Неаполитанская(1$)\n'
                '1) Кальцоне(2$)\n'
                '2) Римская(3$)\n'
                '3) В нарезке(4$)\n'
                '4) Сицилийская(5$)\n'
                '5) Кастомная!(999$)\n: '
            ),
            'min': 0, 'max': 5
        })

    elif size == 2:
        pizza_type = number_error({
            'text':(
                '\nНазвание и цена:\n'
                '0) Неаполитанская(2$)\n'
                '1) Кальцоне(4$)\n'
                '2) Римская(6$)\n'
                '3) В нарезке(8$)\n'
                '4) Сицилийская(10$)\n'
                '5) Кастомная!(1998$)\n: '
            ),
            'min': 0, 'max': 5
        })

    if pizza_type == 5:
        meat = number_error({
            'text': '\n\nСколько добавить мяса?(в попугаях 1-10)\n: ',
            'min': 1, 'max': 10
        })
        green = number_error({
            'text': '\nСколько добавить зелени?(в травах 1-10)\n: ',
            'min': 1, 'max': 10
        })
        ketchnnaise = number_error({
            'text': '\nСколько добавить ketchnnaise?(в Ʞетчунезахъ 1-10)\n: ',
            'min': 1, 'max': 10
        })
        cheese = number_error({
            'text': '\nСколько добавить сыра?(в крысах 1-10)\n: ',
            'min': 1, 'max': 10
        })
        mushroom = number_error({
            'text': '\nСколько добавить грибочков?(в мухоморах 1-10)\n: ',
            'min': 1, 'max': 10
        })

    total_types = [1, 2, 3, 4, 5, 999]
    if size == 2: total_types = [2, 4, 6, 8, 10, 1998]
    print(pizza_type)
    total = total_types[pizza_type]
    pizza_type_text = pizza_types[pizza_type]

    print(f'            {day}.{month}.{year}'
          f'\n.........Кассовый чек №{random.randint(0,2000)}........')

    if pizza_type == 5:
        print(
            f'Название: Кастомная:\n'
            f'  мясо: {meat}\n'
            f'  зелень: {green}\n'
            f'  кетчунез: {ketchnnaise}\n'
            f'  сыра: {cheese}\n'
            f'  грибочков: {mushroom}'
        )
    else: print(f'Название: {pizza_type_text}')
    if years <= year - 18: print(f'Размер пиццы: {size}')
    print(f'Год рождения: {year}\n')
    print(f'Email: {email}')
    print(f'Номер телефона: {phone_num}')

    print(
        f'ИТОГ: {total}$\n'
        '|| ||| ||||| ||||| ||| ||\n'
        f'........СПАСИБО ЗА ПОКУПКУ!.......\n'
        '  сеть пиццерий "Грустная пицца"'
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
