

def calc_gpa(scores):
    # Calculate average
    total = 0
    for s in scores:
        total=total+s
    avg = total/len(scores)
    return avg

def letter_grade(gpa):
    if gpa >= 90: grade = 'A'
    elif gpa >= 80: grade='B'
    elif gpa >= 70:grade = 'C'
    elif gpa>=60:grade='D'
    else:grade='F'
    return grade

class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores = scores
    
    def get_gpa(self):
        return calc_gpa(self.scores)
    
    def display_info(self):
        gpa = self.get_gpa()
        grade = letter_grade(gpa)
        print("Name: " + self.name)
        print("GPA: " + str(round(gpa, 2)))
        print("Grade: " + grade)

# Main program
students = []
students.append(Student("Alice", [85, 90, 88, 92]))
students.append(Student("Bob", [75, 78, 80, 76]))
students.append(Student("Charlie", [95, 98, 96, 99]))

for s in students:
    s.display_info()
    print("---")
