import random

def guess_the_number():
    # Компьютер загадывает случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    iterration = 0 # счетчик попыток
    max_attempts = 8 # макс попыток

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У вас {max_attempts} попыток.")

    while iterration < max_attempts:
        # Получаем предположение игрока
        try:
            guess = int(input(f"Попытка {iterration + 1}. Ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        iterration += 1

        # Проверяем предположение
        if guess < secret_number:
            print("Cлишком маленькое число. Загаданное число больше.")
        elif guess > secret_number:
            print("Cлишком большое число. Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {iterration} попыток!")
            return

    print(f"К сожалению, попытки закончились. Загаданное число было: {secret_number}")

# Запускаем игру
guess_the_number()