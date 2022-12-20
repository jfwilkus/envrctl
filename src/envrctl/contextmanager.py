from contextlib import contextmanager


@contextmanager
def write_file(file_path):
    """Safely open and write to a file"""
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()
