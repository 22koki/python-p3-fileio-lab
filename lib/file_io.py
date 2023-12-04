# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes content to a text file.

    Args:
        file_name (str): The name of the file (including path if needed).
        file_content (str): The content to be written to the file.
    """
    with open(str(file_name), "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    """
    Appends content to a text file.

    Args:
        file_name (str): The name of the file (including path if needed).
        append_content (str): The content to be appended to the file.
    """
    with open(str(file_name), "a") as file:
        file.write("\n" + append_content)  # Add a newline character before appending the content

def read_file(file_name):
    """
    Reads content from a text file.

    Args:
        file_name (str): The name of the file (including path if needed).

    Returns:
        str: The content read from the file.
    """
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, "r") as file:
        return file.read()
