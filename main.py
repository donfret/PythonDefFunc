print("Функция 1: ")
def say_hello():
    print("Привет, мир!")

say_hello()
say_hello()


print("Функция 2: ")
def greet2(name):
    print("Привет,", name + "!")

greet2("Анна")
greet2("Олег")


print("Функция 3: ")
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


print("Функция 4: ")
def greet4(name="Гость"):
    print("Привет,", name + "!")

greet4("Анна")
greet4()


print("Функция 5: ")
def subtract(a, b):
    return a - b

print(subtract(10, 5))
print(subtract(a=10, b=5))
print(subtract(b=5, a=10))


print("Функция 6: ")
def introduce(name, city="Москва"):
    return "Меня зовут " + name + ", я из " + city

print(introduce("Анна", "Казань"))
print(introduce("Олег"))


print("Функция 7: ")
def multiply(*numbers):
    result = 1
    for number in numbers:
        result = result * number
    return result

print(multiply(2, 3, 4))
print(multiply(5, 2))
print(multiply())


print("Функция 8: ")
def display_info(name, age, city):
    print("Имя:", name)
    print("Возраст:", age)
    print("Город:", city)

display_info("Анна", 20, "Москва")


print("Функция 9: ")
def order(product, quantity=1, *extra):
    result = "Товар: " + product
    result += ", количество: " + str(quantity)

    for item in extra:
        result += ", дополнение: " + item

    return result

print(order("Телефон"))
print(order("Ноутбук", 2, "Мышь", "Клавиатура"))


print("Функция 10: ")
def profile(name, age=18, **extra):
    result = ["Имя: " + name]
    result.append("Возраст: " + str(age))

    for key, value in extra.items():
        result.append(key + ": " + str(value))

    return result

print(profile("Анна"))
print(profile("Олег", 25, city="Москва", job="Программист"))