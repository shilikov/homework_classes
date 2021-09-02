from random import randint


# Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»
#
# Привет! Домашняя работа по данной теме является продолжением квиза к предыдущей лекции.
# Мы продолжим реализовывать логику функционала учебной группы в парадигме ООП. Удачи!
#
# Задание № 1. Наследование
#
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов
# (вы можете взять этот код за основу или написать свой).
# Студентов пока оставим без изменения, а вот преподаватели бывают разные,
# поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer
# (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
# А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.
#
# Задание № 2. Атрибуты и взаимодействие классов.
#
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки
# за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
# в котором ключи – названия курсов, а значения – списки оценок).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
#
# Задание № 3. Полиморфизм и магические методы
#
# Перегрузите магический метод __str__ у всех классов.
'''
У проверяющих он должен выводить информацию в следующем виде:
print(some_reviewer)
Имя: Some
Фамилия: Buddy
'''
from functools import reduce

'''
У лекторов:
print(some_lecturer)
Имя: Some
Фамилия: Buddy
Средняя оценка за лекции: 9.9
'''

'''
А у студентов так:
print(some_student)
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование
'''
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
# по средней оценке за лекции и студентов по средней оценке за домашние задания.


# Задание № 4. Полевые испытания
#
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#
# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).
#
#

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grad = {}
        self.python = {}
        self.git = {}

    def __str__(self):
        pass
        return f'{self.name, self.surname}"\n' \
               f' средний бал за лекции {"{:.1f}".format(self.grad)}"\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}"\n' \
               f'Завершенные курсы: {str(self.finished_courses)}'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                if grade in range(1, 11):
                    lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def averag_ecore(self):
        st_list = []
        for grade in self.grades.values():
            for mark in grade:
                st_list.append(mark)
        self.grad = sum(st_list) / len(st_list)
        return self.grad


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        if self.grad < other.grad:
            print(f'Лучший студент {self}')
            return self.grad < other.grad

        if other.grad < self.grad:
            print(f'Лучший студент {other}')
            return self.grad < other.grad



    def ikvel(self, oser, cours):
        if not isinstance(oser, Student):
            print('Not a Lecturer!')
            return
        self.j = self.grades[cours]
        oser.j = oser.grades[cours]
        self.python = (sum(self.j) / len(self.j))
        oser.python = (sum(oser.j) / len(oser.j))
        if self.python > oser.python:
            print(f'лучший студент {cours} {self}')
        else:
            print(f'лучший студент {cours} {oser}')
            return self.python > oser.python


    # def ikvel(self, oser, cours):
    #     if not isinstance(oser, Student):
    #         print('Not a Lecturer!')
    #         return
    #     self.j = self.grades[cours]
    #     oser.j = oser.grades[cours]
    #     self.python = (sum(self.j) / len(self.j))
    #     oser.python = (sum(oser.j) / len(oser.j))
    #     if self.python > oser.python:
    #         print(f'лучший студент Python {self}')
    #     elif print(f'лучший студент Python {oser}'):
    #        return
    #     else:
    #         self.k = self.grades[cours]
    #         oser.k = oser.grades[cours]
    #         self.git = (sum(self.j) / len(self.j))
    #         oser.git = (sum(self.j) / len(self.j))
    #         if self.python > oser.python:
    #             print(f'лучший студент Git {self}')
    #         else:
    #             print(f'лучший студент Git {oser}')





class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'{self.name}, {self.surname}"\n"'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentors):
    def __init__(self, name, sorname):
        super().__init__(name, sorname)
        self.grades = {}
        self.name = name
        self.grad = {}
        self.python ={}
        self.git = {}

    def __str__(self):
        return f'{self.name, self.surname}"\n' \
               f' средний бал за лекции {"{:.1f}".format(self.grad)}"'

    def averag_ecore(self):
        lk_list = []
        for grade in self.grades.values():
            for mark in grade:
                lk_list.append(mark)
        self.grad = sum(lk_list) / len(lk_list)
        return self.grad

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        if self.grad < other.grad:
            print(f'Лучший преподователь {self}')
            return self.grad < other.grad

        if other.grad < self.grad:
            print(f'Лучший преподователь {other}')
            return self.grad < other.grad


    def ikvel(self, oser, cours):
        if not isinstance(oser, Lecturer):
            print('Not a Lecturer!')
            return
        self.j = self.grades[cours]
        oser.j = oser.grades[cours]
        self.python = (sum(self.j) / len(self.j))
        oser.python = (sum(oser.j) / len(oser.j))
        if self.python > oser.python:
            print(f'лучший преподователь {cours} {self}')
        else:
            print(f'лучший преподователь {cours} {oser}')
            return self.python > oser.python
        # if not isinstance(oser, Lecturer):
        #     print('Not a Lecturer!')
        #     return
        # self.k = self.grades[cours]
        # oser.k = oser.grades[cours]
        # self.git = (sum(self.j) / len(self.j))
        # oser.git = (sum(self.j) / len(self.j))
        # if self.git > oser.git:
        #     print(f'лучший преподователь Git {self}')
        # else:
        #     print(f'лучший преподователь Git {oser}')
        #     return self.git > oser.git






ruoy = Student('Ruoy', 'Eman', 'your_gender')
ruoy.courses_in_progress += ['Python']
ruoy.courses_in_progress += ['Git']
sader = Student('Sader', 'Derty', 'your_gender')
sader.courses_in_progress += ['Python']
sader.courses_in_progress += ['Git']
ruoy.add_courses('Введение в программирование')
sader.add_courses('Введение в программирование')
mas = Student('asdf', 'asdsdsada', 'werrwr')
mas.courses_in_progress += ['Python']
mas.courses_in_progress += ['Git']







Some = Reviewer('Some', 'Buddy')
Some.courses_attached += ['Python']
Some.courses_attached += ['Git']
dan = Reviewer('Denis', 'Lim')
dan.courses_attached += ['Python']
dan.courses_attached += ['Git']


rew1 = Reviewer('Some', 'Buddy')
rew1.courses_attached += ['Python']
rew1.courses_attached += ['Git']

elizar = Lecturer('Elizar', 'Fishman')
elizar.courses_attached += ['Python']
elizar.courses_attached += ['Git']
ripli = Lecturer('Ripli', 'Sun')
ripli.courses_attached += ['Python']
ripli.courses_attached += ['Git']

for k in range(1, 11):
    sader.rate_hw(elizar, 'Python', randint(7, 10))
    sader.rate_hw(elizar, 'Git', randint(7, 10))
    sader.rate_hw(ripli, 'Python', randint(7, 10))
    sader.rate_hw(ripli, 'Git', randint(7, 10))

    ruoy.rate_hw(elizar, 'Python', randint(7, 10))
    ruoy.rate_hw(elizar, 'Git', randint(7, 10))
    ruoy.rate_hw(ripli, 'Python', randint(7, 10))
    ruoy.rate_hw(ripli, 'Git', randint(7, 10))

    Some.rate_hw(ruoy, 'Python', randint(7, 10))
    Some.rate_hw(sader, 'Python', randint(7, 10))
    Some.rate_hw(ruoy, 'Git', randint(7, 10))
    Some.rate_hw(sader, 'Git', randint(7, 10))


    dan.rate_hw(ruoy, 'Python', randint(7, 10))
    dan.rate_hw(sader, 'Python', randint(7, 10))
    dan.rate_hw(ruoy, 'Git', randint(7, 10))
    dan.rate_hw(sader, 'Git', randint(7, 10))
    dan.rate_hw(mas, 'Git', randint(10, 10))




enrollee = [ruoy, sader
            ]
cour = ['Python','Git'
        ]
def st_grades(course, *split):
    i = []
    while len(i) < len(split):
        i.append(enrollee)
        k = (i[0][0].grades[course])
        k += i[0][1].grades[course]
        print(f'средний бал всех студентов за курс {course} - {"{:.1f}".format(sum(k) / len(k))}')
        break

def st_grade_kurs(course, enrollee):
    st_list = []
    for student in enrollee:
        if student.grades.get(course) != None:
            for kurs in student.grades.get(course):
                st_list.append(kurs)
        else:
            pass
    avg_grade_kurs = sum(st_list) / len(st_list)
    print(f'средний бал всех студентов {course}- {"{:.1f}".format(avg_grade_kurs)}')
    return avg_grade_kurs

leckturrr = [elizar, ripli]
def lk_grades(course, *split):
    i = []
    while len(i) < len(split):
        i.append(leckturrr)
        k = (i[0][0].grades[course])
        k += i[0][1].grades[course]
        print(f'средний бал всех лекторов {course}- {"{:.1f}".format(sum(k) / len(k))}')
        break

def lk_grade_kurs(course, leckturrr):
    lk_list = []
    for lekt in leckturrr:
        if lekt.grades.get(course) != None:
            for kurs in lekt.grades.get(course):
                lk_list.append(kurs)
        else:
            pass
    avg_grade_kurs = sum(lk_list) / len(lk_list)
    print(f'средний бал всех преподователей {course}- {"{:.1f}".format(avg_grade_kurs)}')
    return avg_grade_kurs



print('{txt:>30}'.format(txt='общие данные проверяющего'))
print()
print(dan)
print()
print('{txt:>30}'.format(txt='общие данные проверяющего'))
print()
print(Some)
print()

lecturer = Lecturer
print('{txt:>30}'.format(txt='средний бал студента elizar'))
print()
lecturer.averag_ecore(elizar)
print()
print('{txt:>30}'.format(txt='средний бал студента ripli'))
print()
lecturer.averag_ecore(ripli)
print()
print('{txt:>30}'.format(txt='общие данные преподователя'))
print()
print(f'{elizar}')
print()
print('{txt:>30}'.format(txt='общие данные преподователя'))
print()
print(ripli)
print()

student = Student
print('{txt:>30}'.format(txt='средний бал студента sader'))
print()
student.averag_ecore(sader)
print()
print('{txt:>30}'.format(txt='средний бал студента ruoy'))
print()
student.averag_ecore(ruoy)
print()
print('{txt:>30}'.format(txt='общие данные студента'))
print()
print(ruoy)
print()
print('{txt:>30}'.format(txt='общие данные студента'))
print()
print(sader)
print()
#

print('{txt:>30}'.format(txt='лучший преподователь курса Python'))
print()
lecturer.ikvel(elizar, ripli, 'Python')
print()
print('{txt:>30}'.format(txt='лучший преподователь курса Git'))
print()
lecturer.ikvel(elizar, ripli, 'Git')
print()
print('{txt:>30}'.format(txt='лучший студент курса Python'))
print()
student.ikvel(ruoy, sader, 'Python')
print()

print('{txt:>30}'.format(txt='лучший студент курса Git'))
print()
print(student.ikvel(ruoy, sader, 'Git'))

print('{txt:>30}'.format(txt='лучший студент'))
print()
print(sader.__lt__(ruoy))
print('{txt:>30}'.format(txt='лучший преподователь'))
print()
print(elizar.__lt__(ripli))
print()
print('{txt:>30}'.format(txt='средний бал преподователей в рамках курса'))
print()
lk_grades('Python', *leckturrr)
lk_grade_kurs('Git', leckturrr)
print()
print('{txt:>30}'.format(txt='средний бал студентов в рамках курса'))
print()
st_grades('Git', *enrollee)
st_grade_kurs('Python', enrollee)




























