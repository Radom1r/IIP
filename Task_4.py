class Student:
    def __init__(self, name, surname, gender, marks={}):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.marks = marks

    def find_average_for_all_students(self):
        for course in self.marks.keys():
            average = sum(self.marks[course])/len(self.marks[course])
            print({course:average})
        
    def give_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            if course in lecturer.marks:
                lecturer.marks[course] += [grade]
            else:
                lecturer.marks[course] = [grade] 
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname} \nAverage grade for hometasks: {sum([item for sublist in self.grades.values() for item in sublist])/len([item for sublist in self.grades.values() for item in sublist])} \nCourses in progress: {", ".join(self.courses_in_progress)} \nFinished_courses: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return sum([item for sublist in self.grades.values() for item in sublist])/len([item for sublist in self.grades.values() for item in sublist]) < sum([item for sublist in other.grades.values() for item in sublist])/len([item for sublist in other.grades.values() for item in sublist])

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            if course in student.marks:
                student.marks[course] += [grade]
            else:
                student.marks[course] = [grade] 
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname, marks={}):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.marks = marks

    def find_average_for_all_lecturers(self):
        for course in self.marks.keys():
            av = sum(self.marks[course])/len(self.marks[course])
            print({course:av})

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname} \nAverage grade for lectures: {sum([item for sublist in self.grades.values() for item in sublist])/len([item for sublist in self.grades.values() for item in sublist])}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Student!')
            return
        return sum([item for sublist in self.grades.values() for item in sublist])/len([item for sublist in self.grades.values() for item in sublist]) < sum([item for sublist in other.grades.values() for item in sublist])/len([item for sublist in other.grades.values() for item in sublist])

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def give_mark(self, student, course, grade):
        self._Mentor__rate_hw(student, course, grade)

    def __str__(self):
        return f'Name: {self.name} \nSurname: {self.surname}'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'java']

new_student = Student('Ruoy', 'Eman', 'your_gender')
new_student.courses_in_progress += ['Python', 'java']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

new_reviewer = Reviewer('Some', 'Buddy')
new_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'java']

new_lecturer = Lecturer('Some', 'Buddy')
new_lecturer.courses_attached += ['Python', 'java']

best_student.give_rate(cool_lecturer, 'Python', 10)
best_student.give_rate(new_lecturer, 'java', 7)
best_student.give_rate(cool_lecturer, 'Python', 3)
best_student.give_rate(new_lecturer, 'Python', 5)
cool_reviewer.give_mark(best_student, 'Python', 10)
cool_reviewer.give_mark(new_student, 'java', 6)
best_student.give_rate(new_lecturer, 'java', 7)
best_student.give_rate(cool_lecturer, 'Python', 10)
cool_reviewer.give_mark(best_student, 'Python', 10)
cool_reviewer.give_mark(new_student, 'Python', 10)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(best_student < new_student)
print(new_lecturer < cool_lecturer)
print(cool_lecturer.find_average_for_all_lecturers()) 
print(best_student.find_average_for_all_students())