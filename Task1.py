import csv


class Style:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Value {value} must be type of str")
        if not value.replace(' ', '').isalpha() or not value.istitle():
            raise ValueError(f'Value {value} must contain only letters and begin with capital one')


class Student:
    fullname = Style()
    subjects = dict()

    def __init__(self, fullname, subjects_file):
        self.fullname = fullname
        self.subjects_file = subjects_file
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        subjects = {}
        with open(subjects_file, 'r', newline='') as fr:
            csv_file = csv.reader(fr)
            for line in csv_file:
                for subject in line:
                    subjects[subject] = {'grades': [], 'test_scores': []}
        return subjects

    def add_grade(self, subject, grade):
        if subject in self.subjects.keys():
            if 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)
            else:
                print(f'Grade must be between 2 and 5 inclusively')
        else:
            print(f'Subject {subject} not found')

    def add_test_score(self, subject, test_score):
        if subject in self.subjects.keys():
            if 0 <= test_score <= 100:
                self.subjects[subject]['test_scores'].append(test_score)
            else:
                print(f'Test score must be between 0 and 100 inclusively')
        else:
            print(f'Subject {subject} not found')

    def get_average_test_score(self, subject):
        avg = sum(self.subjects[subject]['test_scores']) / len(self.subjects[subject]['test_scores'])
        return avg

    def get_average_grade(self):
        sum_grade = 0
        count_grade = 0
        for value in self.subjects.values():
            sum_grade += sum(value['grades'])
            count_grade += len(value['grades'])
        return sum_grade / count_grade

    def __str__(self):
        return f'Student: {self.fullname}\nSubjects: {self.get_subjects()}'

    def get_subjects(self):
        res = ''
        for subject in self.subjects.keys():
            if self.subjects[subject]['grades'] and self.subjects[subject]['test_scores']:
                res += subject + ' '
        return res


if __name__ == '__main__':
    s1 = Student('Harry Potter', 'subjects.csv')
    s1.add_grade("Math", 4)
    s1.add_test_score("Math", 85)
    s1.add_grade("History", 5)
    s1.add_test_score("History", 92)
    average_grade = s1.get_average_grade()
    print(f"Average grade at math: {average_grade}")
    average_test_score = s1.get_average_test_score("Math")
    print(f"Average test score: {average_test_score}")
    print(s1)
