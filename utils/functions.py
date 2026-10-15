import string

def get_valid_number(prompt: str, expected_type: type = int, minimum_value: float | None = None):
    """
    Prompts the user for numerical input, validating its type and an optional minimum value.

    This function continuously asks the user for input until a valid number matching 
    the 'expected_type' is provided. It handles ValueError exceptions to prevent 
    application crashes caused by invalid string inputs (e.g., typing letters instead of numbers).

    Args:
        prompt (str): The message displayed to the user requesting input.
        expected_type (type, optional): The expected numeric data type. 
            Typically 'int' or 'float'. Defaults to 'int'.
        minimum_value (float | None, optional): The minimum acceptable value. 
            If provided, the input must be greater than or equal to this threshold. 
            Defaults to None (no minimum limit).

    Returns:
        int | float: The validated numerical input, converted to the 'expected_type'.

    Example:
        # Get a strictly positive integer (e.g., array index or quantity)
        datasets = get_safe_number("How many datasets? ", expected_type=int, minimum_value=1)
        
        # Get a decimal number with no minimum limit (e.g., temperature)
        temp = get_safe_number("Enter the temperature: ", expected_type=float)
    """
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue
            
        try:
            # Dynamically attempts to cast the string to the expected_type (int or float)
            number = expected_type(user_input)
            
            # Applies the minimum value check only if a threshold was explicitly provided
            if minimum_value is not None and number < minimum_value:
                print(f"Error: Please enter a number greater than or equal to {minimum_value}.")
                continue
                
            return number
            
        except ValueError:
            # expected_type.__name__ automatically prints 'int' or 'float' based on the parameter
            print(f"Error: Invalid input. You must enter a valid {expected_type.__name__}.")

def get_valid_name(prompt: str) -> str:
    
    """
    Prompts the user for a valid string (like a name), ensuring it meets strict formatting rules.

    This function continuously asks for input until the user provides a string that 
    is not empty, does not start with special characters or whitespaces, and 
    does not contain any numeric digits. The valid input is then formatted with 
    title casing (e.g., "john" becomes "John").

    Args:
        prompt (str): The message displayed to the user requesting input.

    Returns:
        str: The validated, title-cased string.

    Example:
        # Get a valid dataset name from the user
        dataset_name = get_valid_name("Enter the dataset name: ")
    """
    # Combines whitespaces and punctuation to check the first character
    unwanted_starting_chars = string.whitespace + "-." + string.punctuation
    
    while True:
        user_input = input(prompt).strip().title()
        
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue
            
        if user_input[0] in unwanted_starting_chars:
            print("Error: The name cannot start with spaces or special characters.")
            continue
            
        if any(char.isdigit() for char in user_input):
            print("Error: The name must not contain any numbers.")
            continue
            
        return user_input


def task_names(prompt: str) -> str:
    """
    Prompts the user for a valid task name, ensuring it meets specific formatting rules.

    This function continuously asks for input until the user provides a string that 
    is not empty, does not start with special characters or whitespaces, and 
    does not contain any numeric digits. The valid input is then formatted with 
    title casing (e.g., "john" becomes "John"). In addition, the task name must be longer than 3 characters.

    Args:
        prompt (str): The message displayed to the user requesting input.

    Returns:
        str: The validated, title-cased string.

    Example:
        # Get a valid task name from the user
        task_name = task_names("Enter the task name: ")
    """
    while True:      
        user_input=get_valid_name(prompt)
        if len(user_input)<3:
            print("Error: The task name must be longer than 3 characters. Please try again.")
        else:
            return user_input




def get_choice(prompt:str, valid_choices: list) -> str:
    """
    Prompts the user for a valid choice from a list of options.

    Args:
        prompt (str): The message displayed to the user requesting input.
        valid_choices (list): A list of strings representing the valid choices.

    Returns:
        str: The validated choice.

    Example:
        # Get a valid choice from the user
        choice = get_choice("Enter your choice (A, B, or C): ", ["A", "B", "C"])
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_choices:
            return user_input
        else:
            print(f"Error: Invalid choice. Please enter one of the following: {', '.join(valid_choices)}")