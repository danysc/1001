class Class:

    def __init__(self, subject, student_amount, lesson_amount):
        self.subject = subject
        self.amount = student_amount
        self.lesson = lesson_amount
        self.progress = 0

    def subject(self):
        self.subject = raw_input("What is the subject? \n")

    def teacher(self):
        self.teacherN = raw_input("What is the teacher's name?")
        self.teacherA = input("What is the teacher's age?")

    def new_Student(self):
        print("Adding a student to your class...")
        self.amount = self.amount + 1

        print("You now have " + str(self.amount) + " students.")

    def lessonProgress(self):
        self.progress = self.progress + 1

    def course_progress(self):
        print(str(self.progress) + " out of " + str(self.lesson) + " lessons.")
