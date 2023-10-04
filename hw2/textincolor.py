class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class file_manager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self):
        self.file.close()


# with file_manager("Text.txt", 'w') as f:
#     f.write("Create a context manager that will paint the color of the displayed text. \n"
#             "https://www.skillsugar.com/how-to-print-coloured-text-in-python")


with open("Text.txt") as f:
    for line in f:
        print('\033[95m' + line + '\033[90m')