def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."

def task2(num1, num2):
    try:
        product = float(num1) * float(num2)
        return product
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."

def task3(input_value):
    if not isinstance(input_value, str):
        return "Error: Please enter a string, not a numeric value."
    return len(input_value)

def task4(int_list):
    total = 0
    for item in int_list:
        if not isinstance(item, int):
            return None
        total += item
    return total

def task5(student_grades):
    try:
        result = []
        for name, grades in student_grades:
            average = sum(grades) / len(grades)
            result.append((average, name))
        return result
    except Exception as e:
        return "List processing error!"







