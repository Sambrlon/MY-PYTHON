class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Runner(Person):
    def run(self):
        print(f"Привет, я {self.firstname} {self.lastname}, и я ранер")


student = Runner("Артем", "Лобазов")
student.print_name()
student.run()