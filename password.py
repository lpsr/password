password = input("Введите пароль: ")


try:
    check = 1 / len(password)
    check = 1 / int(password)
    print("Ваш пароль состоит только из цифр")
except ZeroDivisionError:
    print("Вы ввели пустой пароль")
except ValueError:
    print("Требования к паролю соблюдены")
except:
    print("Неизвестная ошибка")
