



from random import randint

from termcolor import cprint







class Student:
    def __init__(self, name, surname, gender, *course):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.person = {}
        self.course = course




    def __str__(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}, {self.finished_courses}, "\n"' \
               f'Pytson - {self.grades["Python"]}, "\n" Git - {self.grades["Git"]}"\n"' \
               f' средний бал {self.person[self.name]}'



    def rate_hw(self, lekt, course, grade):
        if isinstance(lekt, Lecturer) and course in lecturer.courses_attached \
                and course in lekt.courses_in_progress:
            if course in lekt.lector_grades:
                lekt.lector_grades[course] += [grade]

            else:
                lekt.lector_grades[course] = [grade]

        else:
            return 'Ошибка'
        return f"{lekt.lector_grades[course]}"



    def peson_grade(self, grade,):
        if self.course in self.grades:
            self.person[self.name] += grade
        else:
                self.pers = self.grades['Python'] + self.grades['Git']
                # self.jik[self.name] = float(sum(self.grades['Python'] + self.grades['Git']) / len(self.pers))
                self.person[self.name] = float(sum(self.grades['Python'] + self.grades['Git']) / len(self.pers))


    def student_act(self):

            dese = randint(1, 6)
            if dese == 1:
                students.rate_hw(lecturer, 'Python', 10) and \
                students.rate_hw(lecturer, 'Git', 8)
                lecturer.peson_grade(lecturer, 'Elizar')
                lecturer.peson_grade(lecturer, 'Some')


            elif dese == 4:
                students.rate_hw(lecturer, 'Python', 9) and \
                students.rate_hw(lecturer, 'Git', 10)
                lecturer.peson_grade(lecturer, 'Elizar')
                lecturer.peson_grade(lecturer, 'Some')



            elif dese == 5:
                students.rate_hw(lecturer, 'Python', 8) and \
                students.rate_hw(lecturer, 'Git', 9)
                lecturer.peson_grade(lecturer, 'Elizar')
                lecturer.peson_grade(lecturer, 'Some')


            else:
                students.rate_hw(lecturer, 'Python', 10) and \
                students.rate_hw(lecturer, 'Git', 10)
                lecturer.peson_grade(lecturer, 'Elizar')
                lecturer.peson_grade(lecturer, 'Some')





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        pass




class Lecturer(Mentor):
    def __init__(self, name, surname, *course):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.courses_attached = []
        self.lector_grades = {}
        self.courses_in_progress = []
        self.person = {}
        self.course = course
        self.person1 = {}
        self.person2 = {}





    def __str__(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}, "\n"' \
               f'Pytson - {self.lector_grades["Python"]}, "\n" Git - {self.lector_grades["Git"]}"\n"' \
               f'общий средний бал за лекции {self.person[self.name]}"\n"' \
               f'средний бал за лекции Python - {self.person1}"\n"' \
               f'средний бал за лекции Git - {self.person2}'

    def reed_lection(self, cours,):
        print(f'ghjxbnfk ntrwb - {cours}')

    def peson_grade(self, grade, name, *course):
        if self.course in self.lector_grades:
            print()
            self.person[self.name] += grade
        else:
                self.pers = self.lector_grades['Python'] + self.lector_grades['Git']
                # self.jik = round(sum(self.lector_grades['Python'] + self.lector_grades['Git']) / len(self.pers), 2)
                self.person[name] = round(sum(self.lector_grades['Python'] + self.lector_grades['Git']) / len(self.pers), 2)
                self.person1[self.name] = ("{:.2f}".format(round(sum(self.lector_grades['Python'],
                                                                 2)) / len(self.lector_grades['Python'])))
                self.person2[self.name] = ("{:.2f}".format(round(sum(self.lector_grades['Git'],
                                                                 2)) / len(self.lector_grades['Git'])))

    def __lt__(self, *args, **kwargs):
        if self.person < self.person:
            print('Not a Character!')
            return
        return self.person < self.person, 'gggg'



    def ickvel(self):
        if lecturer.person['Elizar'] < lecturer.person['Some']:
            print('лучший преподователь Some')
        else:
            print('лучший преподователь Elizar')


    def act(self):
        dises = randint(1, 2)
        if dises == 1:
            self.reed_lection('Paython') and self.reed_lection('Git')
        else:
            self.reed_lection('Paython') and self.reed_lection('Git')

# TODO реализовать случайные оценки

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f"{student.grades[course]}"

    def rvw_act(self):

        dese = randint(1, 6)
        if dese == 1:
            reviewer.rate_hw(students, 'Python', 10) and \
            reviewer.rate_hw(students, 'Git', 8)
            students.peson_grade(students)
        elif dese == 4:
            reviewer.rate_hw(students, 'Python', 9) and \
            reviewer.rate_hw(students, 'Git', 10)
            students.peson_grade(students)

        elif dese == 5:
            reviewer.rate_hw(students, 'Python', 8) and \
            reviewer.rate_hw(students, 'Git', 9)
            students.peson_grade(students)

        else:
            reviewer.rate_hw(students, 'Python', 10) and \
            reviewer.rate_hw(students, 'Git', 10)
            students.peson_grade(students)


# реализовать случайные оценки

student = [Student(name="Александр", surname="Фролов", gender='Mail'),
            Student(name="Валерия", surname="Христофорова", gender='Famail',),
            Student(name="Дмитрий", surname="Михеев", gender='Mail',)
            ]

for students in student:
    students.courses_in_progress += ['Python']
    students.courses_in_progress += ['Git']
    students.finished_courses = ['введение в програмирование']


lectur = [Lecturer(name='Some', surname='odoc'),
            Lecturer(name='Elizar', surname='Fishman')]

for lecturer in lectur:
    lecturer.courses_attached += ['Python']
    lecturer.courses_attached += ['Git']
    lecturer.courses_in_progress += ['Python']
    lecturer.courses_in_progress += ['Git']



reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']



for week in range(1, 62, 5):
    cprint(f'========================== {week} ===========================', 'cyan')
    for students in student:
        reviewer.rvw_act()
        # print(students.person)



    cprint(f'========================== игтоги {week} недели ===========================', 'cyan')
    cprint(f'========================== студенты ===========================', 'cyan')

    for students in student:
        cprint(f'{students}', color="yellow")



        # print(students.person)
    cprint(f'========================== преподы ===========================', 'cyan')
    for lecturer in lectur:
        students.student_act()
        cprint(lecturer, color='blue')
        lecturer.person['Some'].__lt__(lecturer.person['Elizar'])
        # lecturer.ickvel()
        # lecturer.peson_grade(lecturer, 'Elizar')
        # lecturer.peson_grade(lecturer, 'Some')
        print(lecturer.person['Elizar'])
        print(lecturer.person['Some'])
        print(f'{(lecturer.person["Elizar"]) == (lecturer.person["Some"])}')
        print(lecturer.person1)
        # break


        # print(lecturer.person['Elizar'] == (lecturer.person['Some']))

        print()



        # lecturer.person.setdefault(lecturer.name), lecturer.person.setdefault(lecturer.name)
        # print(lecturer.person['Elizar'])




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












