def get_student():
    print("====== Computer Lab Access ======")
    
    # Get student name
    name = input("Student Name: ")
    
    # Get student ID
    student_id = input("Student ID: ")
    
    # Get registration status
    registered = input("Registered for today's lab? (Y/N): ").upper()
    while registered not in ['Y', 'N']:
        print("Invalid input! Please enter Y or N.")
        registered = input("Registered for today's lab? (Y/N): ").upper()
    
    # Get lab open status
    lab_open = input("Is the lab open? (Y/N): ").upper()
    while lab_open not in ['Y', 'N']:
        print("Invalid input! Please enter Y or N.")
        lab_open = input("Is the lab open? (Y/N): ").upper()
    
    # Get computer availability
    computer_available = input("Computer Available? (Y/N): ").upper()
    while computer_available not in ['Y', 'N']:
        print("Invalid input! Please enter Y or N.")
        computer_available = input("Computer Available? (Y/N): ").upper()
    
    # Return all collected data
    return {
        'name': name,
        'student_id': student_id,
        'registered': registered,
        'lab_open': lab_open,
        'computer_available': computer_available
    }