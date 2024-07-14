

class Person():
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        print(self.get_class_name(), end=" - ")
        print(f"Name: {self.name}", end=" - ")
        print(f"YoB: {self.yob}", end=" - ")

    def get_class_name(self):
        return self.__class__.__name__


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        super().describe()
        print(f"Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        super().describe()
        print(f"Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        super().describe()
        print(f"Specialist: {self.specialist}")


class Ward():
    def __init__(self, name):
        self.name = name
        self.resident = []

    def add_person(self, person):
        self.resident.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.resident:
            person.describe()

    def count_doctor(self):
        num_doctor = 0
        for person in self.resident:
            if person.get_class_name() == "Doctor":
                num_doctor += 1
        return num_doctor

    def sort_age(self):
        self.resident.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        sum_yob = 0
        num_teacher = 0
        for person in self.resident:
            if person.get_class_name() == "Teacher":
                sum_yob += person.yob
                num_teacher += 1
        return sum_yob/num_teacher


# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

# 2(b)
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print(f"\nNumber of docters: {ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
