#Program that manages students in class

class Student:
    def __init__(self,name,age,marks):
        self.name =name
        self.age=age 
        self.marks=marks
    def get_marks(self):
        return self.marks
class Classroom:
    def __init__(self,class_name,max_students):
        self.class_name=class_name
        self.max_students=max_students
        self.students=[]
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(student.name+ "added: True ")
            return True
        print(student.name + "added :False")
        return False
    def get_average_marks(self):
        value=0
        for student in self.students:
           value +=student.get_marks()
        return value/len(self.students)
    def get_student_count(self):
        return len(self.students)
#creating student object
s1=Student("Alice",20,85)
s2=Student("James",21,70)
s3=Student("Mary",19,90)

#creating classroom object
classroom= Classroom("Computer science",2)

#adding student
classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

#Displaying results
print("Total students:",classroom.get_student_count())
print("Average marks:", classroom.get_average_marks())
