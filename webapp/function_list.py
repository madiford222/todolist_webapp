FILEPATH = "webapp/todos.txt"


def get_todos(filepath = FILEPATH):
    """Reads a text file and return the list of to do items"""
    with open(filepath, "r") as file:
        to_dos_local = file.readlines()
    return to_dos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Writes the list of to do items into the text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())