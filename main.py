import repository
import mailer


def bar():
    repository.message.find()


def foo():
    repository.email.find()


if __name__ == '__main__':
    repository.init()
    mailer.init(repository.email)

    bar()
    foo()
