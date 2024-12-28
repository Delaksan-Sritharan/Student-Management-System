

students=[]
attendence=[]
attendence_today=[]
'''
Student ID (9-digit number)
- NIC - National Identity Card Number (String, with 10 characters)
- Student’s First Name (String, maximum of 10 characters)
- Student’s Last Name (String, maximum of 15 characters)
- Birth Date
- Permanent Address (String, maximum of 15 characters)
- Telephone Number (String, 10 characters)
- Tutorial Group
- Centre
'''

while True:
    print("IIT Campus".center(50))
    print("Main Menu".center(50))
    print("")
    print("1) Enroll a new student")
    print("2) View details of a student")
    print("3) View details of all the students according to the branch")
    print("4) Update student details")
    print("5) Mark attendance")
    print("6) View attendance")
    print("7) Exit")

    choice = input("choice: ")

    if choice== "1":
        while True:#loop for entering the students details
        
            print("IIT Campus".center(50))
            print("")
            print("Enroll a new student")
            student_id = input("Student ID (9-digit number): ")
            while not (len(student_id) == 9 and student_id.isdigit()):
                print("Invalid Student ID. Please enter a 9-digit number.")
                student_id = input("Student ID (9-digit number): ")
            nic = input("NIC (10 characters): ")
            while not (len(nic) == 10 and nic.isdigit()):
                print("Invalid NIC. Please enter a 10 character NIC")
                nic = input("NIC (10 characters): ")
            first_name = input("First Name (max 10 characters): ").capitalize()
            while not (0 < len(first_name) <= 10 and first_name.isalpha()):
                print("Oops! Max 10 characters for First Name. Please try again.")
                first_name = input("First Name (max 10 characters): ").capitalize()
            last_name = input("Last Name (max 15 characters): ").capitalize()
            while not (0 < len(last_name) <= 15 and last_name.isalpha()):
                print("Oops! Max 15 characters for Last Name. Please try again.")
                last_name = input("Last Name (max 15 characters): ").capitalize()                    
            birth_date = input("Birth date: ")
            permanent_address = input("Permanent Address (max 15 characters): ")
            while not (0 < len(permanent_address) <= 15):
                print("Invalid Address. Please enter a maximum of 15 characters.")
                permanent_address = input("Permanent Address (max 15 characters): ")
            phone_number = input("Phone Number (10 digits): ")
            while True:
                if len(phone_number) != 10 or not phone_number.isdigit():
                    print("Invalid phone number. Please enter a 10-digit number.")
                    phone_number = input("Phone Number (10 digits): ")
                else:
                    break  # Exit loop if all validations pass

                    
            phone_number = str(input("Phone number: "))
            tutorial_group = input("Tutorial Group: ")
            centre = input("Centre: ")
            
            save_choice = input("Do you want to save the details[yes/No]?")

            if save_choice == "Yes":
                student=[student_id,nic,first_name,last_name,birth_date,permanent_address,phone_number,tutorial_group,centre]
                students.append(student)
                print("Student added succesfully.")
                break #exit inner loop to go back to main meny

            elif save_choice == "No":
                students.pop()
                print("Student details deleted successfully.")
                continue # continue to the begining on the inner loop

    elif choice == "2":
        print("IIT Campus".center(50))
        print("View details of a student".center(50))
        print("")
        student_id = int(input("Enter student id: "))
        if not student_id:
            print("Please enter a bank account number.")
            continue
        
        found = False #flag to check if it is found.
        for student in students:
            if student[0] == student_id: #comparing the integer
                print(f"NIC - {student[1]}")
                print(f"Phone Number - {student[6]}")
                print(f"First Name - {student[2]}")
                print(f"Last Name - {student[3]}")
                print(f"Tutorial Group - {student[7]}")
                print(f"centre - {student[8]}")
                found = True #set found flag to True
                break
            if not found:
                print("Student Id not found.")

            another_view = input("Do you want to view another student's details(Yes/No)")

            if another_view == "Yes":
                continue
            elif another_view == "No":
                break
            else:
                print("Invalid choice. Please enter again.")


    elif choice == "3":
        print("IIT Campus".center(50))
        print("View details of all the students".center(50))
        print("")
        print("Branch Name:")
        print("Nic\t\tStudent ID\t\tFirst Name\t\tLast Name\t\tTutorial Group")
        for student in students:
                        first_name_indent = 10-len(student[2])
                        last_name_indent = 15-len(student[3])
                        print(f"{student[1]} \t{student[0]}\t{student[2]}"+" "*first_name_indent+f"\t{student[3]}"+" "*last_name_indent+f"\t{student[7]}")

        update_choice = input("Do you want to update the student details")

        if update_choice == "Yes": # Set choice to 4 to trigger the update section
            choice = 4
            continue# Continue back to the main menu to process the new choice
        elif update_choice == "No":
            continue# Continue back to the main menu
        else:
            print("Invalid choice. Please re enter")
            continue# Continue back to the main menu
        
    elif choice == "4":
        print("IIT Campus".center(50))
        print("Update Student Details".center(50))
        print("")
        student_id = int(input("Student ID: "))  # Convert input to integer
        found = False
        for student in students:
            if student[0] == student_id:  # Compare with integer
                found = True
                print(f"NIC - {student[1]}")
                print(f"First Name - {student[2]}")
                print(f"Last Name - {student[3]}")
                print(f"Birth Date - {student[4]}")
                print(f"Permanent Address - {student[5]}")
                print(f"Phone Number - {student[6]}")

                # Get new values from the user
                nic = str(input("New NIC (leave blank to keep current): ") or student[1])
                first_name = str(input("New First Name (leave blank to keep current): ") or student[2])
                last_name = str(input("New Last Name (leave blank to keep current): ") or student[3])
                birth_date = input("New Birth Date (leave blank to keep current): ") or student[4]
                permanent_address = str(input("New Permanent Address (leave blank to keep current): ") or student[5])
                phone_number = str(input("New Phone Number (leave blank to keep current): ") or student[6])
                tutorial_group = input("New Tutorial Group (leave blank to keep current): ") or student[7]
                centre = input("New Centre (leave blank to keep current): ") or student[8]

                # Update the student details
                student[1] = nic
                student[2] = first_name
                student[3] = last_name
                student[4] = birth_date
                student[5] = permanent_address
                student[6] = phone_number
                student[7] = tutorial_group
                student[8] = centre

                print("Student details updated successfully.")
                break  # Exit the loop after updating

        if not found:
            print("Account not found. Please re-enter the account number.")

    elif choice == "5":
        print("IIT Campus".center(50))
        print("Mark Attendance".center(50))
        print("")
        centre = input("Centre - ")
        tutorial_group = input("Tutorial Group - ")
        date = input("Date - ")
        print("Student ID\tPresent/ Absent")
        for student in students:
            if student[7] == tutorial_group and student[8] == centre:
                student_id = student[0]
                attendence_status = input(f"{student_id}: (Present/Absent): ")
                attendence_today.append((student_id,attendence_status))
        print("\nAttendence Records: ")
        print("Student ID\tStatus")
        for record in attendence_today:
            print(f"{record[0]}\t\t{record[1]}")

        save_choice = input("Do you want to save the attendence details(Yes/No): ")

        if save_choice == "Yes":
            attendence.append({
                "date":date,
                "centre":centre,
                "tutorial_group":tutorial_group,
                "attendence":attendence_today
                })
            print("Attendence details saved succesfully.")
        else:
            print("attendence details not saved.")
            if attendence_today:
                attendece_today.pop()

    elif choice == "8":
        print("IIT Campus".center(50))
        print("View Attendance".center(50))
        student_id = int(input("Student ID - "))
        from_date = input("From (YYYY_MM_DD) - ")
        to_date = input("To (YYYY-MM-DD) - ")
        print("\nDate\t\tPresent / Absent")
        found_attendence = False

        for record in attendence:
            if record["date"]>=from_date and record["date"]<=to_date:
                for attendence_record in record["attendence"]:
                    if attendence_record[0] == student_id:
                        print(f"{record["date"]}\t{attendence_record[1]}")
                        found_attendence = True

        if not found_attendence:
            print("No attendence record for this student in this specified date range.")
        
        return_to_menu = input("Do you want to return to this mian menu (Yes/No)? ")
        if return_to_menu == "Yes":
            continue
        else:
            break
    

    elif choice == '7':
        print("Exiting the program.")
        break  # Exit the main loop
            


            

            


           
