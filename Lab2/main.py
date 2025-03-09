# Проверка, является ли участок квадратным
length = 121
width = 100
result = length == width
print(result)

# Условия выплаты премий
salary = 150000
work_experience = 3
if work_experience < 3:
    result = 0
elif 3 <= work_experience <= 6:
    result = 2 * salary
elif 7 <= work_experience <= 15:
    result = 5 * salary
else:
    result = 10 * salary
print(result)

# Поиск доступных товаров
sales = {
    "laptop": 700,
    "smartphone": 100,
    "headphones": 50,
    "mouse": 20,
    "keyboard": 40
}
affordable_products = [product for product, price in sales.items() if price <= 500]
print(affordable_products)

# Проверка на противоположные списки
def are_antipodes(lst_1, lst_2):
    return sorted(lst_1) == sorted(lst_2)

lst_1 = ["1", "0", "0", "1"]
lst_2 = ["0", "1", "1", "0"]
result = are_antipodes(lst_1, lst_2)
print(result)

# Проверка сумм на диагоналях
m = [[1, 23, 4],
     [3, 2, 1],
     [1, 3, 4]]
primary_diagonal = sum(m[i][i] for i in range(len(m)))
secondary_diagonal = sum(m[i][len(m)-1-i] for i in range(len(m)))
result = primary_diagonal == secondary_diagonal
print(result)

# Сортировка и фильтрация списка кортежей
input_list = [('Anna', 13), ('Ivan', 20), ('Irina', 23), ('Olga', 25),
              ('Ivan', 30), ('Oleg', 24), ('Olga', 26)]
result = sorted(filter(lambda x: x[1] % 5 == 0, input_list), key=lambda x: x[1], reverse=True)
print(result)

# Гипотеза Коллатца
def collatz_conjecture(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

print(collatz_conjecture(8))  # -> [8, 4, 2, 1]
print(collatz_conjecture(3))  # -> [3, 10, 5, 16, 8, 4, 2, 1]
