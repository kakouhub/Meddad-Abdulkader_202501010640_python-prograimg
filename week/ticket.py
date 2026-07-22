def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    student_name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")

    print("\nPriority Levels")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Choose priority (1-3): ")

    if choice == "1":
        priority = "High"
        technician = "Ahmad"
    elif choice == "2":
        priority = "Medium"
        technician = "Siti"
    else:
        priority = "Low"
        technician = "Ali"

    return (
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician
    )