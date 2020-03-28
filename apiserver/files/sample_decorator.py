from functools import wraps

def test_decorator(f):
    @wraps(f) #꼭 적용해야만 하는 것은 아니지만 부차적 이슈 해결해준다. TODO: tutorial 참고
    def decorated_function(*args, **kwargs):
        print("Decorated function")
        return f(*args, **kwargs)
    return decorated_function

@test_decorator
def func():
    print("Calling func function")

func()
