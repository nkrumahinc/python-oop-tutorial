# python module to import

print("file two __name__ is set to: {}".format(__name__))


def function_three():
    print("Function three is executed")


def function_four():
    print("Function four is executed")


if(__name__ == "__main__"):
    print("file two executed when ran directly")
else:
    print("file two executed when imported")
