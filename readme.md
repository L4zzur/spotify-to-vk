# Spotify to VK Bio

#### Отображает в статусе VK тот трек, который сейчас играет в Spotify / Display your current listen to a song from Spotify in the VK bio.
![1.1](img/1.png)

# Установка / Installation:

1. Склонировать репозиторий / Clone repository:
```bash
$ git clone https://github.com/L4zzur/spotify-to-telegram.git
```

2. Перейти в папку "spotify-to-telegram" / Go to "spotify-to-telegram" folder:
```bash
$ cd spotify-to-telegram
```

3. Установить зависимости с помощью pip / Install libraries using pip:
```bash
$ pip3 install -r requirements.txt
```

# Настройка / Setting up:

### Telegram:

1. Переходим на [vkhost.github.io](https://vkhost.github.io/) / Go to [vkhost.github.io](https://vkhost.github.io/)
2. Выбираем Kate Mobile / Choose Kate Mobile:
![1.2](img/2.png)
3. Разрешаем доступ через свой аккаунт / Allow access through your account
4. Скопируйте часть адресной строки от `access_token=` до `&expires_in` / Copy the part of the address bar from `access_token=` to `&expires_in`
> Никому не сообщайте эти данные / Don't share this tokens with anyone

### Spotify
1. Переходим на [Spotify Dashboard](https://developer.spotify.com/dashboard/) / Go to [Spotify Dashboard](https://developer.spotify.com/dashboard/)
2. Авторизуемся и создаем новое приложение / Log in and create a new application 
![1.3](img/3.png)
3. Переходим в созданное приложение, а затем в настройки / Go to the created application, and then in settings
![1.4](img/4.png)
4. Изменяем строчку Redirect URIs на http://localhost:8888/callback / Changing the Redirect URIs line to http://localhost:8888/callback
![1.5](img/5.png)
> Никому не сообщайте эти данные / Don't share this tokens with anyone

### Python
1. Заходим в директорию со скриптом (шаг 2 из установки) / Go to the script directory (step 2 from the installation)
2. Запускаем скрипт для настройки / Run the script to configure:
```bash
$ python3 setup.py
```
4. Заполняем все нужные данные, которые мы получили ранее, как просит скрипт / Fill all the necessary data that we received earlier, as requested by the script.
5. Авторизуем наше приложение Spotify через ссылку, которую вернул скрипт. Либо же можно заполнить конфиг самостоятельно в файле config.py / Authorizing our Spotify application through the link that the script returned. Or you can fill in the config yourself in the config.py file

![1.6](img/6.png)

# Запуск / Run
1. Запускаем скрипт / Run script:
```bash
$ python3 main.py
```
2. Проходим авторизацию Telegram / Pass to the Telegram authorization 
3. Радуемся! / Enjoy!