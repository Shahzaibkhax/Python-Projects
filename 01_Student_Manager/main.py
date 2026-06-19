students = []
running = True

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"




while running == True :
    print(f"{YELLOW}===== STUDENT MANAGER ====={RESET}")
    print("1. Add Student ")
    print("2. Show Students ")
    print("3. Search Student ")
    print("4. Delete Student ")
    print("5. Exit ")
    print(f"{YELLOW}==========================={RESET}")
   

    choice = input(f"{CYAN}Enter Your Choice (1-5): {RESET}")

    if choice == "1":
        new_student = input ("Enter the name of the student to add :")
        students.append(new_student)
        print(f"{GREEN} {new_student} has been added successfully!{RESET}")
        
    elif choice == "2":
        print(f"\n{YELLOW}--- Current Student List ---{RESET}")
        if len(students) == 0:
            print(f"{RED}The list is currently empty. Add some students first!{RESET}")
        else:
            for index, student in enumerate(students, start=1):
                print(f"{index}. {student}")

    elif choice == "3":
        print(f"\n{YELLOW}--- Search Student ---{RESET}")
        if len(students) == 0:
            print(f"{RED}The list is empty. Nothing to search!{RESET}")
        else:
            search_name = input("Enter the name of the student to search for: ")
            
            if search_name in students:
                print(f"{GREEN} Found! {search_name} is in the student list.{RESET}")
            else:
                print(f"{RED} Sorry, {search_name} was not found in the list.{RESET}")
        
    elif choice == "4":
        print(f"\n{YELLOW}--- Delete Student ---{RESET}")
        if len(students) == 0:
            print(f"{RED}The list is empty. Nothing to delete!{RESET}")
        else:
            delete_name = input("Enter the name of the student to remove: ")
            
            if delete_name in students:
                students.remove(delete_name) 
                print(f"{RED} {delete_name} has been removed successfully.{RESET}")
            else:
                print(f"{RED} Sorry, {delete_name} was not found in the list.{RESET}")
        
    elif choice == "5":
        print(f"{GREEN}Goodbye! Thanks for using Student Manager.{RESET}")
        running = False
        
    else:
        print(f"\n{RED} Invalid choice! Please type a number from 1 to 5.{RESET}")
