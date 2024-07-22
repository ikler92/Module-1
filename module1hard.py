grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
first_student = sum(grades[0]) / len(grades[0])  # Вычисляем средний балл
second_student = sum(grades[1]) / len(grades[1])
third_student = sum(grades[2]) / len(grades[2])
forth_student = sum(grades[3]) / len(grades[3])
five_student = sum(grades[4]) / len(grades[4])
new_sort_student = list(students)  # Преобразовываем множество в список
list.sort(new_sort_student)  # Сортировка списка по алфавиту
result = {str(new_sort_student[0]): first_student,   # Сопоставление
          str(new_sort_student[1]): second_student,
          str(new_sort_student[2]): third_student,
          str(new_sort_student[3]): forth_student,
          str(new_sort_student[4]): five_student}
print(result)
# print({'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}) Для проверки
