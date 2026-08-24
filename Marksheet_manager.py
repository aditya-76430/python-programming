# Some Example that how the student data will handel by python.
students = {}

# How the data will store in python Dict.
students["01"] = {
    "name": "aditya",
    "marks": {
        "English": 85,
        "Hindi": 95,
        "Maths": 56,
        "Science": 78
    }
}

students["02"] = {
    "name": "Rohan",
    "marks": {
        "English": 78,
        "Hindi": 89,
        "Maths": 82,
        "Science": 12
    }
}
    
# creating a add_student dunction where user can add the student data

def add_student():
    Student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    
    # marks of the student
    
    english_marks = int(input("Enter Eng marks: "))
    hindi_marks = int(input("Enter Hindi marks: "))
    maths_marks = int(input("Enter Maths marks: "))
    science_marks = int(input("Enter Science marks:"))
    
    # Now we will store this data into the students dictionary
    
    students[Student_id] = {
        "name": student_name,
        "marks":{
            "English":english_marks,
            "Hindi":hindi_marks,
            "Maths":maths_marks,
            "Science":science_marks
        }
    }
    
# Now we will search student with student ID
    
def search_student():
    student_id = input("Enter Student ID: ")
    
 # Now ID will get searched and display
 
    if student_id in students:
        print(students[student_id])
    else:
        print("Student record not found !")

#search_student()

# Now we will delete the student id from students_id
def delete_student():
    delete_students = input("Enter Student ID_Del: ")
    
    # we will check the student in dict and if found it will delete
    
    if delete_students in students:
        students.pop(delete_students)
        print("Student deleted sucessfully!")
    else:
        print("Student not found!")       

# to claculate the total marks of the students

def calculate_total_marks():
    Students_id = input("Enter student ID: ")
    
    # we will link the id to calculate the total marks
    
    if Students_id in students:
        total = sum(students[Students_id]["marks"].values())
        print("Toatal Marks of the Studen is: ", total)
    else:
        print("In valid Id or student not found in record!") 
# to calculate the total percentage of the marks
        
def calculate_percentage():
    Students_id = input("Enter student ID: ")
    
    # we will link the id to calculate the total marks
    
    if Students_id in students:
        total = sum(students[Students_id]["marks"].values())
        percentage = (total / 400)*100
        print("Toatal percentage of the Student is: ", percentage)
    else:
        print("In valid Id or student not found in record!")     
     
def menu():
    print("\n======== STUDENT MANAGEMENT SYSTEM ========")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Calculate Total Marks")
    print("5. Calculate Percentage")
    print("6. Calculate Total Percentage")
    
    

while True:
    
    menu()
    
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        print("You have choice: ", choice)
        add_student()
        
    elif choice == 2:
        print("You have Choice: ", choice)
        search_student()
    
    elif choice == 3:
        print("You have Choice: ", choice)
        delete_student()
        
    elif choice == 4:
        print("You have choice: ", choice)
        calculate_total_marks()
        
    elif choice == 5:
        print("You have choice: ", choice)
        calculate_percentage()
    
    else:
        print("Your Have Enter Invalid Choice!")
    