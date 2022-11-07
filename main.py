class Student:
    list_students = {}
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # Student.list_students.append(self.name)

    def rate_lec(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def students_general(self, student, course):
    #     if isinstance(student, Student) and course in student.courses_attached and course in self.courses_in_progress:
    #         Student.list_students[self.name] += self.grades
    #     else:
    #         return 'Ошибка'

    def _average_rate(self):
        sum_grade = 0
        sum_element = 0
        average_rate = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum_element += 1
                sum_grade += grade
            average_rate = float("{:.1f}".format(sum_grade / sum_element))
        return average_rate

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rate()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self._average_rate() < other._average_rate()



    # def list_students(self):

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.list_lecturers = {}

    def _average_rate(self):
        sum_grade = 0
        sum_element = 0
        average_rate = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum_element += 1
                sum_grade += grade
            average_rate = float("{:.1f}".format(sum_grade / sum_element))
        return average_rate

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self._average_rate()}'


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
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

# def all_average_students(students, courses):

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['C+']

student_2 = Student('Jon', 'Sigal', 'man')
student_2.courses_in_progress += ['Python']

student_3 = Student('Mike', 'Magical', 'man')
student_3.courses_in_progress += ['C+']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Snape', 'Severus')
reviewer_2.courses_attached += ['C+']

lecture_1 = Lecturer('Ilon', 'Mask')
lecture_1.courses_attached += ['C+']
lecture_2 = Lecturer('James', 'Gosling')
lecture_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 3)

reviewer_1.rate_hw(student_3, 'C+', 10)
reviewer_1.rate_hw(student_3, 'C+', 8)

student_1.rate_lec(lecture_1, 'C+', 10)
student_1.rate_lec(lecture_1, 'C+', 5)
student_1.rate_lec(lecture_1, 'C+', 0)

student_2.rate_lec(lecture_2, 'Python', 2)
student_2.rate_lec(lecture_2, 'Python', 2)
student_2.rate_lec(lecture_2, 'Python', 2)

print(student_1.grades)
print(student_2.grades)
print(lecture_1.grades)
print(lecture_2.grades)
print(student_3.grades)

print(reviewer_1)
print(reviewer_2)
print(lecture_1)
print(student_1)
print(student_2)
print(student_3)

print(student_1 < student_2)
print(student_1 > student_2)

print(lecture_1 < lecture_2)
print(lecture_2 < lecture_1)

print(Student.list_students)


print(student_1.courses_in_progress)

