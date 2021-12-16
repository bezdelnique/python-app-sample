import repository


def bar():
    repository.message.find()


def foo():
    repository.email.find()


if __name__ == '__main__':
    bar()
    foo()
