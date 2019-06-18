import os


class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


if __name__ == "__main__":
    if os.stat("example.txt").st_size == 0:
        for _ in range(1):
            with File('example.txt', 'w') as infile:
                infile.write('example')
    else:
        with File('example.txt', 'w') as infile:
            infile.write('Error')
