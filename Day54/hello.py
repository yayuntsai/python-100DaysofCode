from flask import Flask
import time
app = Flask(__name__)

# @app.route('/')
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(3):
        print(i * i)

@speed_calc_decorator
def slow_function():
    for i in range(5):
        print(i * i)



fast_function()
# if __name__ == "__main__":
#     app.fast_function()