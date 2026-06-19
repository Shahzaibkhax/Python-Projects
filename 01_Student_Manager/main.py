students = []
running = True

while running == True :
    print("===== STUDENT MANAGER =====")
    print("1. Add Student ")
    print("2. Show Students ")
    print("3. Search Student ")
    print("4. Delete Student ")
    print("5. Exit ")
    print("===================================")

    choice = input("Enter Your Choice (1-5):")

    if choice == "1":
        new_student = input ("Enter the name of the student to add :")
        students.append(new_student)
        print(f"{new_student} has been added sucessfully!")
        
    elif choice == "2":
        print("\n--- current student list ---")
        if len(students) == 0:
            print("The list is currently empty. Add some students first!")
        else:
            for index, student in enumerate(students, start=1):
                print(f"{index}. {student}")

    elif choice == "3":
        print("\n--- Search Student ---")
        if len(students) == 0:
            print("The list is empty. Nothing to search!")
        else:
            search_name = input("Enter the name of the student to search for: ")
            
            if search_name in students:
                print(f" Found! {search_name} is in the student list.")
            else:
                print(f" Sorry, {search_name} was not found in the list.")
        
    elif choice == "4":
        print("\n--- Delete Student ---")
        if len(students) == 0:
            print("The list is empty. Nothing to delete!")
        else:
            delete_name = input("Enter the name of the student to remove: ")
            
            if delete_name in students:
                students.remove(delete_name) 
                print(f"{delete_name} has been removed successfully.")
            else:
                print(f"Sorry, {delete_name} was not found in the list.")
        
    elif choice == "5":
        print("Goodbye! Thanks for using Student Manager.")
        running = False
        
    else:
        print("\n❌ Invalid choice! Please type a number from 1 to 5.")
