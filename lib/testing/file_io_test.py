from file_io import write_file, append_to_file, read_file
import pytest

def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file.txt" # Add .txt extension
    file_content = "This is a test content."
    write_file(str(file_name), file_content)
    with open(file_name, 'r') as f:
        content_read = f.read()
    assert content_read == file_content


def test_append_file(tmp_path):
    """Test append_file()"""
    file_name = tmp_path / "test_file.txt" # Add .txt extension
    file_content = "This is a test content."
    append_content = "Appended content." # Remove the newline character from append_content
    write_file(str(file_name), file_content)
    append_to_file(str(file_name), append_content)
    with open(file_name, 'r') as f:
        file_content_read = f.read()
        print("File Content:", repr(file_content_read))
        assert file_content_read == file_content + '\n' + append_content # Adjust the assertion


def test_read_file(tmp_path):
    """Test read_file()"""
    file_name = tmp_path / "test_file.txt" # Add .txt extension
    file_content = "This is a test content."
    write_file(str(file_name), file_content)
    file_content_read = read_file(str(file_name))
    assert file_content_read == file_content