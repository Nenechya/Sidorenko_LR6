
def user_inp():
    while 1:
        print("Input a number:")
        a = input()
        try:
            x = float(a)
            if x > 0:
                return x
            else:
                print("Not a positive")
        except ValueError:
            print("Not a number")

def t_ver_user_inp(y):
    try:
        x = float(y)
        if x > 0:
            return x
        else:
            print("Not a positive")
            return False
    except ValueError:
        print("Not a number")
        return False

def average_grade(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def is_good(num1, num2, num3):
    if average_grade(num1, num2, num3) > 4:
        print("Final grade is good")
        return True
    return False