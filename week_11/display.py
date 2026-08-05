def print_result(name, student_id, status, reason):
    """
    Display the access result to the user.
    
    Parameters:
    name (str): Student's name
    student_id (str): Student's ID
    status (str): Access status (Access Granted or Access Denied)
    reason (str): Reason for the access status
    """
    
    print("\n===== ACCESS RESULT =====")
    print(f"Student Name: {name}")
    print(f"Student ID: {student_id}")
    print(f"Status: {status}")
    print(f"Reason: {reason}")