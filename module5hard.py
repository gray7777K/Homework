from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user.nickname in [user.nickname for user in self.users]:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
            self.current_user = user
            print(f'Пользователь {nickname} добавлен в систему; осуществлен вход в систему')

    def log_in(self, nickname, password):
        contains = False
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                contains = True
            else:
                continue
        if contains == False:
            print('Такого пользователя нет, или пароль указан неверно')
        else:
            print(f'Пользователь {self.current_user.nickname} вошел в систему')

    def log_out(self):
        print(f'Пользователь {self.current_user.nickname} вышел из системы')
        self.current_user = None

    def add(self, *video):
        for i in video:
            if i.title.lower() not in [video.title.lower() for video in self.videos]:
                self.videos.append(i)
                print(f'Видео "{i.title}" добавлено в систему')
            else:
                print(f'Фильм "{i.title}" уже существует)')
                continue

    def get_videos(self, keyword):
        is_contain = []
        for i in range(0, len(self.videos)):
            if keyword.lower() in self.videos[i].title.lower():
                is_contain.append(self.videos[i].title)
            else:
                continue
        print('Указанное слово содержится в названиях следующих фильмов:', is_contain)

    def watch_video(self, video_title):
        current_video = None
        is_contain_ = False
        if self.current_user == None:
            print('Пожалуйста, войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in range(0, len(self.videos)):
                if video_title != self.videos[i].title:
                    continue
                else:
                    current_video = self.videos[i]
                    is_contain_ = True
                    break
            if is_contain_ == False:
                print('Такого видео нет')
            else:
                if current_video.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(0, current_video.duration):
                        current_video.time_now += 1
                        print(f'{current_video.time_now} ', end = '')
                        sleep(1)
                    print('Конец видео')
                    current_video.time_now = 0

video1 = Video('Жизнь студента-айтишника насыщена и разнообразна', 12)
video2 = Video('Ночная жизнь студентов-программистов', 16, adult_mode = True)

ur = UrTube()

ur.add(video1, video2)

ur.watch_video('Жизнь студента-айтишника насыщена и разнообразна')

ur.register('Михалыч', 'Uy69T8#rGWi0$21kjf&7re98@', 46)
ur.register('Мишутка', 'sapog50', 14)

ur.watch_video('Ночная жизнь студентов-программистов')
ur.watch_video('Жизнь студента-айтишника насыщена и разнообразна')

ur.log_in('Михалыч', 'abcde987')
ur.log_in('Михалыч', 'Uy69T8#rGWi0$21kjf&7re98@')

ur.watch_video('Ночная жизнь студентов-программистов')
ur.watch_video('Новости программирования на питоне 2024')

ur.log_out()

ur.get_videos('Программист')
ur.get_videos('ЖИЗНЬ')
ur.get_videos('Студент')
