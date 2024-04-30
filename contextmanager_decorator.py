from contextlib import contextmanager

@contextmanager
def file_manager(file_name, mod):
    f = open(file_name, mod)
    yield f
    f.close()


with file_manager("exemplu.log", "w") as f:
    f.write("log something")