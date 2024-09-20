import numbers


class User:
    def __init__(self, nickname, password, age):
        if isinstance(password, int):
            self.password = password
            self.nickname = nickname
            self.age = age
        else:
            print("Пароль не прошел проверку")

    def __eq__(self, other):
        if isinstance(other, User):
            return self.password == other.password
        elif isinstance(other, numbers.Number):
            return self.password == other
        elif isinstance(other, str):
            return self.password == other.__hash__()
        else:
            return False
