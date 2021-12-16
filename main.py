import repository
import mailer


def bar():
    repository.message.find()


def foo():
    repository.email.find()


if __name__ == '__main__':
    mailer.init(repository.email)

    bar()
    foo()
