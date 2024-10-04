class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __setattr__(self, name, value):
        if name == 'name':
            if not (value and value.istitle() and value.isalpha()):
                raise ValueError('Name must begin with capital letter and contain only letters')
        elif name == 'age':
            if not isinstance(value, int) or not 0 <= value <= 120:
                raise ValueError('Age has to be an integer and be between 0 and 120')
        elif name == 'email':
            if '@' not in value:
                raise ValueError("An email has to contain '@' symbol")
        super().__setattr__(name, value)

    def __str__(self):
        return f'Person (name={self.name}, age={self.age}, email={self.email})'


if __name__ == '__main__':
    p1 = Person('Ron', 12, 'ron.uesley@gmail.com')
    print(p1)
