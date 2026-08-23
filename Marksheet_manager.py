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

# Options / student_menu .

def menu():
    print("\n======== STUDENT MANAGEMENT SYSTEM ========")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View Student")
    print("4. Update Student")
    print("5. Calculate Toatal Marks")
    print("6. Calculate Total Percentage")
    print("7. Calcualte Grade")
    print("8. Result (pass/Fall)")
    print("9. Load Data")
    print("10. Save Data")
    
    
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

#delete_student()
#print(students)

