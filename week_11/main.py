from student import get_student
from access import check_access
from display import print_resultab

def main():
    # Get student information
    student_data = get_student()
    
    # Check access
    status, reason = check_access(
        student_data['registered'],
        student_data['lab_open'],
        student_data['computer_available']
    )
    
    # Display the result
    print_result(
        student_data['name'],
        student_data['student_id'],
        status,
        reason
    )

if __name__ == "__main__":
    main()