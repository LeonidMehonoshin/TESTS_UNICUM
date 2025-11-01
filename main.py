import time, random

def choice_pizza(number_error):
    total = None
    size = 1

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
        '#          ||\\ |.   |    #\n'
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

    years = number_error({
        'text': 'Сколько вам лет(3-2000)\n: ',
        'min': 3, 'max': 200
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
                '1) Неаполитанская(1$)\n'
                '2) Кальцоне(2$)\n'
                '3) Римская(3$)\n'
                '4) В нарезке(4$)\n'
                '5) Сицилийская(5$)\n'
                '6) Кастомная!(999$)\n: '
            ),
            'min': 1, 'max': 6
        })

    elif size == 2:
        pizza_type = number_error({
            'text':(
                '\nНазвание и цена:\n'
                '1) Неаполитанская(2$)\n'
                '2) Кальцоне(4$)\n'
                '3) Римская(6$)\n'
                '4) В нарезке(8$)\n'
                '5) Сицилийская(10$)\n'
                '6) Кастомная!(1998$)\n: '
            ),
            'min': 1, 'max': 6
        })

    if pizza_type == 6:
        meat = number_error({
            'text': '\n\nСколько добавить мяса?(в попугаях 1-10)\n: ',
            'min': 1, 'max': 10
        })
        green = number_error({
            'text': '\nСколько добавить зелени?(в попугаях 1-10)\n: ',
            'min': 1, 'max': 10
        })
        ketchnnaise = number_error({
            'text': '\nСколько добавить ketchnnaise?(в Ʞетчунезахъ 1-10)\n: ',
            'min': 1, 'max': 10
        })

    if size == 2:
        if pizza_type == 1: pizza_type, total = 'Неаполитанская', '2$'
        elif pizza_type == 2: pizza_type, total = 'Кальцоне', '4$'
        elif pizza_type == 3: pizza_type, total = 'Римская', '6$'
        elif pizza_type == 4: pizza_type, total = 'В нарезке', '8$'
        elif pizza_type == 5: pizza_type, total = 'Сицилийская', '10$'
    else:
        if pizza_type == 1: pizza_type, total = 'Неаполитанская', '1$'
        elif pizza_type == 2: pizza_type, total = 'Кальцоне', '2$'
        elif pizza_type == 3: pizza_type, total = 'Римская', '3$'
        elif pizza_type == 4: pizza_type, total = 'В нарезке', '4$'
        elif pizza_type == 5: pizza_type, total = 'Сицилийская', '5$'

    print(f'\n.........Кассовый чек №{random.randint(0,2000)}........')

    if pizza_type == 6:
        if size == 1: total = '999$'
        else: total = '1998$'

        print(
            f'Название: Кастомная:\n'
            f'  мясо: {meat}, зелень: {green}\n'
            f'  кетчунез: {ketchnnaise}'
        )
    else: print(f'Название: {pizza_type}')
    if years >= 18: print(f'Размер пиццы: {size}')

    print(
        f'ИТОГО: {total}\n'
        '\n||||| |||||||||| |||||\n\n'
        f'........СПАСИБО ЗА ПОКУПКУ!.......\n'
        '  сеть пиццерий "Грустная пицца"\n'
    )

@choice_pizza
def number_error(options):
    while True:
        try:
            num = int(input(options['text']))
            if num <= options['max'] and num >= options['min']:
                break
            else:
                print('\nПроверьте условие ввода числа!\n')
        except ValueError:
            print('\nНеверный формат данных\n')
    return num
