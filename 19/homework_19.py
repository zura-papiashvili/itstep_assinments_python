# შექმენით კლასი Student რომელიც მიიღებს სამ მნიშვნელობას სახელს ასაკს და 
# ლისტში ჩაწერილ ქულებს. კლასს ექნება სამი მეთოდი, პირველი მეთოდი იქნება ჯსონის წაკითხვა,
# მეორე მეთოდი იქნება ქულის საშუალო არითმეტიკულის დაანაგრიშება და მესამე იქნება ჯსონ
# ფაილში ამ ინფორმაციის ჩაწერა.


import json
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def read_json(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        students = []
        for student_data in data['students']:
            student = Student(
                student_data['name'],
                student_data['age'],
                student_data['grades']
            )
            students.append(student)
        return students

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def write_averages_to_json(students, output_file_path):
        averages = {student.name: round(student.average_grade(), 2) for student in students}
        with open(output_file_path, 'w') as file:
            json.dump(averages, file, indent=4)

# Example usage:
students = Student.read_json('students.json')
Student.write_averages_to_json(students, 'students_averages.json')


