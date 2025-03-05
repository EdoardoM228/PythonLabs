# 1. Приветствие пользователя
user_name = input("Enter your name: ")
print(f"Hi, {user_name}! Welcome!")

# 2. Определение переменных
device_name = "MacBook"
device_age = 2
is_under_warranty = True

# 3. Вывод типов данных
print(type(user_name))
print(type(device_name))
print(type(device_age))
print(type(is_under_warranty))

# 4. Преобразование имени в нижний регистр
lower_name = user_name.lower()

# Создание строки "user_name__device_name"
combined_string = f"{user_name}__{device_name}"

# Вывод длины строки
print(len(combined_string))

# 5. Форматированная строка
print(f"{user_name} недавно приобрел {device_name}, которому всего {device_age} лет.")

# 6. Проверка, является ли имя устройства палиндромом
is_palindrome = device_name.lower() == device_name.lower()[::-1]
print(is_palindrome)

# 7. Очистка строки от лишних пробелов
our_text = "We     are located  on Pushkin      Street.   "
result = " ".join(our_text.split())
print(result)

# 8. Маскировка номера карты
card = '5468350018455833'
result = '*' * (len(card) - 4) + card[-4:]
print(result)

# 9. Поиск индекса 10 и количества 9 в списке
my_list = [1, 9, 0, 9, 10]
ten_index = my_list.index(10)
nine_count = my_list.count(9)
print(ten_index, nine_count)

# 10. Обновление списка имен, дат и сортировка элементов
names = ['Peter', 'Maria', 'Alexander', 'Olga']
names.extend(['Ann', 'Bob'])

dates = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18]
del dates[1]  # удаляем второй элемент
del dates[5]  # удаляем седьмой элемент (учитывая сдвиг)
del dates[-1] # удаляем последний элемент

items = ['Lamp', 'Table', 'Book', 'Pen', 'Notebook']
items.sort()

print(names)
print(dates)
print(items)

# 11. Доступные товары
catalog = {"Laptop", "Smartphone", "Headphones", "Camera", "Tablet"}
out_of_stock = {"Camera", "Tablet"}
available_items = catalog - out_of_stock
print(available_items)

# 12. Удаление элемента из множества
my_set = {0, 10, 100}
to_delete = 0
my_set.discard(to_delete)  # безопасное удаление
print(my_set)

# 13. Работа с кортежами
product_info = ("John Doe", "Electronics Store", "Laptop", "15-inch", "Intel i7", "16GB RAM")
contains_laptop = "Laptop" in product_info

seller_info = product_info[:2]
product_details = product_info[2:]

print(contains_laptop)
print(seller_info)
print(product_details)

# 14. Создание словаря с максимальным расходом
customer = {
    "owner_name": "Maria",
    "expenses": [120, 200, 150, 300, 250]
}
summary = {
    "owner_name": customer["owner_name"],
    "max_expense": max(customer["expenses"])
}
print(summary)
