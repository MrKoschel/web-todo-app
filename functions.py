import time
FILEPATH = "todos.txt"


def open_todos_file(filepath=FILEPATH):
    """ Returns text from file as a list"""
    with open(filepath) as file:  # 'r' is default value in this function
        local_todos = file.readlines()
    return local_todos


def override_todos_file(todos_arg, filepath=FILEPATH):
    """Override text file with new to-do list"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def show_current_date():
    """Shows current date"""
    day = int(time.strftime("%#d"))

    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    date = time.strftime(f"{day}{suffix} of %B %Y %H:%M:%S, %A")
    return f"Today is {date}"
