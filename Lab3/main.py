import re

# 1. Проверка товарного кода
def check_product_code(code):
    return bool(re.match(r'^[A-Za-z]\d{3}$', code))

# 2. Извлечение информации о книгах
def extract_book_info(data):
    books = data.replace(",", " ").split()
    titles, authors, years = [], [], []
    for i in range(0, len(books), 3):
        titles.append(books[i])
        authors.append(books[i+1])
        years.append(books[i+2])
    return titles, authors, years

# 3. Проверка формата email
def check_email_format(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))

# 4. Проверка ограничений в диете
def check_restrictions(data):
    return bool(re.search(r'lactose|gluten|nutes', data, re.IGNORECASE))

# 5. Извлечение телефонных номеров
def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
    return re.findall(pattern, text)


# Тестирование функций

# Проверка товарного кода
product_code = "B152"
print("Product code valid:", check_product_code(product_code)) 

# Извлечение информации о книгах
data = "The Great Gatsby,F. Scott Fitzgerald,1925 1984,George Orwell,1949 To Kill a Mockingbird,Harper Lee,1960"
titles, authors, years = extract_book_info(data)
print("Titles:", titles)
print("Authors:", authors)
print("Years:", years)

# Проверка email
email = "owner@example.com"
print("Email valid:", check_email_format(email))

# Проверка пищевых ограничений
client_data = "My diet excludes products containing lactose and gluten."
print("Dietary restrictions detected:", check_restrictions(client_data))

# Извлечение телефонных номеров
text = "Hi, here are some phone numbers: (123) 456-7890, 987-654-3210, 555.555.5555, 111 222 3333."
print("Phone numbers:", extract_phone_numbers(text))  
