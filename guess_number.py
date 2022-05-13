import random

number = random.randint(1, 100)
levels = {
    1: 10,
    2: 7,
    3: 5
}

level = int(input('Выберите уровень сложности (1, 2 или 3): '))
max_count = levels[level]

qty = int(input('Выберите количество игроков: '))
users = []
for i in range(qty):
    user_name = input(f'Игрок {i+1}, введите имя: ')
    users.append(user_name)

count = 0
user_number = 0
while user_number != number:
    count += 1
    if count > max_count:
        print('Попытки закончились. Вы проиграли.')
        print(f'Правильный ответ: {number}')
        break
    print(f'Попытка № {count}')
    for user in users:
        user_number = int(input(f'{user}, введите число: '))
        if user_number > number:
            print('Неверно. Число должно быть меньше.')
        elif user_number < number:
            print('Неверно. Число должно быть больше.')
        else:
            print(f'{user}, вы победили!')
            break
print('Игра окончена.')
