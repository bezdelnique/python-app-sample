import repository


def bar():
    repository.message_repository.find()


def foo():
    repository.message_repository.find()


if __name__ == '__main__':
    bar()
    foo()
