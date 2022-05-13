def guess_single(user_number, number):
    user_number = int(user_number)

    if user_number > number:
        text_result = 'Неверно. Число должно быть МЕНЬШЕ.'
    elif user_number < number:
        text_result = 'Неверно. Число должно быть БОЛЬШЕ.'
    else:
        text_result = 'Вы победили!'
    return text_result


def try_count(count):
    result = f'Попытка № {count}'
    return result
