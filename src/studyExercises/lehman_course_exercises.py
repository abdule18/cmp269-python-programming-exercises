# Exercise 1: The "Lehman Course" Class

class LehmanCourse:

    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits
        self._student_count = 0

    def enroll_student(self):
        self._student_count += 1

    def display_info(self):
        print(f"Course: {self.course_name}")
        print(f"Credits: {self.credits}")
        print(f"Students Enrolled: {self._student_count}")


# Exercise 2: Specialized Inheritance

class LabCourse(LehmanCourse):

    def __init__(self, course_name, credits, lab_fee):
        super().__init__(course_name, credits)
        self.lab_fee = lab_fee

    def display_info(self):
        super().display_info()
        print(f"Lab Fee: ${self.lab_fee}")


# Exercise 3: Duck Typing Demonstration

class Professor:

    def get_role(self):
        return "Teaching and Research"


class Student:

    def get_role(self):
        return "Learning and Coding"


def print_role(person):
    print(person.get_role())


# Main Program

if __name__ == "__main__":

    print("--- Exercise 1 ---")

    course = LehmanCourse("CMP 269", 4)

    course.enroll_student()
    course.enroll_student()

    course.display_info()

    print("\n--- Exercise 2 ---")

    lab_course = LabCourse("CMP 416", 4, 150)

    lab_course.enroll_student()

    lab_course.display_info()

    print("\n--- Exercise 3 ---")

    professor = Professor()
    student = Student()

    print_role(professor)
    print_role(student)