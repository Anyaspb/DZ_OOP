class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_total = []

    def __str__(self):
        grade_sum = 0
        lens = 0
        for i in range(len(list(self.grades.values()))):
            lens += len(list(self.grades.values())[i])
        for i in list(self.grades.values()):
            for x in i:
                grade_sum += x
        self.average_total = grade_sum / lens

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за задания: {self.average_total}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student!")
            return
        return self.average_total > other.average_total


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_total = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __str__(self):
        grade_sum = 0
        lens = 0
        for i in range(len(list(self.grades.values()))):
            lens += len(list(self.grades.values())[i])
        for i in list(self.grades.values()):
            for x in i:
                grade_sum += x
        self.average_total = grade_sum / lens

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_total}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecturer!")
            return
        return self.average_total > other.average_total


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Anna', 'S', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['GIT']
best_student2.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['GIT']

cool_lecturer = Lecturer('Sam', 'Smith')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']
cool_lecturer2 = Lecturer('Elon', 'Musk')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['GIT']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'GIT', 9)
cool_mentor.rate_hw(best_student, 'GIT', 9)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'GIT', 10)
cool_mentor.rate_hw(best_student2, 'GIT', 10)

best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'GIT', 9)
best_student.rate_lec(cool_lecturer, 'GIT', 9)
best_student2.rate_lec(cool_lecturer2, 'Python', 10)
best_student2.rate_lec(cool_lecturer2, 'Python', 10)
best_student2.rate_lec(cool_lecturer2, 'Python', 10)
best_student.rate_lec(cool_lecturer2, 'GIT', 7)


# print(cool_mentor)
#
# print(best_student)
# print(best_student2)
# print(best_student.__lt__(best_student2))
#
# print(cool_lecturer)
# print(cool_lecturer2)
# print(cool_lecturer2.__lt__(cool_lecturer))


# Задание 4

def average_homework_grade(student_list, course):
    res = 0
    qty = 0
    for student in student_list:
        course_grades = student.grades[course]
        qty += len(student.grades[course])
        for i in course_grades:
            res += i
    average = res / qty
    return average


print(average_homework_grade([best_student, best_student2], 'GIT'))


def average_lecture_grade(lecturer_list, course):
    res = 0
    qty = 0
    for lecturer in lecturer_list:
        course_grades = lecturer.grades[course]
        qty += len(lecturer.grades[course])
        for i in course_grades:
            res += i
    average = res / qty
    return average


print(average_lecture_grade([cool_lecturer, cool_lecturer2], 'GIT'))
