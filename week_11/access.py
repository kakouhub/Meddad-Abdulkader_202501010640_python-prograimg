def check_access(registered, lab_open, computer_available):
    """
    Check if a student should be granted access to the computer lab.
    
    Parameters:
    registered (str): 'Y' if student is registered, 'N' otherwise
    lab_open (str): 'Y' if lab is open, 'N' otherwise
    computer_available (str): 'Y' if computers are available, 'N' otherwise
    
    Returns:
    tuple: (status, reason) where status is 'Access Granted' or 'Access Denied'
           and reason is the explanation
    """
    
    # Convert to boolean for easier checking
    is_registered = registered == 'Y'
    is_lab_open = lab_open == 'Y'
    is_computer_available = computer_available == 'Y'
    
    # Check all conditions using logical AND operator
    if is_registered and is_lab_open and is_computer_available:
        return "Access Granted", "Welcome to the lab."
    else:
        # Determine the reason for denial
        if not is_registered:
            return "Access Denied", "Student not registered for today's lab."
        elif not is_lab_open:
            return "Access Denied", "Computer lab is closed."
        elif not is_computer_available:
            return "Access Denied", "No available computer."
        else:
            return "Access Denied", "Access denied due to unknown reason."