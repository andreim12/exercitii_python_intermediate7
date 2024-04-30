from datetime import datetime

def enable_at_hours(from_=5, to_=21):
    def dec(func):
        def wrapper(*args, **kwargs):
            if from_ <= datetime.now().hour < to_:
                func(*args, **kwargs)
        return wrapper  # pointer/obiect in memorie -> care face referinta la rezultatul functiei
    return dec


@enable_at_hours(15, 20)
def say_something(message):
    print(message)

say_something("Ceva")
