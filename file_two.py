# python module to import

print("file two __name__ is set to: {}".format(__name__))

if(__name__ == "__main__"):
    print("file two executed when ran directly")
else:
    print("file two executed when imported")
