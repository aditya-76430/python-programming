# Some Example that how the student data will handel by python.

students = {
    "01":{
        "name":"aditya",
        "marks":{
            "English":85,
            "Hindi":95,
            "Maths":56,
            "Science":78
        }
    },
    
    "02":{
        "name":"Rohan",
        "marks":{
            "English":45,
            "Hindi":45,
            "Maths":85,
            "Science":78
        }
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

