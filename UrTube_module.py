from User_module import User
from Video_module import Video


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f"Welcome {self.current_user.nickname}")
                break
            else:
                print("User not found")

    def register(self, nickname, password, age):
        sameUser = False
        for user in self.users:
            if user.nickname == nickname:
                sameUser = True
                print("This user already exist")
                self.log_in(nickname=nickname, password=password)
                break
        if not sameUser and isinstance(password, str) and isinstance(age, int):
            self.users.append(
                User(
                    nickname=nickname,
                    password=password.__hash__(),
                    age=age
                )
            )

    def log_out(self):
        self.current_user = None

    def add(self, *video):

