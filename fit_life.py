import sys
print('Привет! Я цифровой Фитнес-бот, помогаю следить за вашим здоровьем')

user_input_name = input('Как вас зовут?:')
user_name = user_input_name.capitalize()

while True:
    user_input_age = input('Сколько вам полных лет?:')
    if user_input_age == 'стоп':
        print(f"Опрос завершен, {user_name}, до встречи!")
        sys.exit(1)
    try:
        user_age = int(user_input_age)
        break
    except ValueError:
        print(f'Ошибка: Введенный возраст {user_input_age} не является числом')
        print("Попробуйте снова ввести целое число или стоп для выхода\n")
WATER_PER_KG = 30
ML_PER_LITER = 1000
print("Мне нужен ваш вес и рост для расчета ИМТ и рекомендуемой нормы воды")

user_input_weight = input(f'{user_name}, укажите ваш вес в кг: ')
user_weight = float(user_input_weight)

user_input_height = input('Укажите ваш рост в метрах, например, 1.75: ')
user_height = float(user_input_height.replace(",", "."))

# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round((user_weight / (user_height ** 2)), 1)
# Подсчет воды: (вес * 30 мл) / 1000
water_l = (user_weight * WATER_PER_KG) / ML_PER_LITER

# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)\n")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.2f} литра в день")
print(f"Расчет окончен. {user_name}, Будьте здоровы!")
