# Lab7
Функція task1

def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Помилка: Будь ласка, введіть коректне числове значення для віку."
Опис: Конвертує введене значення age в ціле число.
Вхідні дані: age - Будь-яке значення, яке можна конвертувати в ціле число.
Вихідні дані: Повертає ціле число age, якщо конвертація пройшла успішно. Якщо конвертація не вдалась через ValueError, повертає повідомлення про помилку із запитом ввести коректне числове значення для віку.
Функція task2

def task2(num1, num2):
    try:
        product = float(num1) * float(num2)
        return product
    except ValueError:
        return "Помилка: Будь ласка, введіть коректні числові значення для чисел."
Опис: Обчислює добуток двох чисел (num1 та num2).
Вхідні дані: num1, num2 - Будь-які значення, які можна конвертувати в числа з плаваючою точкою.
Вихідні дані: Повертає добуток num1 та num2, якщо обидва значення є числами. Якщо будь-яке з введених значень не може бути конвертоване в число через ValueError, повертає повідомлення про помилку із запитом ввести коректні числові значення для чисел.
Функція task3

def task3(input_value):
    if not isinstance(input_value, str):
        return "Помилка: Будь ласка, введіть рядок, а не числове значення."
    return len(input_value)
Опис: Перевіряє, чи введене значення input_value є рядком. Якщо так, повертає його довжину. Якщо ні, повертає повідомлення про помилку.
Вхідні дані: input_value - Будь-яке значення для перевірки.
Вихідні дані: Повертає довжину рядка input_value, якщо воно є рядком. Якщо input_value не є рядком (наприклад, числове значення), повертає повідомлення про помилку із запитом ввести рядок.
Функція task4

def task4(int_list):
    total = 0
    for item in int_list:
        if not isinstance(item, int):
            return None
        total += item
    return total
Опис: Обчислює загальну суму цілих чисел у списку (int_list).
Вхідні дані: int_list - Список значень для сумування.
Вихідні дані: Повертає суму всіх цілих чисел у int_list. Якщо будь-який елемент у int_list не є цілим числом, повертає None.
Функція task5

def task5(student_grades):
    try:
        result = []
        for name, grades in student_grades:
            average = sum(grades) / len(grades)
            result.append((average, name))
        return result
    except Exception as e:
        return "Помилка обробки списку!"
Опис: Обчислює середній бал студентів та повертає список кортежів (середній бал, ім'я студента).
Вхідні дані: student_grades - Список кортежів, де кожний кортеж містить ім'я студента та їхні оцінки (список чисел).
Вихідні дані: Повертає список кортежів, де кожен кортеж складається з середнього балу та імені студента. Якщо виникає будь-яка помилка під час обробки списку (наприклад, ділення на нуль), повертає загальне повідомлення про помилку.
Кожна з цих функцій використовує обробку винятків (try-except) для гнучкого контролю за помилками та надання інформативних повідомлень про помилки при невідповідних вхідних даних чи умовах. Кожна функція виконує конкретні завдання з перевіркою даних, обчисленням чи обробкою даних, що гарантує надійність та чіткість при їх використанні.






