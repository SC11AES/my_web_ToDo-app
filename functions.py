FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read file and return list line by line"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """writes list line by line to text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    """name = main - running file directly
       name = filename - running file from import"""
    print("hello")