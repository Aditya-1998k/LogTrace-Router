"""Hello Python"""

def divide_two_number(a,b):
    try:
        result = a/b
        message = f"Division Successfull: {a} / {b} = {result}"
        print(message)
    except ZeroDivisionError as e:
        error_message = f"Error: Division by zero - {e}"
        print(message)

if __name__ == "__main__":
    divide_two_number(10, 5)
    divide_two_number(10, 0)