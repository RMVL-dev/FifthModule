from User_module import User
import time

from Video_module import Video


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password.__hash__():
                self.current_user = user
                break

    def register(self, nickname, password, age):
        sameUser = False
        for user in self.users:
            if user.nickname == nickname:
                sameUser = True
                print(f"Пользователь {nickname} уже существует")
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
            self.log_in(nickname=nickname, password=password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, query):
        filtered_videos = []
        for video in self.videos:
            if isinstance(video.title, str) and isinstance(query, str) and query.lower() in video.title.lower():
                filtered_videos.append(video.title)

        return filtered_videos

    def watch_video(self, video_title):
        current_video = None
        for video in self.videos:
            if video.title == video_title:
                current_video = video

        if current_video is None:
            print("Видео не найдено")
            return

        if self.current_user is not None:
            if current_video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                for sec in range(current_video.time_now, current_video.duration+1):
                    current_video.time_now = sec
                    print(sec)
                    time.sleep(1)
                print("Конец видео")
                if current_video.time_now == current_video.duration:
                    current_video.time_now = 0
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')