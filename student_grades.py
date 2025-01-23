students = []

def add_or_update_student(name, subject, grade):
    for student in students:
        if student['name'] == name:
            student['grades'][subject] = grade
            print(f"Updated {name}'s grade for {subject} to {grade}.")
            return
    
    new_student = {'name': name, 'grades': {subject: grade}}
    students.append(new_student)
    print(f"Added new student {name} with grade {grade} for {subject}.")

def print_report():
    if not students:
        print("No students to report.")
        return
    
    print("Student Report:")
    print("---------------")
    for student in students:
        print(f"Name: {student['name']}")
        for subject, grade in student['grades'].items():
            print(f"  Subject: {subject}, Grade: {grade}")
    print("---------------")

def main():
    while True:
        print("\nMenu:")
        print("1. Add or Update Student Grade")
        print("2. Print Report")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            add_or_update_student(name, subject, grade)
        elif choice == '2':
            print_report()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
