import re

def check_password(password):
    # Проверяем длину пароля
    if len(password) < 8:
        return False

    # Проверяем наличие прописных и строчных букв
    if not re.search('[A-Z]', password) or not re.search('[a-z]', password):
        return False

    # Проверяем наличие цифры
    if not re.search('[0-9]', password):
        return False

    # Проверяем наличие специального символа
    if not re.search('[@_!#$%^&*()+=]', password):
        return False

    return True

with open('passwords.txt', 'r') as file:
    for password in file:
        password = password.strip()
        if check_password(password):
            print(password)
