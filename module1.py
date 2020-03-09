'''
Hello to my first function

It will help you to calculate needed element of Fibonacci`s numbers

'''


def fibNumb(number):
    if number > 0:
        if (number == 1) | (number == 2):
            return 1
        else:
            return fibNumb(number - 1) + fibNumb(number - 2)
    else:
        print("input error")


