email = None
message = None


def init() -> None:
    global email, message
    sqlite_connect = SqliteConnect()
    email = Email(sqlite_connect)
    message = Message(sqlite_connect)


class SqliteConnect:
    def __init__(self):
        pass

    def find(self):
        pass


class Email:
    def __init__(self, connect: SqliteConnect):
        self.connect = connect

    def find(self):
        pass


class Message:
    def __init__(self, connect: SqliteConnect):
        self.connect = connect

    def find(self):
        pass
