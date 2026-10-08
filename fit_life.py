# Проект FitLife - MVP версия 1.0
# 1. Знакомство
print('Привет! Я цифровой Фитнес-бот, помогаю следить за вашим здоровьем')
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_input_name = input('Как вас зовут?:')
user_name = user_input_name.capitalize()
# TODO: Спроси возраст и сохрани в переменную user_age
user_input_age = input('Сколько вам полных лет?:')
user_age = int(user_input_age)
WATER_PER_KG = 30
ML_PER_LITER = 1000
print("Мне нужен ваш вес и рост для расчета ИМТ и рекомендуемой нормы воды")
# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_input_weight = input('Укажите ваш вес в кг: ')
user_weight = float(user_input_weight)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height
user_input_height = input('Укажите ваш рост в метрах, например, 1.75: ')
user_height = float(user_input_height.replace(",", "."))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = round((user_weight / (user_height ** 2)), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Отчет для пользователя: {user_name} ({user_age} г.)\n")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.2f} литра в день")
print(f"Расчет окончен. {user_name}, Будьте здоровы!")
