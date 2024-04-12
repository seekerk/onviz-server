![](https://byob.yarr.is/seekerk/onviz-server/pylint)
# onviz-server
Сервер для сбора данных с камер onviz и рассылки уведомлений в телеграм

## Структура проекта
* [onviz_main](onviz_main) - ядро сервера Django
* [tg_bot](tg_bot) - приложение для запуска бота Telegram. Использует БД сервера для определения получателей сообщений. 
* [ftp_server](ftp_server) - FTP сервер для получения фото/видео данных с камер
* [web_server](web_server) - веб сервер для настройки системы, добавления камер, просмотра данных и т.п.

## Настройка
Для настройки создать файл в `onviz_main/.env`
Допустимые параметры настройки и их дефолтные значения см. в [onviz_main/settings.py](onviz_main/settings.py).

## Установка в виде сервиса

Все скрипты запуска серверов в виде сервисов находятся в каталоге [tools/systemd]().
По умолчанию, проект склонирован в /opt/onviz-server и создано окружение в `/opt/onviz-server/.venv`.

1. Установить требуемые библиотеки через `pip install -r requirements.txt`
2. Скопировать файлы *.service из каталога [tools/systemd]() в `/ets/systemd/system`
3. Перезагрузить systemd с помощью команды `systemctl daemon-reload`
4. Активировать сервисы `systemctl enable onviz-ftp-server.service`
5. Запустить сервисы `systemctl start onviz-ftp-server.service`
