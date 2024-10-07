from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname
class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title #название
        self.duration = duration #Продолжительность
        self.time_now = 0 #Секунда остановки
        self.adult_mode = adult_mode #ограничение по возрасту

class UrTube:
    def __init__(self):
        self.users = [] # Список пользователей
        self.videos = [] # Список видео
        self.current_user = None # Текущий пользователь

    def log_in(self, nickname, password):
        for _ in self.users:
            if _.nickname == nickname and _.password == hash(password):
                self.current_user = _
                print(f"Вы вошли в аккаунт пользователя под ником {_.nickname}")
            else:
                print("Такого пользователя не существует!")
    def register(self, nickname, password, age):
        if len(self.users) == 0:
            i = User(nickname, password, age)
            print(f"Вы зарегистрировались и вошли в аккаунт пользователя {i.nickname}")
            self.current_user = i
            self.users.append(i)
        else:
            c = 0
            for _ in self.users:
                if _.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    c += 1
            if c == 0:
                i = User(nickname, password, age)
                print(f"Вы зарегистрировались и вошли в аккаунт пользователя {i.nickname}")
                self.current_user = i
                self.users.append(i)
    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *Videos):
        for _ in Videos:
            if len(self.videos) == 0:
                self.videos.append(_)
                print(f"Видео под названием '{_.title}' успешно загружено")
            else:
                c = 0
                for i in self.videos:
                    if _.title == i.title:
                        print("Видео с таким названием уже существует")
                        c += 1
                if c == 0:
                    self.videos.append(_)
                    print(f"Видео под названием '{_.title}' успешно загружено")

    def get_videos(self, search_word):
        a = []
        for _ in self.videos:
            if search_word.lower() in _.title.lower() or _.title.lower() in search_word.lower():
                a.append(_.title)
        print(f"По вашему запросу найдено {len(a)} результат(а)(ов)")
        return a

    def watch_video(self, name_of_film):
        for _ in self.videos:
            if _.title == name_of_film:
                if self.current_user == None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    break
                elif self.current_user.age < 18 and _.adult_mode == True:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break
                else:
                    c = 1
                    while _.time_now <= _.duration:
                        print(f"Текущее время просмотра: {_.time_now} сек.")
                        _.time_now += 1
                        sleep(1)
                    print("Конец видео")
                    _.time_now = 0
                    break

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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


