# Functions with outputs

def format_name(f_name, l_name):
    # information
    """
    Takes a first and a last name and formats it into title text
    """
    if f_name == "" or l_name == "":
        return "You didn't provide any input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # The return keywords specifies the end of a function and it returns the values
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your name? "), input("What is your last name? ")))