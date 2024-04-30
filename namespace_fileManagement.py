class FileManager:
    # def __init__, __enter__, __exit__
    def __init__(self, file_name, mod):
        self.file_name = file_name
        self.file = None
        self.mod = mod

    def __enter__(self):
        self.file = open(self.file_name, self.mod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
