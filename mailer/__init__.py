import repository

email_repository_ = None


def init(email_repository: repository.Email) -> None:
    global email_repository_
    email_repository_ = email_repository


class Mailer:
    def __init__(self, email_repository):
        self.email_repository = email_repository

    def find(self):
        pass


email = Mailer(email_repository_)
