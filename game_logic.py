def guess_single(user_number, number, win_number=None):
    user_number = int(user_number)

    if user_number > number:
        text_result = 'Неверно. Число должно быть МЕНЬШЕ.'
    elif user_number < number:
        text_result = 'Неверно. Число должно быть БОЛЬШЕ.'
    else:
        text_result = 'Вы победили!'
        win_number = number
    return text_result, win_number


def try_count(count, max_count, endgame=None):
    if (count-1) > max_count:
        endgame = 'Попытки закончились. Вы проиграли :-('
    this_count = f'Попытка № {count}'
    return this_count, endgame
