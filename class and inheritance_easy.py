class User():
    def  __init__(self, username):
        self.username = username

    def get_role(self):
        return 'User'

    def __str__(self):
        return f'Username:{self.username}, Role:{self.get_role()}' # for using print() method

class Student(User):
    def __init__(self, username, student_id):
        super().__init__(username) # inherit the father class arguments etc.
        self.student_id = student_id
    
    def get_role(self):
        return 'Student'

    def submit_exam(self, exam_name):
        print(f'{self.username} has submitted the exam: {exam_name}')

student1 = Student('Alice', 'S12345')
print(student1)
student1.submit_exam('Python Basics')
