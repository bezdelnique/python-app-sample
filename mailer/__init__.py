import repository

_email_repository = None
email = None


def init(email_repository: repository.Email) -> None:
    global _email_repository
    global email
    _email_repository = email_repository
    email = Mailer(_email_repository)


class Mailer:
    def __init__(self, email_repository: repository.Email):
        self.email_repository = email_repository

    def find(self):
        pass
