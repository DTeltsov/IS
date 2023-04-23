from constraint import *

# Створюємо об'єкт Problem
problem = Problem()

# Створюємо список студентів та їх занять
students = ['Студент 1', 'Студент 2', 'Студент 3']
student_classes = {
    'Студент 1': ['Математика', 'Фізика', 'Хімія'],
    'Студент 2': ['Математика', 'Інформатика', 'Біологія'],
    'Студент 3': ['Фізика', 'Хімія', 'Біологія']
}

# Створюємо список викладачів та їх занять
teachers = ['Викладач 1', 'Викладач 2', 'Викладач 3']
teacher_classes = {
    'Викладач 1': ['Математика', 'Фізика'],
    'Викладач 2': ['Хімія', 'Біологія'],
    'Викладач 3': ['Інформатика']
}

# Створюємо змінні для кожного заняття
classes = []
for student in students:
    for c in student_classes[student]:
        classes.append((student, c))
for teacher in teachers:
    for c in teacher_classes[teacher]:
        classes.append((teacher, c))

# Додаємо змінні до об'єкту Problem
for c in classes:
    problem.addVariable(c, students + teachers)

# Додаємо обмеження на те, щоб кожен студент мав заняття в різні дні і час
for student in students:
    problem.addConstraint(AllDifferentConstraint(), [c for c in classes if c[0] == student])

# Додаємо обмеження на те, щоб кожен викладач мав заняття в різні дні і час
for teacher in teachers:
    problem.addConstraint(AllDifferentConstraint(), [c for c in classes if c[0] == teacher])

# Розв'язуємо задачу
solution = problem.getSolution()

# Виводимо рішення
for c in sorted(classes):
    print(f"{c[0]} - {c[1]}: {solution[c]}")
