import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(decorate_function):
    def wrapper_function():
        start_time = time.time()
        decorate_function()
        difference = time.time() - start_time
        print(f"{decorate_function.__name__} run speed: {difference}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i *= i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i *= i


fast_function()
slow_function()
